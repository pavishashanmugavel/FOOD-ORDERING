from django.contrib import admin
from .models import Order
from .models import Feedback

admin.site.register(Order)
admin.site.register(Feedback)
