from pydantic import BaseModel
class ErrorReport(BaseModel):
    function_name: str
    module: str
    args_repr: str
    kwargs_repr: str
    exception_type: str
    exception_message: str
    traceback: str
    source_code: str | None = None
