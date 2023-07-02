from django.shortcuts import render


def home(request):
    return render(request,
                  'main/home.html')


def portraits_view(request):
    return render(request,
                  'main/portraits.html')

