"""
URL configuration for python222_site_pc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.views.static import serve

import helloWorld.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', helloWorld.views.index, name='index'),
    # 配置媒体文件的路由地址
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    path('blog/<int:id>', helloWorld.views.bolg),
    path('blog2/<int:year>/<int:month>/<int:day>/<int:id>', helloWorld.views.blog2),
    re_path('blog3/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})', helloWorld.views.blog3),
    # 路由重定向
    path("redirectTo", RedirectView.as_view(url='index/')),
    # 命名空间namespace
    path('user/', include('user.urls', 'user')),
    path('order/', include('order.urls', 'order')),
    path('download1', helloWorld.views.download_file1),
    path('download2', helloWorld.views.download_file2),
    path('download3', helloWorld.views.download_file3),
    path('get', helloWorld.views.get_test),
    path('post', helloWorld.views.post_test),
    path('tologin/', helloWorld.views.to_login),
    path('login', helloWorld.views.login),
    path('toUpload/', helloWorld.views.to_upload),
    path('upload', helloWorld.views.upload),
    path('student/list/', helloWorld.views.List.as_view()),
    path('student/<int:pk>/', helloWorld.views.Detail.as_view()),
    path('student/create', helloWorld.views.Create.as_view()),
    path('student/update/<int:pk>', helloWorld.views.Update.as_view()),
    path('student/delete/<int:pk>', helloWorld.views.Delete.as_view()),
]
