from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from cride.circles.models import Circle

def list_circles(request):
    
    #esta sentencia no se evalua en la base de datos. Solo hasta cuando se hace el for
    circles = Circle.objects.all()
    public = circles.filter(is_public=True)
    data = []

    for circle in public:
        #print(circle)
        data.append(circle)

    json_data = serialize('json', data)
    print(json_data)
    return JsonResponse(json_data, safe=False)

    #return HttpResponse('hola')