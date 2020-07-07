from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
    # added in part 8
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    path("borrowed/", views.LoanedBooksAllListView.as_view(), name="all-borrowed"),
    # Added for challenge part 8
    # views.LoanedBooksAllListView.as_view() directs to LoanedBooksAllListView() in views.py
    path(
        "book/<uuid:pk>/renew/", views.renew_book_librarian, name="renew-book-librarian"
    ),
    # added in part 9
    # directs to renew_book_librarian() in views.py
]

urlpatterns += [
    path("author/create/", views.AuthorCreate.as_view(), name="author_create"),
    path("author/<int:pk>/update/", views.AuthorUpdate.as_view(), name="author_update"),
    path("author/<int:pk>/delete/", views.AuthorDelete.as_view(), name="author_delete"),
    path("books/create/", views.BookCreate.as_view(), name="book_create"),
    path("books/<int:pk>/update", views.BookUpdate.as_view(), name="book_update"),
    path("books/<int:pk>/delete", views.BookDelete.as_view(), name="book_delete"),
]
