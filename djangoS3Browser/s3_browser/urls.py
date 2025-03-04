"""s3_browser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import path, re_path
from django.conf.urls.static import static

from djangoS3Browser.s3_browser import settings
from djangoS3Browser.s3_browser import views

urlpatterns = [
                  re_path('get_folder_items/(?P<main_folder>.+)/(?P<sort_a_z>.+)/', views.get_folder_items, name='get_folder_items'),
                  path('upload/', views.upload, name='upload'),
                  path('create_folder/', views.create_folder, name='create_folder'),
                  path('download/', views.download, name='download'),
                  path('rename_file/', views.rename_file, name='rename_file'),
                  path('paste_file/', views.paste_file, name='paste_file'),
                  path('move_file/', views.move_file, name='move_file'),
                  path('delete_file/', views.delete_file, name='delete_file'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
