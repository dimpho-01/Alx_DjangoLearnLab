from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

CustomUser = get_user_model()

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Post, Like
# Assuming Notification model and logic are implemented and ready to be used

User = get_user_model()

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_409_CONFLICT)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        like = Like.objects.filter(post=post, user=user)
        if like.exists():
            like.delete()
            Notification.objects.filter(recipient=post.author, actor=user, verb='liked', target_id=post.id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)