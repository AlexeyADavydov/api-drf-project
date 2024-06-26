from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets, permissions, mixins
from posts.models import Post, Group, Comment, Follow
from .serializers import (FollowSerializer,
                          GroupSerializer,
                          CommentSerializer,
                          PostSerializer)

from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

from django.contrib.auth import get_user_model
User = get_user_model()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id')
        )
        serializer.save(
            author=self.request.user,
            post=post,
        )

    def get_queryset(self):
        post = get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id')
        )
        return post.comments.all()


class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.user_subscriptions.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
