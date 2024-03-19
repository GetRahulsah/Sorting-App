# sorting_project/sorting_app/models.py
from django.db import models

class SortingResult(models.Model):
    # Your model fields go here
    unsorted_data = models.CharField(max_length=255)
    sorted_data = models.CharField(max_length=255)
    sorting_algorithm = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sorting_algorithm} - {self.timestamp}"
