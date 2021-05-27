from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bpp_app.models import MarketingPoints, Heading

# Create your views here.
def test_view(request):
    return HttpResponse("Yay it works")

def landing_page(request):
    headings = Heading.objects.all()
    context_dict = {"headings": []}
    for heading in headings:
        new_heading_dict = {"heading": heading}
        the_items = MarketingPoints.objects.filter(heading=heading)
        new_heading_dict["marketing_points"] = the_items
        context_dict["headings"].append(new_heading_dict)
    return render(request, "bpp_app/landing.html", context=context_dict)

