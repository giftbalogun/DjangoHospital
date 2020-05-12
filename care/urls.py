"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from django.views.generic import TemplateView
from care.views import SendBookingEmail, SendContactEmail
from care.views import index, about, search, blog_list, blog_detail, contact

from emailing.views import subscribe
from emailing.views import email_list_signup

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('search/', search, name='search'),
    path('blog', blog_list, name='blog'),
    path('blog/<id>/', blog_detail, name='blog-details'),
    path('contact/', contact, name='contact'),
    path('book/', SendBookingEmail.as_view(), name='book'),
    path('mailme/', SendContactEmail.as_view(), name='mailme'),
    path('subcribe/', email_list_signup, name='emailing'),
    path('subcribes/', subscribe, name='emailings'),
]
