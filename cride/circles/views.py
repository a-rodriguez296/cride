from rest_framework.decorators import api_view
from rest_framework.response import Response

from cride.circles.models import Circle

@api_view(['GET'])
def list_circles(request):
    
    #esta sentencia no se evalua en la base de datos. Solo hasta cuando se hace el for
    circles = Circle.objects.all()
    public = circles.filter(is_public=True)
    data = []

    for circle in public:
        #print(circle)
        data.append({
            'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_taken': circle.rides_taken,
            'rides_offered': circle.rides_offered,
            'members_limit': circle.members_limit
        })
    
    return Response(data)