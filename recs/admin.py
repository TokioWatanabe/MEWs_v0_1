from django.contrib import admin
from . models import (Section1_1, Section1_2, Section1_3,)

MyModels = (Section1_1, Section1_2, Section1_3,)
# Register your models here.
admin.site.register( MyModels )