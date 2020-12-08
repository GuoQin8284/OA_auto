import logging


def log_method(func):
    def wrapper(*args,**kwargs):
        wrapper.__name__ = func.__name__
        global result
        try:
            result = func(*args,**kwargs)
            logging.info("调用了{}方法,参数为{},{}".format(func.__name__,*args,**kwargs))
        except Exception as f:
            logging.error("调用{}方法出错：{}".format(func.__name__,f))
        return result

    log_method.__name__ = wrapper.__name__
    return wrapper