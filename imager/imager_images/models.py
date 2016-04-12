from django.db import models
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings

# Create your models here.


@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,
                            related_name='albums',
                            null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Photo(models.Model):
    img_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='photo_files/%Y-%m-%d')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE,
                            related_name='photos',
                            null=True)
    albums = models.ManyToManyField(Album, related_name='photos')

    def __str__(self):
        return self.img_name