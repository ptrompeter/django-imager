# Create your tests here.
from __future__ import unicode_literals
from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
import factory

from imager_profile.models import ImagerProfile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(
            username='bob',
            email='bob@dobalina.com',
        )
        self.user.set_password('secret')

    # def tearDown(self):
    #     User.objects.filter(username='bob').all().delete()

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

