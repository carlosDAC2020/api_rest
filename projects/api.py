from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    # llamamos a todos los registros del modelo 
    queryset = Project.objects.all()
    # añadimos los permisos de operaciones con los registros 
    permission_classes = [permissions.AllowAny]
    # serializer en el que se basa el viewset
    serializer_class = ProjectSerializer