from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('list/',views.BookList.as_view(),name='booklist'),
    path('details/<int:pk>',views.BookDetails.as_view(),name='details'),
    path('about/',views.AboutUs.as_view(),name='about'),
    path('create/',views.BookCreateView.as_view(),name='bookcreate'),
    path('contact/',views.ContactView.as_view(),name='contact')
    #path('about2/',TemplateView.as_view(template_name='about.html')),
]