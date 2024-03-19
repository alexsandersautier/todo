from django.db import models

class Task(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    completed = models.BooleanField()
    
    def __str__(self):
        return f'{self.description}'