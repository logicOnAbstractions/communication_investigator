# decorators - centralizing the handling of some common, repetitive things such as logging headers from http response &
# try/excepts
from functools import wraps
from utils import *
from utilities.logger import get_root_logger
LOG = get_root_logger(BASE_LOGGER_NAME)

def api_calls_wrapper(func):
    """ does basic error-handling for us as well as logging all http headers responses for further analysis """
    @wraps(func)
    def func_wrap(*args, **kwargs):
        try:
            response =  func(*args, **kwargs)
            LOG.info(f"Response headers: {response.headers}")
            LOG.info(f"Status code: {response.status_code}")
            LOG.info(f"URL: {response.url}")
            return response
        except TypeError as type_err:
            print(f"Wrong type!: {type_err}")
            return type_err
        except Exception as ex:
            print(f"Some other error: {ex}")
            return ex
    return func_wrap