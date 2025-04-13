from rest_framework.decorators import api_view
from rest_framework.response import Response
from local_businesses.models import LocalBusiness

@api_view(['GET'])
def nearby_businesses(request):
    businesses = LocalBusiness.objects.all()[:10]  # Example query
    data = [{
        'name': biz.name,
        'type': biz.business_type,
        'location': biz.location
    } for biz in businesses]
    return Response(data)