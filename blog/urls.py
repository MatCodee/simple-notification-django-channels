from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.PostListView.as_view()),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]