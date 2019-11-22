from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = routers.SimpleRouter()
router.register('cards', views.CardView)
router.register('users', views.UserView)
router.register('cardspurchased', views.CardPurchasedView)
router.register('transactions', views.TransactionView)



urlpatterns = [

    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
