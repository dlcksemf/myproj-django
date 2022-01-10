from rest_framework import viewsets
from blog.serializers import PostSerializers
from blog.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers