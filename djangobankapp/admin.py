
from django.contrib import admin
from . models import Country,City,Person,Gender,Account

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Gender)
admin.site.register(Account)


