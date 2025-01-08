from django.db import models


class Topic(models.Model):
    '''Topic studied by the user.'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    '''User-researched information on the topic.'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_created=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
