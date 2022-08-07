from django.db import models

# Create your models here.

class Customer(models.Model):
    Ravi_Network = 'R'
    Guru_Network = 'G'
    Appu_Network = 'A'
    RESPONSIBLE_PEOPLE = [
        (Ravi_Network,'Ravi'),
        (Guru_Network,'Guru'),
        (Appu_Network,'Appu'),
    ]
    name = models.CharField(max_length=255)
    address = models.TextField()
    number = models.CharField(max_length = 255)
    payment_status = models.BooleanField()
    last_payment_date = models.DateTimeField(auto_now_add = True)
    incharge = models.CharField(max_length=1,choices=RESPONSIBLE_PEOPLE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-id']

class Box(models.Model):
    box_no = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE,null = True)

    def __str__(self) -> str:
        return self.box_no
    
    class Meta:
        ordering = ['-customer__id']

class Channels(models.Model):
    channel_name = models.CharField(max_length = 255)
    channel_price = models.DecimalField(max_digits=6,decimal_places=2)  
    customer = models.ManyToManyField(Customer)
    class Meta:
        ordering = ['id']



