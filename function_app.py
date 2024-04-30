import azure.functions as func
import datetime
import json
import logging
from app import app

fapp = func.FunctionApp()

@fapp.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    return func.WsgiMiddleware(app.wsgi_app).handle(req)

#@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
#def http_trigger(req: func.HttpRequest) -> func.HttpResponse: