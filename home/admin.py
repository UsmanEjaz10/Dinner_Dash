from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.register(Issue)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(OrderItem)
