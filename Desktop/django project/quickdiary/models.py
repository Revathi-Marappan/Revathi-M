from django.db import models

# Create your models here.

class MoodTracker(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('neutral', 'Neutral'),
        ('excited', 'Excited'),
        ('angry', 'Angry'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    mood = models.CharField(max_length=10,
choices=MOOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
    