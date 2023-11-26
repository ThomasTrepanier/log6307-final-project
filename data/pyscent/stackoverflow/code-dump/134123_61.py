import boto3
import threading
import time
from queue import LifoQueue, Empty


class DDBTableCleaner(object):

    def __init__(self, table_name, threads_limit=32):
        self._queue = LifoQueue()
        self._threads = dict()
        self._cnt = 0
        self._done = False
        self._threads_limit = threads_limit
        dynamodb_client = boto3.resource('dynamodb')
        self.table = dynamodb_client.Table(table_name)

    def run(self):
        for i in range(self._threads_limit):
            thread_name = f'worker_thread_{i}'
            self._threads[thread_name] = threading.Thread(
                target=self.worker_thread,
                name=thread_name,
            )
            self._threads[thread_name].start()
        self.queue_replenish()
        while self._queue.qsize() > 0:
            print(f'items processed: ({self._cnt})')
            time.sleep(1)
        self._done = True
        for thread in self._threads.values():
            if thread.is_alive():
                thread.join()
        print(f'items processed: ({self._cnt})')

    def queue_replenish(self):
        table_key_names = [key.get('AttributeName') for key in self.table.key_schema]
        projection_expression = ', '.join('#' + key for key in table_key_names)
        expression_attr_names = {'#' + key: key for key in table_key_names}
        page = self.table.scan(
            ProjectionExpression=projection_expression,
            ExpressionAttributeNames=expression_attr_names
        )
        while page['Count'] > 0:
            for item in page['Items']:
                self._queue.put(item)
            if 'LastEvaluatedKey' in page:
                page = self.table.scan(
                    ProjectionExpression=projection_expression,
                    ExpressionAttributeNames=expression_attr_names,
                    ExclusiveStartKey=page['LastEvaluatedKey']
                )
            else:
                break

    def worker_thread(self):
        thr_name = threading.current_thread().name
        print(f'[{thr_name}] thread started')
        with self.table.batch_writer() as batch:
            while not self._done:
                try:
                    item = self._queue.get_nowait()
                except Empty:
                    time.sleep(1)
                else:
                    try:
                        batch.delete_item(Key=item)
                        self._cnt += 1
                    except Exception as e:
                        print(e)
        print(f'[{thr_name}] thread completed')


if __name__ == '__main__':

    table = '...'
    cleaner = DDBTableCleaner(table, threads_limit=10)
    cleaner.run()


