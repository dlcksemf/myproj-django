from django.urls import path, include
from rest_framework.routers import DefaultRouter
from emojis.views import EmojisViewSet

app_name = "emojis"

router = DefaultRouter()
router.register("emojis", EmojisViewSet)

urlpatterns = [path("api/", include(router.urls))]
