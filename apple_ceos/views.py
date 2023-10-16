from django.shortcuts import render

# Create your views here.

from .models import CEO

def index(request):
    """View function for home page of site."""

    num_ceos = CEO.objects.all().count
    ceos = CEO.objects.all()

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_ceos': num_ceos, 'ceos': ceos},
    )