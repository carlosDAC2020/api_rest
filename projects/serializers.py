from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # atributos a obtener
        fields = ("id","title","descrition","tecnology", "created_at")
        # atributos no modificables 
        read_only_fields = ('created_at',)
        