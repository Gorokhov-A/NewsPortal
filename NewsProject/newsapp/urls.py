from django.contrib import admin
from django.urls import path
from .views import PostsList, PostDetail, index  # импортируем наше представление


urlpatterns = [
    # path — означает путь.
    path('index', index),
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(),)
]