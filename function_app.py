
#import azure.functions as func
#from azure.functions import HttpRequest, HttpResponse
import azure.functions
import datetime
import json
import logging
import app.routes.identity
#from app.routes.middleware import common_middleware
import fastapi
#from fastapi.middleware.trustedhost import TrustedHostMiddleware
#import fastapi.middleware.trustedhost
import time

fast_app = fastapi.FastAPI()

@fast_app.middleware("http")
async def add_process_time_header(request: fastapi.Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print("start_time={}, process_time={}".format(start_time, process_time))
    return response

fast_app.include_router(app.routes.identity.router, prefix="/api/identity")
app = azure.functions.AsgiFunctionApp(app=fast_app, http_auth_level=azure.functions.AuthLevel.ANONYMOUS)
