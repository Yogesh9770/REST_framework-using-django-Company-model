from django.db import models

# Create your models here.
# company models

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=50)
    company_about = models.TextField()
    company_types = models.CharField(max_length=50, choices=(
                                                            ('IT','IT'),
                                                            ('NON IT','NON IT'),
                                                            ('Mechanical','Mechanical'))
                                                            )
    added_date = models.DateTimeField(auto_now=True)
    company_active =  models.BooleanField(default=True)


# Employee Models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_first_name = models.CharField(max_length=30)
    employee_last_name = models.CharField(max_length=30)
    employee_email = models.EmailField(unique=True)
    employee_phone = models.CharField(max_length=20)
    employee_position = models.CharField(max_length=50, choices=(('software dev','software dev'),
                                                                 ('manager','manager'),
                                                                 ('junior associate','junior associate')
                                                                 ))
    employee_gender = models.CharField(max_length=6,choices=(('Male', 'Male'), ('Female', 'Female')))
    employee_date_of_birth = models.DateField()
    employee_address = models.CharField(max_length=150)
    employee_city = models.CharField(max_length=30)
    employee_country = models.CharField(max_length=30)
    employee_postal_code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name + " " + self.last_name