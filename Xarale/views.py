from django.shortcuts import get_object_or_404, render

def home(request):
    return render(request, 'xarale/index.html')


# contact views

def about(request):
    return render(request, 'about.html')



 