
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.root,name='root'),
    path('login',views.login_func,name='login'),
    path('signup',views.signup,name='signup'),
    path('test',views.test,name='test'),
    path('payment',views.payment,name='payment'),
    path('thank-you',views.payment_success,name='success'),
    path("admin_panel",views.admin_panel,name='admin_panel')

]