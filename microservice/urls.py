from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from olympians.views import CompanyListView, CompanyDetailView

urlpatterns = [  
    # re_path(r'^.*', CompanyListView.as_view()),
    path('', CompanyListView.as_view()),
    path('detail/<pk>/', CompanyDetailView.as_view(), name='detail'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)