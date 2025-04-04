from django.contrib import admin

from main.models import About, Contact, Image, Project, Skill

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Image)
