"""Define URL schemes for learning_logs."""

from django.urls import path

from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('index/', views.index, name='index'),

    # Page with all themes.
    path("topics/", views.topics, name='topics'),

    # Topic content page.
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
