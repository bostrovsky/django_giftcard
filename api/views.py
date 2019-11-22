from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.views import View
from .models import Card, User, CardPurchased, Transaction
from .serializer import UserSerializer, CardSerializer, CardPurchasedSerializer, TransactionSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CardView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardPurchasedView(viewsets.ModelViewSet):
    queryset = CardPurchased.objects.all()
    serializer_class = CardPurchasedSerializer


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
