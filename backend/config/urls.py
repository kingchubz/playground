from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tinypng.urls'), name='tinypng'),
    # path('admin/', admin.site.urls),
]

