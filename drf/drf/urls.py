from django.contrib import admin
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from drf.views import index_view, about_view
from utils.constants import Urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name=Urls.INDEX_REVERSE.value),
    path("about/", about_view, name=Urls.ABOUT_REVERSE.value),
] + debug_toolbar_urls()
