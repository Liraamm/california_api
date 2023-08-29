from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, CategoryViewSet

router = DefaultRouter()
router.register('product', ProductsViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]