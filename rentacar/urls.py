"""rentacar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [



    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('reservation/', include('reservation.urls')),
    path('user/', include('user.urls')),
    path('hakkimizda', views.hakkimizda, name="hakkimizda"),
    path('referanslarimiz', views.referanslarimiz, name="referanslarimiz"),
    path('iletisim', views.iletisim, name="iletisim"),
    path('car/', include('car.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_cars, name='category_cars'),
    path('car/<int:id>/<slug:slug>/', views.car_detail, name='car_detail'),
    path('content/<int:id>/<slug:slug>/', views.content_detail, name='content_detail'),
    path('search/', views.car_search, name='car_search'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('faq/', views.faq, name='faq'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
