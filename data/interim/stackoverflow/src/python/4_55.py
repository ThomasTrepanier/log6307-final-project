from multiprocessing import set_start_method
from multiprocessing import Process, Manager
try:
    set_start_method('spawn')
except RuntimeError:
    pass
@app.get("/article_classify")
def classification(text:str):
    """function to classify article using a deep learning model.
    Returns:
        [type]: [description]
    """
    manager = Manager()

    return_result = manager.dict()
    # as the inference is failing 
    p = Process(target = inference,args=(text,return_result,))
    p.start()
    p.join()
    # print(return_result)
    result = return_result['all_tags']
    return result
