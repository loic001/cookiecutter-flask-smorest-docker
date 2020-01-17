from .models import Entity

def service(args):
    return list(Entity.object())