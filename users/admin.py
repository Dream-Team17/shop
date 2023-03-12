from django.contrib import admin
from users.models import User
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['email', 'username', 'number', 'created_at']

admin.site.register(User)