from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'), 
    path('signup/', views.signup, name='signup'), 
    path('buynow/', views.buynow, name='buynow'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('admin/', admin.site.urls),
    path('buynow', views.product_list, name='product_list'),
    path('favorites/', views.favorite_products, name='favorites'), 
    path('save_to_favorites/<int:product_id>/', views.save_to_favorites, name='save_to_favorites'),
    path('past_orders/', views.past_orders, name='past_orders'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('add_address/', views.add_address, name='add_address'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
