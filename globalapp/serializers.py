from rest_framework import serializers
from .models import Projects, Contributors, Issues, Comments


class ProjectsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = "__all__"

class ContributorsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contributors
        fields = "__all__"


class IssuesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = "__all__"


class CommentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"
