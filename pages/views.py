from django.shortcuts import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello World!')