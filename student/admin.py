from django.contrib import admin

# Register your models here.
from student.models import Account, Del_Account

admin.site.register(Account)
admin.site.register(Del_Account)