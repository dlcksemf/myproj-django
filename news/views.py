import json
from django.http import HttpResponse
from rest_framework import viewsets

# from news.serializers import ArticleAdminSerializers, ArticleAnonymousSerializers, ArticleGoldMembershipSerializers
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from news.models import Article
from rest_framework.generics import ListAPIView
from news.serializers import ArticleSerializers


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    # permission_classes = [AllowAny] # DRF 디폴트 설정
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_serializer_class(self):
    #     # return ArticleAdminSerializers
    #     return ArticleGoldMembershipSerializers
    #     # return ArticleAnonymousSerializers
    #
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #
    #     query = self.request.query_params.get("query", "")
    #     if query:
    #         qs = qs.filter(title__icontains=query)
    #
    #     year = self.request.query_params.get("year", "")
    #     if year:
    #         qs = qs.filter(created_at__year=year)
    #
    #     return qs


# article_list = ListAPIView.as_view(
#     queryset=Article.objects.all(),
#     serializer_class=ArticleSerializers,
# )


# step 1
# def article_list(request):
#     qs = Article.objects.all()
#
#     # 2
#     serializer = ArticleSerializers(qs, many=True)
#     data = serializer.data
#
#     # data = [
#     #     {
#     #         "id": article.id,
#     #         "title": article.title,
#     #         "content": article.content,
#     #         "photo": request.build_absolute_uri(article.photo.url) if article.photo else None,
#     #         "created_at": article.created_at.strftime("%Y-%M-%D"),
#     #         "updated_at": article.updated_at.strftime("%Y-%M-%D"),
#     #     }
#     #     for article in qs
#     # ]
#     json_string = json.dumps(data)
#
#     return HttpResponse(json_string)
#
