from django.contrib import admin

from .models import Project, Todo

class TodoInline(admin.TabularInline):
  model = Todo
  extra = 3

class ProjectAdmin(admin.ModelAdmin):
  inlines = [TodoInline]

admin.site.register(Project, ProjectAdmin)
# admin.site.register(Project)