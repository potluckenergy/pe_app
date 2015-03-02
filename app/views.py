from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


def home(request):
    d = TemplateData()

    """
        login modal
    """
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect("/dashboard")
            else:
                # Show an error page
                return HttpResponseRedirect("/login")

    t = get_template('home.html')
    c = RequestContext(request, d.getData())    
    return HttpResponse(t.render(c))


def app(request):
    if not request.user.is_authenticated():
        print 'not'
        return HttpResponseRedirect('/login')
    d = TemplateData()
    t = get_template('app.html')
    c = RequestContext(request, d.getData())    
    return HttpResponse(t.render(c))


"""
    auth
"""
def login(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect("/dashboard")
            else:
                # Show an error page
                return HttpResponseRedirect("/login")

    t = get_template('login.html')
    c = RequestContext(request, {})  
    return HttpResponse(t.render(c))

def logout(request):
    auth.logout(request)
    t = get_template('logout.html')
    c = RequestContext(request, {})    
    return HttpResponse(t.render(c))



"""
    Static pages 
"""

def about(request):
    t = get_template('about.html')
    c = RequestContext(request, {})    
    return HttpResponse(t.render(c))

def benefitreport(request):
    t = get_template('benefitreport.html')
    c = RequestContext(request, {})    
    return HttpResponse(t.render(c))

def legal(request):
    t = get_template('legal.html')
    c = RequestContext(request, {})    
    return HttpResponse(t.render(c))




"""
    Helpers
"""

class TemplateData:
    def __init__(self):
        self.d = {}
    def addData(self, key, entry):
        self.d[key] = entry
    def getData(self):
        return self.d