from fastapi import Request
import logging

class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, request: Request, call_next):
        logger = logging.getLogger("uvicorn")
        logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        return response
