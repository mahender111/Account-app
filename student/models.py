from django.db import models

# Create your models here.
class Account(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,primary_key=True)
    salary = models.IntegerField(default =True)
    age = models.DateTimeField()
    addarcard = models.ImageField(upload_to="image/")
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')


    def __str__(self):
        return self.name


    def database(self):
        if self.status=="draft":
            return True
        return False


    def datasalary(self):
        sum=0
        if self.salary < 34000:
            return True
        return False


    def data_sal(self):
        if self.salary >= 100000:
            return False
        return True


class Del_Account(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,primary_key=True)
    salary = models.IntegerField(default =True)
    age = models.DateTimeField()
    addarcard = models.ImageField(upload_to="image/")
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    def __str__(self):
        return self.name





