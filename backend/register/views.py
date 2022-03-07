from django.shortcuts import render, redirect

from .forms import RegisterUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            print('******')
            form.save()
        else:
            print(form.errors)
        return redirect("login")
    else:
        form = RegisterUserForm()

    return render(request, 'register/register.html', {"form": form})