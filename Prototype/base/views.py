from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import UseForm


def register(request):
    if request.method == 'POST':
        form = UseForm(request.POST)
        if form.is_valid():
            group = Group.objects.get(id=request.POST['group'])
            user = form.save()
            group.user_set.add(user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UseForm()
    content = {'form': form,
               'groups': Group.objects.all()}
    return render(request, 'base/register.html', content)
