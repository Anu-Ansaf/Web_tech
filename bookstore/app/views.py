from django.shortcuts import render
from django.http import HttpResponse
from django import http
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
import datetime
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
from app.models import CustomUser
import re
# Create your views here.

def root(req):
    # return HttpResponse({"hello ansaf":1})
    # return render(req,'index.html')
    print(req.method)
    if req.method == "GET":
        res = render(req,'main.html')
        # res.set_cookie('my_cookie', '250000')
        # res.set_cookie('my_cookie',
        #                 value='cookie_value',
        #                  # Expires in 1 hour
        #                 expires=datetime.datetime.utcnow() + datetime.timedelta(days=9),  # Expires in 7 days
        #                 path='/ooansafdfg',
        #                 domain="127.0.0.1",
        #                 secure=True,
        #                 httponly=True,samesite='strict')
        return res
        # csrfContext = RequestContext(req)
        # return render(req,'mai.html')
    # if req.method == 'POST':
        # print(req.session.get("my_cookie"))
        # return HttpResponse(req)
def test(req):
    # print(req.session.get("my_cookie"))
    print(req.COOKIES)
    print(req)
    print("Request Method:", req.method)

    # Print request headers
    print("Request Headers:", req.headers)

    # Print GET parameters
    print("GET Parameters:", req.GET)

    # Print POST parameters
    print("POST Parameters:", req.POST)

    # Print cookies
    print("Cookies:", req.COOKIES)
    print("User:", req.user)
    # Print user information (if authenticated)
    if req.user.is_authenticated:
        print("User:", req.user)

    # ... Add more information as needed

    # Return a response
    return HttpResponse("req inspection complete")
    return HttpResponse(req)
def login_func(req):
    if req.method == "GET":
        # print(req.csrf_token)
        print(get_token(req))
        
        return render(req,'login.html')
    if req.method == "POST":
        print("User:", req.user)
        email = req.POST["email"]
        password = req.POST["password"]
        # all_users = CustomUser.objects.all()
        all_name = CustomUser.objects.values_list('username', flat=True)
        all_phone = CustomUser.objects.values_list('phone', flat=True)
        # user = authenticate(request=req,username = name,password=password)
        # all_name = CustomUser.objects.values_list('username', flat=True)
        user = authenticate(request=req,email=email,password=password)
        if user:
            login(req,user)
            return HttpResponse(all_phone)
            # print(user)
        else:
            return HttpResponse("Not Authenticated")

        # return HttpResponse(get_token(req))
        return HttpResponse(all_emails)
def validationcheck(email,phonenumber,password,repassword):
    if password !=repassword:
        return HttpResponse("Password Not Match")
    
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not(re.fullmatch(email_regex, email)):
        return HttpResponse("Email not in Correct Format")
    
    phone_regex = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
    match = re.search(phone_regex, phonenumber)
    if not(match):
        return HttpResponse("Phone Number is not Correct")
    else:
        return True
    

def signup(req):
    if req.method=="GET":
        return render(req,'signup.html')
    if req.method == "POST":
        # print(get_token(req))
        name = req.POST["name"]
        email = req.POST["email"]
        phonenumber = req.POST["phonenumber"]
        password = req.POST["password"]
        repassword = req.POST["repassword"]
        check_res = validationcheck(email=email,phonenumber=phonenumber,password=password,repassword=repassword)
        print(check_res)
        if check_res:
            pass
        else:    
            return HttpResponse("Error")
        # user = CustomUser.objects.create_user(username=name, email=email, password=password,phone=phonenumber)
        user = CustomUser.objects.create_user(username=name, email=email,phone=phonenumber,password=password)
        # user.first_name = 'John'
        # user.last_name = 'Doe'
        user.save()
        return HttpResponse("Success")