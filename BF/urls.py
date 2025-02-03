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
    path('', views.product_list, name='product_list'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
