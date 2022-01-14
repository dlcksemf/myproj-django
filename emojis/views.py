from rest_framework import viewsets

from emojis.serializers import EmojisSerializer
from emojis.models import Emojis


class EmojisViewSet(viewsets.ModelViewSet):
    queryset = Emojis.objects.all()
    serializer_class = EmojisSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(name__icontains=query)

        return qs
