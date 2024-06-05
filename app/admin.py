from django.contrib import admin

from app.models import Addtask

# Register your models here.

class Display(admin.ModelAdmin):
  dis_list = ['addtask', 'updated_at', 'created_at']
  search_fields = ('dis_list',)


admin.site.register(Addtask, Display)