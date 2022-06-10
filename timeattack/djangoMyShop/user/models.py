from django.db import models

# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table='my_user'
    def __str__(self):
        return self.email
    email = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=256, null=False)