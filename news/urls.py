from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import ArticleViewSet

app_name = "news"

router = DefaultRouter()
router.register("articles", ArticleViewSet)

urlpatterns = [
    # path("articles.json", article_list),
    path("api/", include(router.urls)),
]