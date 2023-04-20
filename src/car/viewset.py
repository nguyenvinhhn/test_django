from django.http import JsonResponse
from .models import Car

def getJson(request):
    obj = Car.objects.all()
    data = { "result" :list( obj.values("id", "name", "color", "brand") ) }
    return JsonResponse(data)