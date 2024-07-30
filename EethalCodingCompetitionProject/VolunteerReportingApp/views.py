from django.shortcuts import render
from django.http import HttpResponse
from .forms import TutorialDropDownForm
#Create your views here.
def index(request):
    return HttpResponse("hi this is my first app")

def tutorial_view(request):
    if request.method == 'POST':
        form = TutorialDropDownForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['choice_field'])
    else:
        form = TutorialDropDownForm()
    return render(request, 'tutorial.html', {'form': form})