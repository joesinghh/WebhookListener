from django.db import models
from django.utils import timezone
# from django_hstore import hstore
# from django_mysql.models import JSONField
# from django_jsonfield_backport.models import JSONField



class RequestDataJson(models.Model):

    date = models.DateTimeField(default=timezone.now)
    data = models.JSONField()

    def __str__(self):
        return f"{self.date}"

class RequestDataText(models.Model):
    date = models.DateTimeField(default=timezone.now)
    data = models.TextField(default=None,)

    def __str__(self):
        return "{}".format(self.date)

# Create your models here
