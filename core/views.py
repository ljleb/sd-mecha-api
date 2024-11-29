from rest_framework.views import APIView as RestAPIView
from rest_framework.permissions import IsAuthenticated


class ApiView(RestAPIView):
    # permission_classes = [IsAuthenticated]
    pass
