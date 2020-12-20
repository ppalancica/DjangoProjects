"""notepad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from notes.views import (
    note_list_view,
    finish_item,
    delete_item,
    recover_item
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', note_list_view, name='note-list'),
    path('finish-item/<id>/', finish_item, name='finish-note-item'),
    path('recover-item/<id>/', recover_item, name='recover-note-item'),
    path('delete-item/<id>/', delete_item, name='delete-note-item')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
