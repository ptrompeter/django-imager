# Create your tests here.
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.test import TestCase

import factory

from imager_images.models import Album, Photo

from imager_profile.models import ImagerProfile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    image = factory.django.ImageField(color='blue')


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(
            username='bob',
            email='bob@dobalina.com',
        )
        self.user.set_password('secret')

    def test_user_has_profile(self):
        self.assertTrue(self.user.profile)

    def test_user_pw_is_hashed(self):
        self.assertTrue(len(self.user.password) > 30)

    def test_profile_is_created_when_user_is_saved(self):
        self.assertTrue(ImagerProfile.objects.count() == 1)

    def test_user_is_active(self):
        self.assertTrue(self.user.is_active)

    def test_user_is_inactive(self):
        self.user.is_active = False
        self.assertFalse(self.user.is_active)

    def test_dunder_str(self):
        self.assertEquals(self.user.profile.__str__(), 'bob')


class PhotoTestCase(TestCase):

    def setUp(self):
        """Setup for tests."""
        self.user = UserFactory.create(
            username='buddy',
            email='buddy@example.com'
        )
        self.user.set_password('stuff123')

        self.user_2 = UserFactory.create(
            username='er',
            email='er@example.com'
        )
        self.user_2.set_password('asdf')

        self.image_1 = PhotoFactory.create(
            title="image 1",
            user=self.user,
            description="nature",
        )
        self.image_2 = PhotoFactory.create(
            title="image 2",
            user=self.user,
            description="sports",
        )
        self.image_3 = PhotoFactory.create(
            title="image 3",
            user=self.user,
            description="other title",
        )
        self.album_1 = AlbumFactory.create(
            title='Album',
            description='I haz photoz',
            user=self.user,
            cover_photo=self.image_1
        )

        self.album_2 = AlbumFactory.create(
            title='another album',
            description='with more photos',
            user=self.user,
            cover_photo=self.image_1
        )
        self.album_1.pictures.add(self.image_1)
        self.album_1.pictures.add(self.image_2)
        self.album_2.pictures.add(self.image_1)

    def test_photo_exists(self):
        self.assertIsInstance(self.image_1, Photo)

    def test_photo_title(self):
        self.assertEqual(self.image_1.title, 'image 1')

    def test_photo_description(self):
        self.assertEqual(self.image_1.description, 'nature')

    def test_photo_date_uploaded(self):
        self.assertIsNotNone(self.image_1.date_uploaded)

    def test_photo_in_album(self):
        self.assertIn(self.image_2, self.album_1.pictures.all())

    def test_photo_not_in_album(self):
        self.assertNotIn(self.image_3, self.album_1.pictures.all())

    def test_photo_delete(self):
        self.image_1.delete()
        self.assertNotIn(self.image_1, self.album_1.pictures.all())

    def test_user_has_photo(self):
        self.assertEqual(self.user, self.image_1.user)

    def test_user_does_not_own_photo(self):
        self.assertNotEqual(self.user_2, self.image_1.user)

    def test_user_has_album(self):
        self.assertEqual(self.user, self.album_1.user)

    def test_user_does_not_own_album(self):
        self.assertNotEqual(self.user_2, self.album_1.user)

    def test_album_exists(self):
        self.assertIsInstance(self.album_1, Album)

    def test_album_title(self):
        self.assertEqual(self.album_1.title, 'Album')

    def test_album_description(self):
        self.assertEqual(self.album_1.description, 'I haz photoz')

    def test_album_date_uploaded(self):
        self.assertIsNotNone(self.album_1.date_uploaded)

    def test_album_has_multiple_photos(self):
        self.assertEqual(len(self.album_1.pictures.all()), 2)
