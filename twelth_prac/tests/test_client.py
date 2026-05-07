import unittest
from unittest.mock import Mock, AsyncMock, call, patch
from app.client import UserClient, Response, ApiTimeoutError, ApiResponseError

class TestUserClient(unittest.IsolatedAsyncioTestCase):
    
    async def test_success_path(self):
        # Test 1: успешный ответ с нормализацией
        pass
    
    async def test_retry_after_timeout(self):
        # Test 2: retry после timeout
        pass
    
    async def test_retry_after_500(self):
        # Test 3: retry после 5xx ошибки
        pass
    
    async def test_final_timeout_raises_exception(self):
        # Test 4: исчерпание попыток -> ApiTimeoutError
        pass
    
    async def test_404_no_retry(self):
        # Test 5: неретраябельный статус (404)
        pass
    
    async def test_timeout_wiring(self):
        # Test 6: узкий тест на передачу timeout в wait_for
        pass