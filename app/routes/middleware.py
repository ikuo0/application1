
import fastapi

async def common_middleware(request: fastapi.Request, call_next):
    print("Common middleware executed")
    response = await call_next(request)
    return response

