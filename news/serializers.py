import re
from rest_framework import serializers
from news.models import Article


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "content", "photo", "created_at", "updated_at"]
    #
    # def validate_title(self, title):
    #     if len(title) < 3:
    #         raise serializers.ValidationError("3글자 이상!!")
    #     if not re.search(r"[ㄱ-힣]", title):
    #         raise serializers.ValidationError("한글로 입력해주세요")
    #     return title

# # 비로그인 사용자용
# class ArticleAnonymousSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["id", "title", "content"]
#
#
# # 골드멤버쉽 사용자용
# class ArticleGoldMembershipSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["id", "title", "content", "photo"]
#
#
# # 관리자용
# class ArticleAdminSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["id", "title", "content", "photo", "created_at", "updated_at"]
