from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter(trailing_slash=False)
router.register("user", views.UserViewSet, basename="user")
router.register("menu", views.MenuViewSet, basename="menu")
router.register("booking", views.BookingViewSet, basename="booking")


urlpatterns = [
    path("", include(router.urls)),
    path("", views.index, name="index"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
