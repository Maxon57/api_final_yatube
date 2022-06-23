from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Group, Post, Follow, User
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created', 'post')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('pub_date', 'image')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',
                                        read_only=True
                                        )

    class Meta:
        model = Follow
        fields = '__all__'
