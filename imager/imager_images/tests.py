
from __future__ import unicode_literals

import datetime

from django.db.models.fields.files import ImageFieldFile
from django.test import TestCase

import factory

from imager_images.models import Album, Photo

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

        self.user_2 = UserFactory.create(
            username='sally',
            email='sally@example.com',
        )
        self.user_2.set_password('moresecret')

        self.album = AlbumFactory.create(
            name='an_album',
            user=self.user,
            date_created=datetime.datetime.now(),
            date_modified=datetime.datetime.now(),
            date_published=datetime.datetime.now(),
        )

        self.photo = PhotoFactory.create(
            title='image01',
            user=self.user,
            date_created=datetime.datetime.now(),
            date_modified=datetime.datetime.now(),
            date_published=datetime.datetime.now(),
        )
        self.photo.albums.add(self.album)

    def test_photo_exists(self):
        self.assertTrue(self.photo)
        self.assertIsInstance(self.photo, Photo)

    def test_image_has_image(self):
        self.assertIsInstance(self.photo.image, ImageFieldFile)

    def test_photo_has_user(self):
        self.assertEquals(self.photo.user, self.user)

    def test_photo_in_user(self):
        self.assertIn(self.photo, self.user.photos.all())

    def test_photo_has_album(self):
        self.assertIn(self.album, self.photo.albums.all())

    def test_album_exists(self):
        self.assertTrue(self.album)

    def test_add_friends(self):
        bob_pr = self.user_1.profile
        bob_pr.friends.add(self.user_2)
        self.assertEqual(bob_pr.friends.all()[0], self.user_2)
        self.assertEqual(self.user_2.friend_of.all()[0], self.user_1.profile)

    def test_not_friends(self):
        sally_pr = self.user_2.profile
        self.assertNotIn(self.user_1.profile, sally_pr.friends.all())

    def test_user_username(self):
        self.assertEqual(self.user.username, 'bob')

    def test_email(self):
        self.assertEqual(self.user_2.email, 'sally@example.com')

    def test_str(self):
        sally_pr = self.user_2.profile
        self.assertEquals(str(sally_pr), 'sally')
        