from django.contrib import admin
from django.urls import path
from blog.views import chiclete, jujuba

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chiclete/', chiclete),
    path('jujuba/', jujuba),
]