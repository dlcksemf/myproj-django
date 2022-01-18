from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from news.models import Article
from news.serializers import ArticleSerializers


# list, detail, create, update, delete를 1개의 ViewSet에서 지원
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    # 유효성 검사가 끝나고 나서
    # 실제 serializer.save()를 할 때 수행 되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않습니다.
        # 대신 키워드 인자를 통한 속성 지정을 지원합니다.
        serializer.save(author=self.request.user)
