from django.shortcuts import render, redirect
from .models import Tourist
from .forms import Touristform
from django.contrib import messages



# Create your views here.
def home(request):
    all_Tourists = Tourist.objects.all
    return render(request, 'home.html', {'all' :all_Tourists})

def join(request):
    if request.method == "POST":
        form = Touristform(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Yeyyy...Submission Success! '))
        #return render(request, 'home.html', {})
        return redirect('home')

    else: 
        return render(request, 'join.html', {})
