from django.contrib import admin
from django.urls import path,include
from django.db import router
from rest_framework import routers
from app.urls import router as app_router

router  =   routers.DefaultRouter()
router.registry.extend(app_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include("app.urls")),

]
