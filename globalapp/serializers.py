from rest_framework import serializers
from .models import Projects, Contributors, Issues, Comments


class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"

        extra_kwargs = {'author_user_id': {'read_only': True},
                        'project_id': {'read_only':True}
                        }


class ContributorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = "__all__"


class IssuesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = "__all__"

        extra_kwargs = {'author_user_id': {'read_only': True},
                        'project_id': {'read_only': True}
                        }


class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
