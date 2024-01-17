from django.contrib import admin
from .models import *


# Register your models here.
@admin.register( 
User,
Image,
Video,
Verifications
    )

class AppAdmin(admin.ModelAdmin):
    pass