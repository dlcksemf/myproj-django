from rest_framework import serializers
from emojis.models import Emojis


class EmojisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emojis
        fields = "__all__"
