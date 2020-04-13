from django.contrib import admin
from .models import Sign_verification_forged
from .models import Sign_verification_genuine

# Register your models here.
admin.site.register(Sign_verification_forged)
admin.site.register(Sign_verification_genuine)
