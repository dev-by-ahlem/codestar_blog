from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('accounts/', include('allauth.urls')),   # ⭐ ADD THIS
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls')),
]
