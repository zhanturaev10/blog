from django.urls import path
from .views import HomeView, PostView, PostCreateView, PostUpdateView, PostDeleteView, about, search

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about.html', about, name='about'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('search.html', search, name='search'),
]
