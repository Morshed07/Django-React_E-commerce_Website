from rest_framework.views import APIView
from rest_framework.response import Response
from apps.products.models import Product
from .serializers import ProductSerializer

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all().order_by('id')[0:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)