from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bpp_app.models import MarketingPoints

# Create your views here.
def test_view(request):
    return HttpResponse("Yay it works")

def landing_page(request):
    marketing_messages = MarketingPoints.objects.all()
    context_dict = {"messages": marketing_messages}
    for message in marketing_messages:
        print(message.text)
    return render(request, "bpp_app/landing.html", context=context_dict)

