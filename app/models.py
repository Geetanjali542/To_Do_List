from django.db import models

# Create your models here.
class Addtask(models.Model):
  addtask = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_completed = models.BooleanField(default=False)

  def __str__(self):
          return self.addtask
  