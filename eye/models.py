from django.db import models
import uuid
# Create your models here.
class Events(models.Model):
    CONSUMER1 = 'www.consumeraffairs.com'
    CONSUMER2 = "www.consumeraffairs2.com"
    CONSUMER3 = "www.consumeraffairs3.com"

    Applications = [
        (CONSUMER1, 'www.consumeraffairs.com'),
        (CONSUMER2, 'www.consumeraffairs2.com'),
        (CONSUMER3, 'www.consumeraffairs3.com'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    session_id = models.UUIDField(null=False)
    category = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    host = models.CharField(
        max_length=35,
        choices=Applications,
    )
    path = models.CharField(max_length=100)
    element = models.CharField(max_length=50,blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=False)
