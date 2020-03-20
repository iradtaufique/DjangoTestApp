from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django_tables2 import SingleTableView

from singupApp.forms import SignUpForm, CreateNewUser, CreateAdditionInfo
from singupApp.models import Personal
from singupApp.table import PersonalTable


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'singupApp.html', {'form': form})


class CreatePersonal(CreateView):
    model = Personal
    fields = '__all__'
    template_name = 'home.html'

    def form_valid(self, form):
        form.is_valid()
        form.save()
        return redirect('signup')


class PersonalListView(SingleTableView):
    model = Personal
    table_class = PersonalTable
    template_name = 'simple_table.html'


def newUser(request):
    form = CreateNewUser
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
        return redirect('additionInfo')
    return render(request, 'additionInfo/new_user.html', {'form': form})


def additioInformation(request):
    form2 = CreateAdditionInfo(request.POST)
    if request.method == 'POST':
        if form2.is_valid():
            form2.save()
        return redirect('login')
    return render(request, 'additionInfo/addition_info.html', {'form2': form2})
