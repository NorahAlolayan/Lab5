from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books_index"),
    path('list_books/', views.list_books, name="books_list_books"),
    path('<int:bookId>/', views.viewbook, name="books_view_one_book"),
    path('aboutus/', views.aboutus, name="books_aboutus"),
    path('html5/links/', views.links),
    path('html5/text/formatting/', views.formatting),
    path('html5/listing/', views.listing),
    path('html5/tables/', views.tables),
    path('search', views.search, name='search'),
]
