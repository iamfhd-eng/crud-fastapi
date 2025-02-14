from fastapi import Request
from fastapi.responses import JSONResponse

class AuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if not token:
            return JSONResponse(status_code=401, content={"message": "Authorization token missing"})
        response = await call_next(request)
        return response
