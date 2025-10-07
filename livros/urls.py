from django.urls import path
from .views import LivroListCreateAPIView, LivroDetail


urlpatterns = [
    path("livros/", LivroListCreateAPIView.as_view(), name="livro-list-create"),
    path("livros/<int:pk>/", LivroDetail.as_view(), name="livro_detail")
]