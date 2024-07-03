from django.contrib import admin
from .models import Member


# Register your models here.
class MemberAmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'phone', 'joined_date')
admin.site.register(Member,MemberAmin)