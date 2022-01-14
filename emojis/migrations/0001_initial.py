# Generated by Django 3.2.11 on 2022-01-14 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emojis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('apple_name', models.CharField(db_index=True, max_length=100)),
                ('other_names', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('Smileys & People', 'Smileys & People'), ('Animals & Nature', 'Animals & Nature'), ('Food & Drink', 'Food & Drink'), ('Activity', 'Activity'), ('Travel & Places', 'Travel & Places'), ('Objects', 'Objects'), ('Symbols', 'Symbols'), ('Flags', 'Flags')], db_index=True, default='Person', max_length=50)),
                ('removed', models.BooleanField(default=False)),
                ('released_date', models.CharField(max_length=15)),
                ('released_emoji_version', models.CharField(db_index=True, max_length=20)),
                ('apple_version', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
