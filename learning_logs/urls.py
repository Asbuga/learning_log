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
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for add new Topic.
    path('new-topic/', views.new_topic, name='new_topic'),

    # Page for add new Entry.
    path('new-entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
