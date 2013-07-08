from django.http import HttpResponse
from annoying.decorators import render_to
from django.http import HttpResponseRedirect
from resume_app.models import *

@render_to('test.html')
def test(request):
    return{}
    
@render_to('index.html')
def home(request):
    category_skill_list = {}
    for category in Category.objects.all():
        category_skill_list[category] = Skills.objects.filter(category=category)
      
    return {'person_list':Person.objects.all(),
           'skill_list':Skills.objects.all(),
           'category_list':Category.objects.all(),
           'category_skill_list':category_skill_list,
           'project_list':Projects.objects.all(),
           'experience_list':Experience.objects.all()}

