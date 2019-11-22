import time
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, phone):
        if not email:
            raise ValueError("ENTER AN EMAIL BUDDY")
        if not password:
            raise ValueError("PASSWORD?!?!?!? HELLO??")
        if not phone:
            raise ValueError("PHONE?!?!?!? HELLO??")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, phone):
        user = self.create_user(email, password, phone)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first = models.CharField(max_length=100, null=True, blank=True)
    last = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(unique=True, max_length=100)
    stripe_number = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=30)
    approved_seller = models.BooleanField(default=False)
    business_name = models.CharField(max_length=100, null=True, blank=True)
    business_address = models.CharField(max_length=100, null=True, blank=True)
    business_city = models.CharField(max_length=100, null=True, blank=True)
    business_state = models.CharField(max_length=100, null=True, blank=True)
    business_zip = models.CharField(max_length=50, null=True, blank=True)
    business_phone = models.CharField(max_length=30, null=True, blank=True)
    fein = models.CharField(max_length=20, null=True, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]

    objects = UserManager()


class Card(models.Model):
    business = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True)
    balance = models.FloatField(default=0)

    card_image = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=150, null=True)
    address2 = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    state = models.CharField(max_length=150, null=True)
    zip = models.CharField(max_length=150, null=True)


class CardPurchased(models.Model):
    card_id = models.CharField(max_length=10)
    buyer = models.CharField(max_length=20)
    seller = models.CharField(max_length=20)
    amount = models.FloatField()
    time_purchased = models.IntegerField(default=int(time.time()))
    redeemed = models.BooleanField(default=False)
    redeemed_date = models.CharField(max_length=15)


class Transaction(models.Model):
    buyer = models.CharField(max_length=20)
    seller = models.CharField(max_length=20)
    amount = models.FloatField()
    time_purchased = models.IntegerField(default=int(time.time()))
    associated_transaction = models.IntegerField()
    card_purchased = models.CharField(max_length=10)

