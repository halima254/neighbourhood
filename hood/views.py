from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import SignupForm,PostForm,UpdateProfileForm,NeighbourHoodForm,BusinessForm
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Post,Profile,Business
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def community(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'comm.html', params)