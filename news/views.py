from rest_framework import viewsets
from news.serializers import ArticleSerializers
from news.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
