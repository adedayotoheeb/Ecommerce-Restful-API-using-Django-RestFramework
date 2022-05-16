from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collection', views.CollectionViewSet)
router.register('cart', views.CartViewSet)

prouduct_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product_pk')

prouduct_router.register('reviews', views.ReviewViewSet,
                         basename='products-reviews')

cart_router = routers.NestedDefaultRouter(router, 'cart', lookup='cart_pk')

cart_router.register('items', views.CartItemViewset, basename='cart-items')


urlpatterns = router.urls + prouduct_router.urls + cart_router.urls
