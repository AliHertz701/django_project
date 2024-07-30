"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import index, product, edit, register,shop_view,edit_p
from rest_framework.routers import DefaultRouter
from app.views import ProductViewSet,userViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'users', userViewSet)


urlpatterns = [  
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('register/', register, name='register'),
    path('edit/<int:id>', edit, name='edit'),
    path("accounts/", include("django.contrib.auth.urls")),
    # path('login/', user_login, name='login'),
    path('', include(router.urls)),

    path('shop/', shop_view, name='shop'),
    path('edit_p/<int:id>',edit_p,name='edit_p')
    
     
]
