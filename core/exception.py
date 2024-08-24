from typing import Dict, Any, Optional
from aiohttp import ClientResponse
from core import settings
from http import HTTPStatus


# https://fastapi.tiangolo.com/tutorial/handling-errors/#handling-errors
# https://docs.python.org/3/library/http.html#http.HTTPStatus

class EtherException(Exception):
    service_name: str = settings.service_name
    error_code: str
    status_code: HTTPStatus
    message: str
    detail: Optional[str]
    data: Optional[Dict[str, Any]]
    error: Optional[BaseException]

    def __init__(self, error: BaseException, error_code: str, status_code: HTTPStatus, message: str, detail: str,
                 data: Optional[Dict[str, Any]] = None):
        self.error_code = error_code
        self.message = message or error_code
        self.status_code = status_code
        self.detail = detail
        self.data = data
        self.error = error


class EtherRestClientException(Exception):
    status_code: int
    request_url: str
    request_method: str
    response_body: Any

    def __init__(self, response: ClientResponse, response_body: Any):
        self.status_code = response.status
        self.request_url = str(response.real_url)
        self.request_method = response.request_info.method
        self.response_body = response_body
