# Extensions/config_di.py

from injector import Injector, Binder
from fastapi_injector import attach_injector
from Services.services_di import configure_services

def configure_bindings(binder: Binder):
    configure_services(binder)
    print("[INFO] All DI bindings configured")

def register_services(app):
    injector = Injector(configure_bindings)
    attach_injector(app, injector)
    print("[INFO] Services registered using Injector")
