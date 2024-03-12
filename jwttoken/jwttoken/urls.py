from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from app.views import *


router = DefaultRouter()
router.register('personapi', ModelViewSetview, basename='person')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('authen/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', TokenObtainPairView.as_view(), name='gettokenview'),
    path('refreshview/', TokenRefreshView.as_view(), name='tokenrefresh'),
    path('tokenverify/', TokenVerifyView.as_view(), name='tokenverify'),

]
