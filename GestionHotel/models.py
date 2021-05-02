from django.db import models
from model_utils.fields import MonitorField
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneField(blank=True, help_text='numero de telephone')
    email_employee = models.EmailField(blank=True, null=True)



class Client(models.Model):
    """Discription of the Client models."""
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    ID = (
        ('PS', 'Passport'),
        ('IC', 'Identity Card'),
    )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    sex = models.CharField(max_length=1, choices=SEX)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    phone_number = PhoneField(blank=True, help_text='numero de telephone') #par pip instal phonefield
    email_client = models.EmailField(blank=True, null=True)
    identificator_type = models.CharField(max_length=2, choices=ID)
    id_number = models.CharField(max_length=10, unique=True)

    # Metadata
    class Meta:
        ordering = ['last_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return '%s %s'%(self.first_name, self.last_name)


class ChamberType(models.Model):
    type_name = models.CharField(max_length=60)
    type_price = models.DecimalField(max_digits=6, decimal_places=2)

    # Metadata
    class Meta:
        ordering = ['type_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.type_name



class Chamber(models.Model):
    chamber_number = models.IntegerField()
    chamber_type = models.ForeignKey(ChamberType, on_delete=models.CASCADE)
    chamber_stage = models.IntegerField()
    chamber_phone = PhoneField(blank=True, help_text='numero de telephone de la chambre')
    chamber_reserved = models.BooleanField(null=True, default=False)
    chamber_cleaned = models.BooleanField(null=True, default=True)

    # Metadata
    class Meta:
        ordering = ['chamber_stage','chamber_number']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.chamber_number


class Reservation(models.Model):
    """A typical class defining a reservation model."""

    # Fields
    id_reservation = models.BigAutoField(primary_key=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    chambre_id = models.ForeignKey(Chamber, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['-end_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id_reservation)])
    @property
    def days(self):
        return (self.end_date - self.start_date).days

    def __str__(self):
        return self.id_reservation


class Invoice(models.Model):
    """ Model Representing Invoice itself"""
    NEW = 'nw'
    SENT = 'sent'
    RETURNED = 'retu'
    PAID = 'paid'
    CREDIT = 'cred'
    INCOLECTIBLE = 'inco'
    BANK_TRANSFER = 'BqTr'
    CASH = 'cash'
    CASH_ON_DELIVERY = 'COD'
    PAYMENT_CARD = 'pycd'
    PERSONAL_PICKUP = 'pick'
    MAILING = 'emal'
    DIGITAL = 'dig'

    STATUS = [
        (NEW,'new'),
        (SENT,'sent'),
        (RETURNED,'returned'),
        (PAID,'paid'),
        (CREDIT,'credited'),
        (INCOLECTIBLE,'uncollectible'),
        ]
    PAYMENT_METHOD = [
      (BANK_TRANSFER,'bank transfer'),
      (CASH,'cash'),
      (CASH_ON_DELIVERY,'cash on delivery'),
      (PAYMENT_CARD,'payment card'),
    ]
    DELIVERY_METHOD = [
      (PERSONAL_PICKUP,'personal pick up'),
      (MAILING,'mailing'),
      (DIGITAL,'digital'),
    ]
    invoice_number =  models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=4, choices=STATUS, default=NEW)
    reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    note = models.CharField(max_length=60, blank=True, default='Thank you for using our services' )
    date_due = models.DateField(help_text='date de payment')
    date_sent = MonitorField(monitor='status',when=[SENT],verbose_name="date d'envoi",blank=True, default=None)
    date_paid = MonitorField(monitor='status',when=[PAID],verbose_name="date de paiement",blank=True, default=None)
    payment_method = models.CharField(max_length=4, choices=DELIVERY_METHOD)

    # Metadata
    class Meta:
        ordering=['status']

    # Methods
    def __str__(self):
        return invoice_number

class OnlineRequest(models.Model):
    date_request = models.DateField(auto_now=True,blank= False,null=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = PhoneField(blank=False, help_text='numero de telephone') #par pip instal phonefield
    email_client = models.EmailField(blank=True, null=True)
    ChamberType_id = models.ForeignKey(ChamberType, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    request_confirmed = models.BooleanField(null=True, default=False)

    # Methods
    def __str__(self):
        return (self.client_id)
