import datetime
from django.db import models


REALIZED = 'REALIZED'
STARTED = 'STARTED BUT NOT REALIZED YET'
NOT_STARTED = 'NOT STARTED YET'

STATUS = [
    (REALIZED, 'Already completed'),
    (STARTED, 'Started, but not finished yet'),
    (NOT_STARTED, 'Not started yet'),
]

LOW = 'LOW'
MEDIUM = 'MEDIUM'
HIGH = 'HIGH'

PRIORITY = [
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
    (HIGH, 'High'),
]

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    category = models.ManyToManyField(Category)
    priority = models.CharField(
        max_length=32,
        choices=PRIORITY,
        default=MEDIUM
    )
    details = models.CharField(
        max_length=1000,
        blank=True
    )
    date = models.DateTimeField(
        default=datetime.datetime.now(),
        blank=True
    )
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default=NOT_STARTED
    )


