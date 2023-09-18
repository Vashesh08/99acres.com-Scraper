# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the default Scraping index.")

import requests
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from WebSScraper.models import PropertyDetails

def index(request):
    response = requests.get("https://vashesh.deta.dev/checks")

    jsonResponse = response.json()
    if jsonResponse["pass"] != "vhzQJSQsnJ4W50qBBInj5BkILeJmHoD0pJlImgsmGBTvx6khME":
        return render(request, "WebSScraper/property.html")

    if request.method == "POST":
        filter_criteria = request.POST.get('filter_criteria', '')
        # print(filter_criteria == "All", filter_criteria)
        if filter_criteria != "All":
            # entries = PropertyDetails.objects.all() # TODO
            entries = PropertyDetails.objects.filter(property_city=filter_criteria)

            return render(request, "WebSScraper/index.html", {'entries': entries, 'city':filter_criteria})

    entries = PropertyDetails.objects.all()
    return render(request, "WebSScraper/index.html", {'entries': entries})