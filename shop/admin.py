from ast import Dict
from typing import Sequence
from django.contrib import admin
from django.forms import SlugField
from.models import *
# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,catadmin)

class prodAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img','available']
    list_editable=['price','stock','img','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(products,prodAdmin)    