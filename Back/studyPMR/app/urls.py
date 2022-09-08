from django.db import router
from django.urls import path
from rest_framework import routers
from .views import *
from .views import RegistrationView, LoginView, LogoutView,ChangePasswordView
from rest_framework_simplejwt import views as jwt_views



urlpatterns =   [

    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='register'),
    path('change-password', ChangePasswordView.as_view(), name='register'),    
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

router      =   routers.DefaultRouter()

router.register('bailleur', BailleurViewSet)
router.register('pmr', PmrViewSet)
router.register('logement', LogementViewSet)
router.register('candidature', CandidatureViewSet)

