from django.db import models

# Create your models here.
class UserModel(models.Model):
#     def __init__(self, username, password):
#         self.username = models.CharField(max_length=20, null=False)
#         self.password = models.CharField(max_length=256, null=False)

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
