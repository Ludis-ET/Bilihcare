from django.shortcuts import render,redirect
from repair.models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    User = request.user
    brand = Brand.objects.all()
    amount = Price.objects.all()
    if User.is_authenticated:
        pp = Profile.objects.get(user=User.id)
    else:
        pp = ""
    if request.method == 'POST':
        try:
            if 'no' in request.POST:
                a=request.POST['name']
                b=request.POST['email']
                c=request.POST['phone']
                d=request.POST['country']
                e=request.POST['city']
                f=request.POST['device']
                g=request.POST['model']
                h=request.POST['problem']
                i=request.POST['other']
                model=Order.objects.create(
                    name=a,
                    email=b,
                    device=f,
                    model=g,
                    problems=h,
                    others=i,
                    phone=c,
                    country=d,
                    city=e,
                    my_place=False,
                )
                if not User.is_authenticated:
                    messages.add_message(request, messages.INFO, 'Your order Placed succesfully Login with your account to become customer')
                else:
                    messages.add_message(request, messages.INFO, 'Your order Placed succesfully')
                return redirect('repair:amharic')
            if 'yes' in request.POST:
                a=request.POST['name']
                b=request.POST['email']
                c=request.POST['phone']
                d=request.POST['country']
                e=request.POST['city']
                f=request.POST['device']
                g=request.POST['model']
                h=request.POST['problem']
                i=request.POST['other']
                model=Order.objects.create(
                    name=a,
                    email=b,
                    device=f,
                    model=g,
                    problems=h,
                    others=i,
                    phone=c,
                    country=d,
                    city=e,
                    my_place=True,
                )
                if not User.is_authenticated:
                    messages.add_message(request, messages.INFO, 'Your order Placed succesfully Login with your account to become customer')
                else:
                    messages.add_message(request, messages.INFO, 'Your order Placed succesfully')
                return redirect('repair:amharic')
            if 'apply' in request.POST:
                a = request.POST['name']
                b= request.POST['email']
                c = request.POST['phone']
                d = request.FILES['file']
                main = Apply.objects.create(
                    name=a,
                    email=b,
                    file=d,
                    phone=c,
                )
                if not User.is_authenticated:
                    messages.add_message(request, messages.INFO, 'Your personal data submitted successfully stay tuned Login with your account to become customer')
                else:
                    messages.add_message(request, messages.INFO, 'Your personal data submitted successfully stay tuned')
                return redirect('repair:amharic')
        except:pass
    web = Webpack.objects.get(id=1)
    context = {
        'User':User,
        'web': web,
        'pp':pp,
        'brand':brand,
        'amount':amount,
    }
    return render(request,"a-index.html",context)

def about(request):
    web = Webpack.objects.get(id=1)
    ab = About.objects.all()
    User = request.user
    if User.is_authenticated:
        pp = Profile.objects.get(user=User.id)
    else:
        pp = ""
    context = {
        'web':web,
        'ab':ab,
        'User':User,
        'pp':pp
    }
    return render(request,"a-about.html",context)


def faq(request):
    web = Webpack.objects.get(id=1)
    ab = Faq.objects.all()
    User = request.user
    if User.is_authenticated:
        pp = Profile.objects.get(user=User.id)
    else:
        pp = ""
    context = {
        'web':web,
        'ab':ab,
        'User':User,
        'pp':pp,
    }
    return render(request,"a-faq.html",context)

def googleadsense(request):
    return HttpResponse('google.com, pub-6510615875274346, DIRECT, f08c47fec0942fa0')