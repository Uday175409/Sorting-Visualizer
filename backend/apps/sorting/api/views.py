from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SortRequestSerializer, SortResponseSerializer
from ..services.sort_factory import SortFactory

class SortView(APIView):
    def post(self, request):
        serializer = SortRequestSerializer(data=request.data)
        if serializer.is_valid():
            algorithm = serializer.validated_data['algorithm']
            array = list(serializer.validated_data['array'])
            
            try:
                result = SortFactory.sort(algorithm, array)
                return Response(result, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
