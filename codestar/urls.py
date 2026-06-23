from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("about/", include("about.urls"), name="about-urls"),
    path("", include("blog.urls"), name="blog-urls"),
]