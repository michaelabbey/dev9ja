from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Registration(models.Model):
    email = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.CharField(max_length=150, blank=True, null=True)
    sex = models.CharField(max_length=150, blank=True, null=True)
    i_am_registering_for = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    does_your_child_have_any_experience_coding = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'registration'
        managed = True
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'