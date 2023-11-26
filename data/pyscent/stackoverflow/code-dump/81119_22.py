from fastapi import FastAPI, BackgroundTasks
import time
app = FastAPI()

def sleep(msg):
    time.sleep(10)
    print(msg)

@app.get('/')
async def root(background_tasks: BackgroundTasks):
    msg= 'Sleeping for 10'
    background_tasks.add_task(sleep, msg)
    print('Awake')
    return {'message': 'hello'}

