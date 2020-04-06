
from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/bookmark/', views.BookmarkDetailView.as_view(), name='bookmark-detail'),
]