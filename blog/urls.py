from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, post_list

app_name = "blog"

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("posts.json", post_list),
    path("api/", include(router.urls)),
]