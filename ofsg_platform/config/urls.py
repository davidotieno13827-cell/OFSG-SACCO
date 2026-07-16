from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path('', lambda request: redirect('/members/')),
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
