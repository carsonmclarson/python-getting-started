from django.urls import path

from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search'),
    path('', HomePageView.as_view(), name='home'),
]
