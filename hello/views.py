from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from .models import Greeting, User

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

class SearchView(ListView):
    model = User
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = User.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result
