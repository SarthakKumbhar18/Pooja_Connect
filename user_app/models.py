from django.db import models

# Create your models here.
class User_table(models.Model):
    User_Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30,)
    Email_Id = models.EmailField(default="")
    Username = models.CharField(max_length=30,)
    Password = models.CharField(max_length=30,)

    def __str__(self):
        return self.Name
    
    class Meta:
        db_table = "User Table"
