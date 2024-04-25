from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    guest_amount = models.SmallIntegerField(validators = [MaxValueValidator(6)])
    booking_time = models.DateTimeField()
    
    def __str__(self):
        return self.name + " - " + str(self.booking_time)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.SmallIntegerField(validators = [MaxValueValidator(5)])

    def __str__(self):
        return self.title
