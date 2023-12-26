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
from .models import Book, Purchase
from django.contrib.auth.decorators import login_required
from .models import Purchase
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.
# user_books = {'anu':{'book':[2],'price':[156.99]},
#               "ansaf":{'book':[1],'price':[86.99]},
#               "joel":{'book':[6],'price':[26.99]},
#               "praveen":{'book':[12],'price':[216.99]},
#               "david":{'book':[5],'price':[60.99]},
#               "niman":{'book':[9],'price':[496.99]}}
user_books = {'anu':{'book':[2],'price':[156.99]},
              "ansaf":{'book':[1],'price':[86.99]},
              "joel":{'book':[6],'price':[26.99]},
              "praveen":{'book':[12],'price':[216.99]}}

def root(req):
    # return HttpResponse({"hello ansaf":1})
    # return render(req,'index.html')
    print(req.method)
    if req.method == "GET":
        if req.user.is_authenticated:
            # return HttpResponse(str(req.user.username)+str(req.user.email)+str(req.user.phone))
            name = req.user.username
            data = {"name":req.user.username}
            return render(req,"dashboard.html",context=data)
        print(req.user)
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
            # return HttpResponse(out)
            # return render(req,"dashboard.html")
            return redirect('root')
            # print(user)
        else:
            out = login(req,user)
            print(out)
            return HttpResponse("Not Authenticated")

        # return HttpResponse(get_token(req))
        return HttpResponse(all_emails)
def validationcheck(email,phonenumber,password,repassword):
    if password !=repassword:
        return HttpResponse("Password Not Match")
    try:
        validate_password(password=password)
        print("Validated")
    except :

        return False
    
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
            return HttpResponse("Password Must be Strong")
        # user = CustomUser.objects.create_user(username=name, email=email, password=password,phone=phonenumber)
        user = CustomUser.objects.create_user(username=name, email=email,phone=phonenumber,password=password)
        # user.first_name = 'John'
        # user.last_name = 'Doe'
        user.save()
        return render(req,'login.html')

def payment(req):
    if req.user.is_authenticated and req.method == "POST":
        # print(req.POST)
        # book_instance = Book.objects.get(id=1)

        # # Assuming you have a User instance (you can use get_user_model() to get the User model)
        # user_instance = get_user_model().objects.get(id=1)

        # # Create a Purchase instance
        # purchase_instance = Purchase.objects.create(user=user_instance, book=book_instance)

        # # Save the instance to the database
        # purchase_instance.save()
        # # purchase = Purchase.objects.create(user=req.user, book='dsads')
        # print(purchase_instance)
        # file = open('data','r')
        # file_data = file.read()
        # file_data =eval(file_data)
        # print(file_data)
        # file.close()
        # file = open('data','w+')
        # try:
        #     list_of_books = file_data[req.user.username]["book"]
        #     file_data[req.user.username]["book"]=list_of_books.append(req.POST["book"])

        #     list_of_price = file_data[req.user.username]["price"]
        #     file_data[req.user.username]["price"]=list_of_price.append(req.POST["price"])
        # except:
        #     # list_of_books = file_data[req.user.username]["book"]
        #     file_data[req.user.username]["book"]=list_of_books.append(req.POST["book"])

        #     # list_of_price = file_data[req.user.username]["price"]
        #     file_data[req.user.username]["price"]=list_of_price.append(req.POST["price"])
        # file.write(str(file_data))
        # file.close()
        price = req.POST["price"]
        book = req.POST["book"]
        print(book,price)
        list_of_books = list(user_books[req.user.username]['book'])
        list_of_books.append(book)
        user_books[req.user.username]['book']=list_of_books

        list_of_price = list(user_books[req.user.username]['price'])
        list_of_price.append(price)
        user_books[req.user.username]['price']=list_of_price
        print(user_books)


        

    # return HttpResponse(req.POST['book'])
        return render(req,'payment.html')
    
    elif req.user.is_authenticated and req.method == "GET":
        return HttpResponse("GET Operation is not possible")
    else:
        return render('main.html',context={'error':True})
def payment_success(req):
    if req.user.is_authenticated and req.method == "GET":
        # purchased_books = Purchase.objects.filter(purchase__user=req.user)
        # print(purchased_books)

        # return HttpResponse("Success")
        return render(req,'success.html')
    else:
        print(req)
def admin_panel(req):
    if req.method=="POST":
        superuser = authenticate(req, username=req.POST['email'], password=req.POST["password"])
        if superuser:
            login(req,superuser)

            users = CustomUser.objects.all()
            return render(req,"admin.html",{'users': users,"data":user_books})
        else:
            return render(req,"auth_failed.html")
        # books = user_books[users.user.username]['book']
        # price = user_books[users.user.username]['price']
            return render(req,"admin.html",{'users': users})
    elif req.method=="GET":
        return render(req,'admin_login.html')