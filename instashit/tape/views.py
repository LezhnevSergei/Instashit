from django.shortcuts import render
from django.views.generic import View
from django.views.decorators import csrf
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import LoginForm, UserRegistrationForm


# Create your views here.
class TapeView(View):
    
    def get(self, request):
        posts = Post.objects.order_by('-pub_date')

        return render(request, 'tape/tape.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})        