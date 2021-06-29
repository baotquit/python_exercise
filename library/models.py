from __future__ import unicode_literals

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

AVAILABLE = 0
BORROWED = 1
STATUS_CHOICES = (
    (AVAILABLE, 'Available'),
    (BORROWED, 'Borrowed'),
)


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)


class Category(models.Model):
    """The model to control the category of the book"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    categories = models.ManyToManyField(Category, related_name='categories')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    quantity = models.PositiveSmallIntegerField()
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        related_name="books",
    )

    def __str__(self):
        return self.name


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    first_name = None
    last_name = None
    full_name = models.CharField(_('fullname'), max_length=250, blank=True)
    address = models.CharField(_('address'), max_length=500, blank=True)

    def __str__(self):
        return self.username
