from django.urls import path
from . import views
urlpatterns=[
    path('list/',views.booklist,name='booklist'),
]