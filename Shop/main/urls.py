from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view())


]
from django.urls import path
from .views import home, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
]


from django.urls import path
from .views import create_order

urlpatterns = [
    path('order/', create_order, name='create_order'),
]


from django.urls import path
from .views import add_to_cart,cart_detail

urlpatterns = [
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
path('cart/', cart_detail, name='cart_detail'),
]

