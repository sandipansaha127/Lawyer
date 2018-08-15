from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from accounts.forms import SignUpForm
from django.db import transaction
import re

from django.conf import settings
from lawyer.forms import LawyerForm,CategoryForm

from lawyer.views import lawyer_list


@login_required
def Bari(request):
    return render(request, 'index.html')

    #
    #
    #
    # return redirect('lawyer_list')


def signup(request):
    context = {
        'category_form':CategoryForm(),
        'lawyer_form': LawyerForm(),
    }
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            if request.user.profile.role == "LAWYER":
                return render(request, 'registration/lawyer_registration.html', context)
            return HttpResponseRedirect('lawyer_list')
            #redirect('lawyer_list')
            #return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, ('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, ('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
