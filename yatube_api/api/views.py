from rest_framework.exceptions import ValidationError

from posts.models import Group, Post, Follow
from rest_framework import permissions, viewsets, filters
from rest_framework.generics import get_object_or_404

from .permission import UserIdentificationObject
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer

from rest_framework.pagination import LimitOffsetPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (UserIdentificationObject,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (UserIdentificationObject,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('following__username',)

    def get_queryset(self):
        follow = Follow.objects.filter(user=self.request.user)
        return follow

    def perform_create(self, serializer):
        following = dict(serializer.validated_data)['following']
        check_subscription = self.get_queryset().filter(
            following=following
        )
        if following == self.request.user:
            raise ValidationError('Нельзя на самого себя подписываться!')
        if check_subscription.exists():
            raise ValidationError(f'Вы уже подписаны на {following}')

        return serializer.save(user=self.request.user)
