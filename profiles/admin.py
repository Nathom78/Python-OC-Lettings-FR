from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Profile


admin.site.register(Profile)

# unregister the Group model from admin.
# admin.site.unregister(Group)
