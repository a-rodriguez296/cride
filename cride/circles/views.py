from rest_framework.decorators import api_view
from rest_framework.response import Response

from cride.circles.models import Circle
from cride.circles.serializers import CircleSerializer

@api_view(['GET'])
def list_circles(request):
    
    #esta sentencia no se evalua en la base de datos. Solo hasta cuando se hace el for
    circles = Circle.objects.all()
    public = circles.filter(is_public=True)
    data = []

    for circle in public:
        serializer = CircleSerializer(circle)
        data.append(serializer.data)
    
    return Response(data)


@api_view(['POST'])
def create_circle(request):
    name = request.data['name']
    slug_name = request.data['slug_name']
    about = request.data.get('about', '')

    #Con esto se guarda el objeto en la base de datos
    circle = Circle.objects.create(name=name, slug_name=slug_name, about=about)
    data = {
        'name': circle.name,
        'slug_name': circle.slug_name,
        'rides_taken': circle.rides_taken,
        'rides_offered': circle.rides_offered,
        'members_limit': circle.members_limit, 
        'about': circle.about
    }
    return Response(data)



