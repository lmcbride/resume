from django.contrib import admin
from resume_app.models import Person, Skills, Category, Projects, Experience

admin.site.register(Person)
admin.site.register(Skills)
admin.site.register(Category)
admin.site.register(Projects)
admin.site.register(Experience)