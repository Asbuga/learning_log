from django.shortcuts import render

from .models import Topic


def index(request):
    """The home page of the Learning Log app."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Lists all user topics."""
    topics = Topic.objects.order_by('date_added')
    content = {'topics': topics}
    return render(request, 'learning_logs/topics.html', content)


def topic(request, topic_id):
    """List the Entry by Topic."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
