# Create your tests here.
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album
from imager_profile.tests import UserFactory


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    image = factory.django.ImageField(color='blue')

class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

class PhotoTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(
            username='bob',
            email='bob@dobalina.com',
        )
        self.user.set_password('secret')


        self.album = AlbumFactory.create(
            name='an_album',
            user= self.user,
        )

        self.photo = PhotoFactory.create(
            img_name='image01',
            user = self.user,
            # albums = self.album
        )
        # self.photo.albums = self.album

    def test_photo_exists(self):
        self.assertTrue(self.photo)

    def test_image_has_image(self):
        self.assertIsInstance(self.photo.image, ImageFieldFile)

    def test_photo_has_user(self):
        self.assertEquals(self.photo.user, self.user)

    # def test_photo_has_album(self):
    #     self.assertEquals(self.photo.albums, self.album)

class AlbumTestCase(TestCase):

    def setUp(self):

        self.user = UserFactory.create(
            username='bob',
            email='bob@dobalina.com',
        )
        self.album = AlbumFactory.create(
            name='an_album',
            user= self.user,
        )

    def test_album_exists(self):
        self.assertTrue(self.album)

