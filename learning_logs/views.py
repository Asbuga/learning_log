from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """The home page of the Learning Log app."""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Lists all user topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    content = {'topics': topics}
    return render(request, 'learning_logs/topics.html', content)


def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404

@login_required
def topic(request, topic_id):
    """List the Entry by Topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    
    if request.method == 'POST':
        topic.delete()
        return redirect('learning_logs:topics')
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Defines a new topic."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
        
    # Returns empty form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Adds a new entry in topics."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edits exist entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    elif 'delete' in request.POST:
        entry.delete()
        return redirect('learning_logs:topic', topic_id=topic.id)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
