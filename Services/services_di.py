from injector import Binder
from Services.dummyService import MyService

def configure_services(binder: Binder):
    binder.bind(MyService, to=MyService)
    print("[INFO] MyService bound in services_di")
