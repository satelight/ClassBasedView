from django.urls import path
from .views import (
    BookCreateView, BookDetailView, IndexView,HomeView,BookListView,UpdateBookView,BookDeleteView,BookFormView
)# from django.views.generic.base import TemplateView #静的なHTMLに使用

app_name = 'store'

urlpatterns = [
    path('index',IndexView.as_view(),name='index'),
    # path('home/',TemplateView.as_view(template_name='home.html'),name='home')
    path('home/<name>',HomeView.as_view(),name='home'),
    path('detail_book/<int:pk>',BookDetailView.as_view(),name='detail_book'),
    path('list_books/',BookListView.as_view(),name='list_books'),
    path('list_books/<name>', BookListView.as_view(), name='list_books'),
    path('add_book/',BookCreateView.as_view(),name='add_book'),
    path('edit_book/<int:pk>',UpdateBookView.as_view(),name='edit_book'),
    path('delete_book/<int:pk>',BookDeleteView.as_view(),name='delete_book'),
    path('book_form/',BookFormView.as_view(),name='book_form'),
]
