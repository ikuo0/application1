import azure.functions as func
import datetime
import json
import logging
import app as app

fapp = func.FunctionApp()

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.WsgiMiddleware(app.app.wsgi_app).handle(req)

