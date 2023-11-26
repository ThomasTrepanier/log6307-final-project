import boto3
import threading
import time
from queue import LifoQueue, Empty
from tqdm.notebook import tqdm

class DDBTableCleaner(object):
    def __init__(self, table_name, profile_name, threads_limit=32):
        self._pbar = None
        self._queue = LifoQueue()
        self._threads = dict()
        self._cnt = 0
        self._done = False
        self._threads_limit = threads_limit
        self._table_name = table_name
        self.session = boto3.Session(profile_name=profile_name)
        dynamodb_client = self.session.resource('dynamodb')
        self.table = dynamodb_client.Table(table_name)

    def run(self):
        if bool(self._pbar):
            self._pbar.close()

        self._pbar = tqdm(desc=self._table_name)
        for i in range(self._threads_limit):
            thread_name = f'worker_thread_{i}'
            self._threads[thread_name] = threading.Thread(
                target=self.worker_thread,
                name=thread_name,
            )
            self._threads[thread_name].start()
        self.queue_replenish()
        while self._queue.qsize() > 0:
            # print(f'items processed: ({self._cnt})')
            time.sleep(1)
        self._done = True
        for thread in self._threads.values():
            if thread.is_alive():
                thread.join()
        self._pbar.close()
        print(f'items processed: ({self._cnt})')

    def queue_replenish(self):
        table_key_names = [key.get('AttributeName') for key in self.table.key_schema]
        projection_expression = ', '.join('#' + key for key in table_key_names)
        expression_attr_names = {'#' + key: key for key in table_key_names}
        total_read = 0
        page = self.table.scan(
            ProjectionExpression=projection_expression,
            ExpressionAttributeNames=expression_attr_names
        )
        while page['Count'] > 0:
            total_read += page['Count']
            for item in page['Items']:
                self._queue.put(item)
            # print("Still reading... Total read: %d" % total_read)
            self._pbar.total = total_read
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
        # print(f'[{thr_name}] thread started')
        with self.table.batch_writer() as batch:
            while not self._done:
                try:
                    item = self._queue.get_nowait()
                except Empty:
                    # print("Empty queue")
                    time.sleep(1)
                else:
                    try:
                        batch.delete_item(Key=item)
                        self._pbar.update(1)
                        self._cnt += 1
                    except Exception as e:
                        print(e)
        # print(f'[{thr_name}] thread completed')
