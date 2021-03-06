from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class ActiveProfileManger(models.Manager):
    """Return a query set of the active users."""
    def get_queryset(self):
        qs = super(ActiveProfileManger, self).get_queryset()
        return qs.filter(user__is_active__exact=True)

PHOTOGRAPHY_TYPES = [
    ('portrait', 'Portrait'),
    ('landscape', 'Landscape'),
    ('nature', 'Nature'),
    ('family', 'Family'),
    ('travel', 'Travel'),
    ('art', 'Art'),
    ('food', 'Food'),
]

US_REGIONS = [
    ('pnw', 'Pacific Northwest'),
    ('wc', 'West Coast'),
    ('sw', 'South West'),
    ('mw', "Midwest"),
    ('s', "Southern U.S."),
    ('ec', "East Coast"),
    ('ne', "New England"),
    ('ak', "Alaska"),
    ('h', "Hawaii"),
    ('t', "U.S. Territory"),
]


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Create a user profile model (to be attached on creation)"""
    camera = models.TextField(default='')
    photography_type = models.CharField(max_length=30,
                                        choices=PHOTOGRAPHY_TYPES,)
    region = models.CharField(max_length=30, choices=US_REGIONS)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile'
    )

    """Friends, below, will be profile objects"""
    friends = models.ManyToManyField("self", symmetrical=False,
                                     related_name='friend_of')

    objects = models.Manager()
    active = ActiveProfileManger()

    @property
    def is_active(self):
        return self.user.is_active

    def __str__(self):
        return self.user.username
