from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
    
    def ready(self):
        from django.db.models.signals import post_save
        from .models import Comment,Post
        from .signals import create_comment_notification
        post_save.connect(create_comment_notification, sender=Comment)
