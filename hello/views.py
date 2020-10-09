from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from .models import Greeting, User

# Create your views here.
'''def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")'''

class HomePageView(TemplateView):
    template_name = 'index.html'

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

class SearchResultsView(ListView):
    model = User
    template_name = 'search.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = User.objects.filter(
            Q(username__icontains=query) | Q(email__icontains=query)
        )
        return object_list


