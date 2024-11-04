from django.db import models


class Topic(models.Model):
    """The topic the user is researching."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_created=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Information learned by the user."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_created=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Returns a string representation of the model."""
        return f"{self.text[:50]}..."
