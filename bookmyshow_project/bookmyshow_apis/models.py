from django.db import models
import uuid

# Create your models here.
class Cinemas_table(models.Model):
    movie_name = models.TextField()
    theatre_name = models.TextField()
    theatre_timings = models.TextField()
    theatre_show_timing_total_seats = models.IntegerField()
    theatre_show_timings_current_seats = models.IntegerField()
    theatre_city = models.TextField()
    ticket_uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)


class users_table(models.Model):
    username = models.TextField()
    password = models.TextField()
    user_ticket_uuid_list = models.JSONField()
