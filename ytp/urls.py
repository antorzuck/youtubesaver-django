from django.contrib import admin
from django.urls import path
from ytd.views import home, download, downloaded

urlpatterns = [
    path('', home),
    path('download', download, name="download"),
    path('done/<resolution>', downloaded, name='downloaded')
]
