from django.urls import path
from .views import (
    LivroReadAPIView, LivroCreateAPIView,
    LivroUpdateAPIView, LivroDestroyAPIView
)


urlpatterns = [
    path("livros/", LivroReadAPIView.as_view(), name="livro-list"),
    path("livros/<int:pk>/", LivroReadAPIView.as_view(), name="livro-retrieve"),

    path("livros/create/", LivroCreateAPIView.as_view(), name="livro-create"),
    path("livros/update/<int:pk>/", LivroUpdateAPIView.as_view(), name="livro-update"),
    path("livros/delete/<int:pk>/", LivroDestroyAPIView.as_view(), name="livro-delete")
]