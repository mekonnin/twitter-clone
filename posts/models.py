from django.db import models
from email.mime import image
from cloudinary.models import CloudinaryField

class Post(models.Model):
    class Meta(object):
        db_table = 'post'
        
    name = models.CharField (
            'name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
        )
    body = models.CharField(
            'Body',blank=True,max_length=140,db_index=True
        )
    created_at = models.DateTimeField(
            'created DateTime', blank=True,auto_now_add=True
        )
    likecount = models.IntegerField(
        'like_count',default=0, blank=True
    )
    image= CloudinaryField(
        'image', blank=True, db_index=True
    )
