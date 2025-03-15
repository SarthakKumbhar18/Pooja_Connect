from django.db import models
from Pandit_app.models import *
from user_app.models import *
# Create your models here.

class Appointment_Table(models.Model):
    User_ID = models.ForeignKey(User_table, on_delete=models.CASCADE)
    Pandit_Id = models.ForeignKey(Pandit, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Phone_no = models.CharField(max_length=15)
    Date = models.DateField()
    Work = models.CharField(max_length=50)
    Status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Declined', 'Declined')],
        default='Pending'
    )

    def __str__(self):
        return f""" {self.Name} + {self.Work}""" 
    
    class Meta:
        db_table = "Appointment"
        
