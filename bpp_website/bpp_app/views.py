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
        new_heading_dict = {"heading": heading.heading, "slug": heading.slug}
        the_items = MarketingPoints.objects.filter(heading=heading)
        the_item_list = []
        for item in the_items:
            item_dict = {}
            item_dict["item"] = item
            the_paragraphs = item.text.split("\n")
            item_dict["paragraphs"] = the_paragraphs
            the_item_list.append(item_dict)
        new_heading_dict["marketing_points"] = the_item_list
        context_dict["headings"].append(new_heading_dict)
        print(context_dict)
    return render(request, "bpp_app/base.html", context=context_dict)

