from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(TimeStampedModel):
    title = models.CharField(
        max_length=100,
        db_index=True,
        validators=[
            MinLengthValidator(3),
            RegexValidator(r"[ㄱ-힣]", message="한글로 입력해주세요"),
        ],
    )
    content = models.TextField()

    photo = models.ImageField(blank=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
