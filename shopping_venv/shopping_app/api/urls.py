# from django.urls import path, include
# from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'cart-items', views.CartItemView)

# urlpatterns = [
#     path('',include(router.urls)),
#     path('api-auth/', include('rest_framework.urls'))
# ]
from django.urls import path
from .views import CartItemView

urlpatterns = [
    path('cart-items/', CartItemView.as_view()),
    path('cart-items/<int:id>', CartItemView.as_view())
]