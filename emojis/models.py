from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Emojis(TimeStampedModel):
    name = models.CharField(max_length=100, db_index=True)
    apple_name = models.CharField(max_length=100, db_index=True)
    other_names = models.CharField(max_length=100, blank=True)

    description = models.TextField(blank=True)

    category = models.CharField(
        max_length=8,
        choices=[
            ("Person", "Smileys & People"),
            ("Nature", "Animals & Nature"),
            ("Food", "Food & Drink"),
            ("Activity", "Activity"),
            ("Travel", "Travel & Places"),
            ("Objects", "Objects"),
            ("Symbols", "Symbols"),
            ("Flags", "Flags"),
        ],
        db_index=True,
        default="Person",
    )

    status = models.CharField(
        max_length=1,
        choices=[
            ("D", "Default"),
            ("C", "Changed"),
            ("R", "Removed"),
        ],
        db_index=True,
        default="D",
    )

    released_date = models.CharField(max_length=15)
    released_emoji_version = models.CharField(max_length=20, db_index=True)

    apple_version = models.ImageField()
    google_version = models.ImageField(blank=True)
    joypixels_version = models.ImageField(blank=True)
    twitter_version = models.ImageField(blank=True)
    samsung_version = models.ImageField(blank=True)
    microsoft_version = models.ImageField(blank=True)
    blob_version = models.ImageField(blank=True)
