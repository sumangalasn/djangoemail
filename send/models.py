from django.db import models
# Create your models here.
class sentmail(models.Model):
  sent_email = models.CharField(max_length=200,
    primary_key=True)

  subject = models.TextField(max_length=100)

  text = models.CharField(max_length=40)

  from_email = models.CharField(max_length=30)

  class Meta:
    db_table = 'send'




