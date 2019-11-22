from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin

from .models import User, Card, CardPurchased, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'business')


class CardPurchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardPurchased
        fields = ('id', 'business')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'business')