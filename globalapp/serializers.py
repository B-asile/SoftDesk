from rest_framework import serializers
from .models import Projects


class ProjectsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = "__all__"
        extra_kwargs = {'author_user_id': {'read_only': True}}
