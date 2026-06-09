from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Detail

@api_view(['GET'])
def index(request):
    return Response("Hey Extras!!! This is the ulitmate appreciation page for the Great Explosion Murder God Dynamight!")

@api_view(['GET'])
def general_details(request):
    details = Detail.objects.first()
    if details is None:
        return Response({"error": "data not found"}, status=404)
    return Response(details.detail)
