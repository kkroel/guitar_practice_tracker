from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import NewSongForm, StudentSongForm


def index(request):
    return render(request, 'student/index.html')


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def new_song(request):
    if request.POST:
        pass
    else:
        form = NewSongForm()
        u_form = StudentSongForm()
        context = {'form': form,
                   'u_form': u_form}
        return render(request, 'student/new_song.html', context)
