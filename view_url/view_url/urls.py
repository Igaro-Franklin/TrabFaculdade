from django.contrib import admin
from django.urls import path

from home.views import minha_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/', minha_view),
]
