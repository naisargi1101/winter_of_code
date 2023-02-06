from . tokens import generate_token
from django.utils.http import urlsafe_base64_encode
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from winter_of_code import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage,send_mail
from django.utils.http import urlsafe_base64_decode

# Create your views here.
def home(request):
    return render(request,'login/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username alreasy exists! Please try different account")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already Exists")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request,"Username must be less than 10 characters")

        if pass1!= pass2:
            messages.error(request,"Passwords didn't match")
        
        if not username.isalnum():
            messages.error(request,"Username must be Alpha-numeric")
            return redirect('home')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()

        # messages.success(request,"Your Account Has Been Created Successfully. We have sent you a confirmation email.")
        # # welcome Email
        # subject = "welcome to Winter of code!!"
        # message = "Hello" + myuser.first_name + "Welcome to winter of code. This email is confirmation Email. Your Email Id is successfully registered with Winter of code. Thank you. "
        # from_email = settings.EMAIL_HOST_USER
        # to_list = {myuser.email}
        # send_mail(subject,message,from_email,to_list,fail_silently=True)

        # #Email Address Confirmation Email
        # current_site = get_current_site(request)
        # email_subject = "Confirm your email with winter of code"
        # message2 = render_to_string('email_confirmation.html',{
        #     'name':myuser.first_name,
        #     'domain':current_site.domain,
        #     'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })

        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()
        return redirect('signin')

    return render(request,'login/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username= username,password = pass1)
        if user:
            login(request,user)
            fname = user.first_name
            return redirect('homeUser',user.id)
        else:
            messages.error(request,"Wrong username or password")
            return redirect('home')
    return render(request,'login/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"You are Signed Out")
    return redirect("home")

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    
    if myuser and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        login(request,myuser)
        return redirect('home')
    else:
        return render(request,'activation_failed.html')