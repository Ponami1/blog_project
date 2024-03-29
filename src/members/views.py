from django.shortcuts import render, redirect
from .forms import RegisterForm,  ProfileChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib import messages
#email imports
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.core.mail import EmailMessage  

# Create your views here.
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")
    return redirect('login')

def activateEmail(request, user, to_email):
  mail_subject = "Activate your User"
  message = render_to_string("template_activate.html", {
    "user":user.username,
    "domain": get_current_site(request).domain,
    "uid":urlsafe_base64_encode(force_bytes(user.pk)),
    "token":account_activation_token.make_token(user),
    "protocol":'https' if request.is_secure() else 'http'
  })
  
  
  email = EmailMessage(mail_subject, message, to=[to_email])
  if email.send():
    messages.success(request, f'Dear {user}, please go to your email {to_email} inbox and click on the activation link to cinfirm and complete the registration')
  else:
    messages.error("problem sending email to {to_email} check if you typed it correctly")
  
def Register(request):
  form= RegisterForm()
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_active = False
      user.save()
      activateEmail(request, user, form.cleaned_data.get("email"))
      return redirect('login')
    else:
      for error in list(form.errors.values()):
          messages.error(request, error)
  else:
    form = RegisterForm()
  return render(request, 'registration/register.html', {"form":form})

def PasswordChange(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      return redirect('home')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'registration/change-password.html', {"form":form})
      


def Profile(request):
  form = ProfileChangeForm(instance=request.user)
  if request.method == "POST":
    form = ProfileChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      form = ProfileChangeForm()
  return render(request, 'Profile.html', {"form": form})


