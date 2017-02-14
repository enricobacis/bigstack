import sys as _sys
import types as _types
import functools as _functools
import threading as _threading
import multiprocessing.pool as _mpool

_k = (2 ** 10)
_M = (2 ** 10) * _k
_G = (2 ** 10) * _M

_lock = _threading.Lock()

def bigstack(*args, **kwargs):
    '''Decorator that increases the stack size of a function and the recursion
    limit. The function runs in a separated thread with a stack size specified
    by the 'stacksize' parameter (default: 128MiB). Also the recursion limit can
    be modified by the 'recursionlimit' parameter (default: 1M), but be aware
    that this is a variable shared by the whole python environment, so a
    subsequent invocation of a decorated function may change it.'''

    stacksize = kwargs.get('stacksize', 128 * _M)
    recursionlimit = kwargs.get('recursionlimit', _M)

    def _decorator(fn):
        '''This is the bigstack decorator itself.'''

        @_functools.wraps(fn)
        def _fn(*args, **kwargs):

            # no two functions can change the stack size
            with _lock:
                _threading.stack_size(stacksize)
                _sys.setrecursionlimit(recursionlimit)

                # only new threads get the redefined stack size
                pool = _mpool.ThreadPool(processes=1)

            async_result = pool.apply_async(fn, args, kwargs)
            return async_result.get()

        return _fn

    if not args:
        return _decorator

    # return the decorated function when used without keyword arguments
    if not isinstance(args[0], _types.FunctionType):
        raise ValueError('use keyword argument as bigstack parameters')
    return _decorator(args[0])
