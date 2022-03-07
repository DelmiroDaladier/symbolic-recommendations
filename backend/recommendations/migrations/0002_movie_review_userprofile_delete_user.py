# Generated by Django 4.0.3 on 2022-03-06 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_title', models.CharField(default='dafault title', max_length=500)),
                ('sysnopsis', models.TextField(max_length=1000)),
                ('symbolic_synopsis', models.JSONField(null=True)),
                ('actors', models.JSONField()),
                ('symbolic_actors', models.JSONField(null=True)),
                ('movie_genres', models.JSONField()),
                ('symbolic_movie_genres', models.JSONField(null=True)),
                ('director', models.TextField(max_length=100)),
                ('symbolic_director', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendations.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]