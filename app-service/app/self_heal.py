import inspect, traceback, httpx, anyio

HEALER_URL = "http://healer-service:8001/report_error"

async def report_error_to_healer(func, exc, args, kwargs):
    try:
        source = inspect.getsource(func)
    except Exception:
        source = None
    payload = {
        "function_name": func.__name__,
        "module": func.__module__,
        "args_repr": repr(args),
        "kwargs_repr": repr(kwargs),
        "exception_type": type(exc).__name__,
        "exception_message": str(exc),
        "traceback": traceback.format_exc(),
        "source_code": source,
    }
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            await client.post(HEALER_URL, json=payload)
        except:
            pass

def self_heal(func):
    if inspect.iscoroutinefunction(func):
        async def async_wrap(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                await report_error_to_healer(func, e, args, kwargs)
                raise
        return async_wrap
    def sync_wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            anyio.run(report_error_to_healer, func, e, args, kwargs)
            raise
    return sync_wrap
