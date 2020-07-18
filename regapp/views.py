from django.shortcuts import render
from django.http import HttpResponseRedirect
from regapp.models import Student
from regapp.forms import StudentForm
from django.shortcuts import redirect
# Create your views here.
def form_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'start/home.html',{'form':form})