from django.shortcuts import render

# Create your views here.

def jinja(request):
    d = {'name' : 'udaykiran', 'age' : 22, 'course' : 'django', 'FE' : True, 'BE' : True}
    return render(request, 'jinja_operational.html', d)
