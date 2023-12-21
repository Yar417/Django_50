from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # add new name with directory
    name = 'modules.blog'
    # add rus naming
    verbose_name = 'Блог'
