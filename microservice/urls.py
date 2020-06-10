from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from rest_framework import routers
from olympians.views import CompanyListView, CompanyDetailView
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='OLYMPIANS')

urlpatterns = [     
    url(r'^$', schema_view), 
    path('api/', CompanyListView.as_view(), name='listview'),    
    path('detail/<pk>/', CompanyDetailView.as_view(), name='detail'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 