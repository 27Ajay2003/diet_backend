from django.urls import path
from .views import RecipeAPIView

urlpatterns = [
    path('view/', RecipeAPIView.as_view(), name='recipe-list'),
]