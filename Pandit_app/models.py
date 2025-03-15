from django.db import models

# Create your models here.

class Pandit(models.Model):
    Pandit_Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=60)
    Age = models.IntegerField()
    Area = models.CharField(max_length=60)
    Work_Experience = models.IntegerField()
    Image = models.ImageField(upload_to="pandit_images/",default="")
    Email_Id = models.EmailField(default="")
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Name
     
    class Meta:
        db_table = "Pandit"

    