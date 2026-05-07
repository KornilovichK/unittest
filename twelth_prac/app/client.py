from __future__ import annotations
import asyncio
from dataclasses import dataclass

# Data classes
@dataclass
class Response:
    status: int
    payload: dict

# Custom exceptions
class ApiTimeoutError(Exception):
    pass

class ApiResponseError(Exception):
    pass

# Transport interface
class AsyncTransport:
    async def send(self, method: str, path: str) -> Response:
        raise NotImplementedError

# Client implementation
class UserClient:
    def __init__(self, transport: AsyncTransport, *, timeout: float = 0.20, 
                 retries: int = 1, retry_delay: float = 0.01) -> None:
        self._transport = transport
        self._timeout = timeout
        self._retries = retries
        self._retry_delay = retry_delay
    
    async def get_user(self, user_id: int) -> dict:
        # Implementation here
        pass