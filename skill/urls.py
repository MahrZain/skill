from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("save/", views.saveuserdata, name="save"),
    path("reset/", views.reset, name="reset"),
    path("delete/<slug:slug>", views.delete, name="delete"),
    path("edit/<slug:slug>", views.edit, name="edit"),
]
