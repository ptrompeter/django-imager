from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

PUB_CHOICES = [('pr', 'Private'), ('s', 'Shared'), ('pub', 'Public')]


@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='albums',
                             )
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Photo(models.Model):
    title = models.CharField(max_length=30, default="")
    image = models.ImageField(upload_to='photo_files/%Y-%m-%d')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='photos',
                             )
    albums = models.ManyToManyField(Album, related_name='photos')
    desc = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    cover_photo = models.ForeignKey(Album,
                                    on_delete=models.CASCADE,
                                    related_name='cover',
                                    default=False)

    published = models.CharField(max_length=30,
                                 choices=PUB_CHOICES,
                                 default='pub')

    def __str__(self):
        return self.img_name
