from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import BookListApiView,  \
    BookDetailApiView, BookCreateApiView, BookUpdateApiView, \
    BookDeleteApiView, BookListCreateApiView, BookDetailUpdateDeleteApiView, \
    BookViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')


urlpatterns = [
    # path('books/', book_list_view),
    # path('books/', BookListApiView.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('booklistcreate/', BookListCreateApiView.as_view()),
    # path('bookdetailupdatedelete/<int:pk>/', BookDetailUpdateDeleteApiView.as_view()),
    # # CRUD
    # path('books/create/', BookCreateApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),

]

urlpatterns = urlpatterns + router.urls