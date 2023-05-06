from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# creating a validator function
phone_regex = RegexValidator(regex=r'^[0-9]{10}$', message="enter valid number")

def validate_geeks_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("enter valid email format")


class Employee(models.Model):
    emp_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    firstname = models.CharField(max_length=50,blank=True, null=True) 
    lastname = models.CharField(max_length=50, blank=True, null=True) 
    email = models.EmailField( max_length=50, validators =[validate_geeks_mail], unique=True, blank=True, null=True)
    lan1 = models.CharField(max_length=50, blank=True, null=True) 
    lan2 = models.CharField(max_length=50, blank=True, null=True)         
    dist = models.CharField(max_length=50, blank=True, null=True) 
    state = models.CharField(max_length=50, blank=True, null=True) 
    country = models.CharField(max_length=50, blank=True, null=True) 
    blood_group = models.CharField(max_length=50, blank=True, null=True) 
    phone_no = models.CharField(validators=[phone_regex],max_length=10, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True) 
    marital_status = models.CharField(max_length=50, blank=True, null=True) 
    department = models.CharField(max_length=50,blank=True, null=True)
    grade_level = models.CharField(max_length=50, blank=True, null=True)
