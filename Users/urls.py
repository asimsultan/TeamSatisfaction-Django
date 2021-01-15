# Importing Libraries
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Users',views.UsersView)

urlpatterns = [
    path('', include(router.urls)),
    path('user-detail/<str:pk>/', views.userDetail, name="user-detail"),
]