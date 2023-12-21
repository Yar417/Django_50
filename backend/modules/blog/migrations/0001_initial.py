# Generated by Django 5.0 on 2023-12-20 15:49

import django.core.validators
import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.CharField(blank=True, max_length=255, verbose_name='URL категории')),
                ('description', models.TextField(max_length=300, verbose_name='Описание категории')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'app_categories',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('short_description', models.TextField(max_length=500, verbose_name='Краткое описание')),
                ('full_description', models.TextField(verbose_name='Полное описание')),
                ('thumbnail', models.ImageField(blank=True, upload_to='images/thumbnails/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], verbose_name='Превью поста')),
                ('status', models.CharField(choices=[('published', 'Опубликовано'), ('draft', 'Черновик')], default='published', max_length=10, verbose_name='Статус поста')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('fixed', models.BooleanField(default=False, verbose_name='Зафиксировано')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='authors_post', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('updater', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updater_post', to=settings.AUTH_USER_MODEL, verbose_name='Обновил')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='blog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'app_articles',
                'ordering': ['-fixed', '-time_create'],
                'indexes': [models.Index(fields=['-fixed', '-time_create', 'status'], name='app_article_fixed_e300bf_idx')],
            },
        ),
    ]