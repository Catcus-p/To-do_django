from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')   # columnsshown
    list_filter = ('completed',)                  # filtersidebar
    search_fields = ('title',)                    # searchbar
    list_editable = ('completed',)                # editdirectly
    ordering = ('-id',)                           # latestfirst


admin.site.register(Task, TaskAdmin)
# Register your models here.
