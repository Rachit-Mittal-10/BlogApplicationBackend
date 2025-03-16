from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Roles
from .serializers import RoleSerializers 

# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    """
    - creates the viewset for manages role instancaes and provides the basic CRUD operations.
    """
    queryset = Roles.objects.all()
    serializer_class = RoleSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        : configuring the response for the post api for api/roles path
        """
        response = super().create(request, args, kwargs)
        return Response(
            data = {
                "message": "Role Successfully created"
            },
            status=status.HTTP_201_CREATED
        )