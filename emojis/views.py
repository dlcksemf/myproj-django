from rest_framework import viewsets

from emojis.serializers import EmojisSerializer
from emojis.models import Emojis


class EmojisViewSet(viewsets.ModelViewSet):
    queryset = Emojis.objects.all()
    serializer_class = EmojisSerializer
