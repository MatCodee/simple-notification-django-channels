from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Comment, Notification

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, **kwargs):
    if kwargs.get('created', False):
        ContentType.objects.get_for_model(instance)
        Notification.objects.create(
            user=instance.author,
            message=f'{instance.author.username} comentó en tu publicación "{instance.post.title}"',
        )
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "notification_message",
                "text": f"{instance.author.username} comentó en tu publicación \"{instance.post.title}\"",
            },
        )