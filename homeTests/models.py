from django.db import models
from datetime import datetime

choice = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]

class questions(models.Model):
    title:str = models.CharField(max_length=90, blank=False, unique=True)
    created_at:int = models.DateField(default=datetime.now)
    resposta:str = models.CharField(max_length=1,choices=choice ,unique=True, default='A')

