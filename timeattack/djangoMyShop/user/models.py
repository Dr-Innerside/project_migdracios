from django.db import models

# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table='my_user'