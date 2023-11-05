from django.contrib import admin
from .models import ProfileModel
from .models import ProfileDetails

# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(ProfileDetails)

