from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True)
    phone = models.CharField(max_length=100,blank=True)
    rut=models.CharField(max_length=100,blank=True)
    is_company = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Related(models.Model):
    owner=models.ForeignKey(Contact, on_delete=models.CASCADE,related_name='related')
    contacts=models.ManyToManyField(Contact,related_name='contacts')
    def __str__(self):
        return self.owner.name

class Address(models.Model):
    contact=models.ForeignKey(Contact, on_delete=models.CASCADE,related_name='address')
    street=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    is_invoice = models.BooleanField(default=False)
    is_shipping = models.BooleanField(default=False)
    def __str__(self):
        return self.contact.name