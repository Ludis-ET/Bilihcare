from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import *


def index(request):
    User = request.user
    brand = Brand.objects.all()
    amount = Price.objects.all()
    new = New.objects.all()
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
                return redirect('repair:index')
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
                return redirect('repair:index')
            if 'apply' in request.POST:
                a = request.POST['name']
                b= request.POST['email']
                c = request.POST['phone']
                d = request.FILES['file']
                e = request.POST['more']
                main = Apply.objects.create(
                    name=a,
                    email=b,
                    file=d,
                    phone=c,
                    more=e
                )
                if not User.is_authenticated:
                    messages.add_message(request, messages.INFO, 'Your personal data submitted successfully stay tuned Login with your account to become customer')
                else:
                    messages.add_message(request, messages.INFO, 'Your personal data submitted successfully stay tuned')
                return redirect('repair:index')
        except:pass
    web = Webpack.objects.get(id=1)
    context = {
        'User':User,
        'web': web,
        'pp':pp,
        'brand':brand,
        'amount':amount,
    }
    return render(request,"index.html",context)


def about(request):
    new = New.objects.all()
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
        'pp':pp,
        'new':new
    }
    return render(request,"about.html",context)


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
    return render(request,"faq.html",context)


def login_user(request):
    web = Webpack.objects.get(id=1)
    micon = ""
    mtitle = ""
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'],) 
            if user is not None:
                login(request,user)
                if Profile.objects.filter(user=request.user):
                    micon = "success"
                    mtitle = "success"
                    messages.add_message(request, messages.INFO, 'Logged in Successfully now you can edit your personal information')
                    return redirect('repair:profile')
                else:
                    micon = "success"
                    mtitle = "success"
                    messages.add_message(request, messages.INFO, 'Logged in Successfully now you can add other personal information')
                    return redirect('repair:register2')
        else:
            micon = "error"
            mtitle = "error"
            messages.add_message(request, messages.INFO, 'Invalid user data entered')
    context = {
        'web':web,
        'mtitle':mtitle,
        'micon':micon,
    }
    return render(request,"login.html",context)


def terms(request):
    web = Webpack.objects.get(id=1)
    User = request.user
    context = {
        'web':web,
        'User':User,
    }
    return render(request,"terms.html",context)


def blog(request):
    web = Webpack.objects.get(id=1)
    User = request.user
    post = Post.objects.all()
    category = Category.objects.all()
    one = Post.objects.filter(level='one')
    two = Post.objects.filter(level='two')
    three = Post.objects.filter(level='three')
    four = Post.objects.filter(level='four')
    five = Post.objects.filter(level='five')
    context = {
        'web':web,
        'User':User,
        'post':post,
        'category':category,
        'one':one,
        'two':two,
        'three':three,
        'four':four,
        'five':five,
    }
    return render(request,'blog.html',context)


def category(request,id):
    category = Category.objects.get(id=id)
    web = Webpack.objects.get(id=1)
    User = request.user
    post = Post.objects.all()
    categor = Category.objects.all()
    main = Post.objects.filter(category=id)
    context = {
        'category':category,
        'web':web,
        'User':User,
        'post':post,
        'categor':categor,
        'main':main,
    }
    return render(request,'category.html',context)


def post(request,id):
    postt = Post.objects.get(id=id)
    web = Webpack.objects.get(id=1)
    User = request.user
    post = Post.objects.all()
    categor = Category.objects.all()
    context = {
        'category':category,
        'web':web,
        'User':User,
        'post':post,
        'postt':postt,
        'categor':categor,
    }
    return render(request,'post.html',context)


@login_required(login_url='login')
def profile(request):
    web = Webpack.objects.get(id=1)
    User = request.user
    micon = ""
    mtitle = ""
    history = Order.objects.filter(user=User.id)
    pp = Profile.objects.get(user=User.id)
    if request.method == 'POST':
        try:
            a = request.POST['one']
            b = request.POST['two']
            c = request.POST['three']
            d = request.POST['four']
            e = request.POST['five']
            f = request.POST['six']
            g = request.POST['seven']
            if e:
                if e == f:
                    User.set_password(e)
                    User.save()
                    micon = "success"
                    mtitle = "success"
                    messages.add_message(request, messages.INFO, 'Password Updated successfully')
                    return redirect('repair:login')
                else:
                    micon = "error"
                    mtitle = "error"
                    messages.add_message(request, messages.INFO, 'Passwords donot match please try again')
                
            User.username=c
            User.first_name=a
            User.last_name=b
            User.email=d
            User.save()
            pp.phone=g
            pp.save()
            micon = "success"
            mtitle = "success"
            messages.add_message(request, messages.INFO, 'Profile Updated successfully')      
            if request.FILES['eight']:
                h = request.FILES['eight']
                pp.profile_pic = h
                pp.save()
                micon = "success"
                mtitle = "success"
                messages.add_message(request, messages.INFO, 'Profile picture Updated successfully')  
            
        except:pass
    context = {
        'web':web,
        'User':User,
        'micon':micon,
        'mtitle':mtitle,
        'pp':pp,
        'history':history,
    }
    return render(request,'profile.html',context)



@login_required(login_url='login')
def admin_page(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    cc = Apply.objects.all().count()
    a = Order.objects.all().count()
    p = Profile.objects.all().count()
    pp = Profile.objects.get(user=User.id)
    aa = Profile.objects.filter(is_manager=True).count()
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'cc':cc,
        'a':a,
        'pp':pp,
        'p':p,
        'aa':aa,
    }
    return render(request,'admin-page/index.html',context)


@login_required(login_url='login')
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("repair:index")


@login_required(login_url='login')
def about_edit(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    ab = About.objects.all()
    pp = Profile.objects.get(user=User.id)
    if request.method == 'POST':
        try:
            if 'add' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                c = request.POST['three']
                d = request.POST['four']
                e = request.POST['five']
                About.objects.create(title=a,p1=b,p2=c,p3=d,p4=e)
                messages.add_message(request, messages.INFO, 'New About added successfully')
                return redirect('repair:about_edit')
            if 'edit' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                c = request.POST['three']
                d = request.POST['four']
                e = request.POST['five']
                f = request.POST['six']
                g = About.objects.get(id=f)
                g.title = a
                g.p1 = b
                g.p2 = c
                g.p3 = d
                g.p4 = e
                g.save()
                messages.add_message(request, messages.INFO, 'Existing About updated successfully')
                return redirect('repair:about_edit')
            if 'delete' in request.POST:
                f = request.POST['six']
                a = About.objects.get(id=f)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected Item Deleted successfully')
                return redirect('repair:about_edit')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'ab':ab,
        'pp':pp,
    }
    return render(request,"admin-page/about-edit.html",context)



@login_required(login_url='login')
def sup_edit(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    sb = Faq.objects.all()
    pp = Profile.objects.get(user=User.id)
    if request.method == 'POST':
        try:
            if 'add' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                Faq.objects.create(question=a,answer=b,)
                messages.add_message(request, messages.INFO, 'New FAQ added successfully')
                return redirect('repair:faq_edit')
            if 'edit' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                c = request.POST['three']
                g = Faq.objects.get(id=c)
                g.question = a
                g.answer = b
                g.save()
                messages.add_message(request, messages.INFO, 'Existing FAQ updated successfully')
                return redirect('repair:faq_edit')
            if 'delete' in request.POST:
                f = request.POST['three']
                a = Faq.objects.get(id=f)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected Item Deleted successfully')
                return redirect('repair:faq_edit')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'sb':sb,
        'pp':pp,
    }
    return render(request,"admin-page/sup-edit.html",context)
    

@login_required(login_url='login')
def user_edit(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    sb = Profile.objects.all().exclude(user=User.id)
    pp = Profile.objects.get(user=User.id)
    if request.method == 'POST':
        try:
            if 'edit' in request.POST:
                c = request.POST['three']
                g = Profile.objects.get(id=c)
                if g.is_manager == True:
                    g.is_manager = False
                else:
                    g.is_manager = True
                g.save()
                messages.add_message(request, messages.INFO, 'Existing User updated successfully')
                return redirect('repair:user_edit')
            if 'delete' in request.POST:
                f = request.POST['three']
                a = Profile.objects.get(id=f)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected User Deleted successfully')
                return redirect('repair:user_edit')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'sb':sb,
        'pp':pp,
    }
    return render(request,"admin-page/user-edit.html",context)
  

@login_required(login_url='login')
def book(request):
    a = Order.objects.all().count()
    b = Order.objects.all()
    User = request.user
    web = Webpack.objects.get(id=1)
    pp = Profile.objects.get(user=User.id)
    if request.method == "POST":
        try:
           a = request.POST['one']
           b = Order.objects.get(id=a)
           b.approved = True
           b.save()
           messages.add_message(request, messages.INFO, " order approved successfully.")
           return redirect('repair:book')
        except:pass
    prob = Model.objects.all()
    context = {
        "a":a,
        'prob':prob,
        'b':b,
        'web':web,
        'User':User,
        'pp':pp,
    }
    return render(request,'admin-page/book.html',context)


@login_required(login_url='login')
def com(request):
    a = Apply.objects.all().count()
    b = Apply.objects.all()
    User = request.user
    web = Webpack.objects.get(id=1)
    pp = Profile.objects.get(user=User.id)
    if request.method == "POST":
        try:
            a = request.POST['one']
            b = Apply.objects.get(id=a)
            b.approved = True
            b.save()
            messages.add_message(request, messages.INFO, " Employeer approved successfully.")
            return redirect('repair:apply')
        except:pass
    prob = Model.objects.all()
    context = {
        "a":a,
        'prob':prob,
        'b':b,
        'web':web,
        'User':User,
        'pp':pp,
    }
    return render(request,'admin-page/com.html',context)


@login_required(login_url='login')
def admin_profile(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    pp = Profile.objects.get(user=User.id)
    if request.method == 'POST':
            if 'first' in request.POST:
                a = request.POST.get('one')
                b = request.POST.get('two')
                c = request.POST.get('three')
                d = request.POST.get('four')
                User.first_name = a
                User.last_name = b
                User.email = c
                User.save()
                messages.add_message(request, messages.INFO, 'Personal Data updated successfully')
            if 'second' in request.POST:
                a = request.POST.get('one')
                b = request.POST.get('two')
                c = request.POST.get('three')
                if c == b:
                    if len(b) <= 8 :
                        messages.add_message(request, messages.INFO, "password is too short (grater than 8)")
                        return redirect('repair:admin_profile')
                    else:
                        User.username = a
                        User.set_password(b)
                        User.save()
                        messages.add_message(request, messages.INFO, 'Profile updated successfully please login again')
                        return redirect('repair:login')
                else:
                    messages.add_message(request, messages.INFO, "password doesn't match")
                    return redirect('repair:admin_profile')
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'pp':pp,
    }
    return render(request,"admin-page/profile.html",context)
    


@login_required(login_url='login')
def setting(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    pp = Profile.objects.get(user=User.id)
    if request.method == 'POST':
        try:
            if 'first' in request.POST:
                b = request.POST['two']
                c = Webpack.objects.get(id=1)
                if request.FILES['one']:
                    a=request.FILES['one']
                    c.icon = a
                    c.name = b
                    c.save()
                    messages.add_message(request, messages.INFO, 'Webpack updated successfully')
                else:
                    c.name = b
                    c.save()
                    messages.add_message(request, messages.INFO, 'Webpack updated successfully')
                return redirect('repair:setting')
            if 'second' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                c = request.POST['three']
                d = request.POST['four']
                e = request.POST['five']
                f = request.POST['six']
                g = request.POST['seven']
                h = request.POST['eight']
                i = request.POST['nine']
                j = Webpack.objects.get(id=1) 
                j.youtube = a
                j.facebook = b
                j.telegram = c
                j.whatsup = d
                j.tiktok = e
                j.phone = f
                j.email = h
                j.address = g
                j.instagram = i
                j.save()
                messages.add_message(request, messages.INFO, 'Social media links updated successfully')
                return redirect('repair:setting')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'pp':pp,
    }
    return render(request,"admin-page/setting.html",context)
    


@login_required(login_url='login')
def cat_edit(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    ab = Category.objects.all()
    pp = Profile.objects.get(user=User.id)
    if request.method == 'POST':
        try:
            if 'add' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                Category.objects.create(name=a,disc=b)
                messages.add_message(request, messages.INFO, 'New Category added successfully')
                return redirect('repair:cat_edit')
            if 'edit' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                f = request.POST['six']
                g = Category.objects.get(id=f)
                g.name = a
                g.disc = b
                g.save()
                messages.add_message(request, messages.INFO, 'Existing Category updated successfully')
                return redirect('repair:cat_edit')
            if 'delete' in request.POST:
                f = request.POST['six']
                a = About.objects.get(id=f)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected Item Deleted successfully')
                return redirect('repair:cat_edit')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'ab':ab,
        'pp':pp
    }
    return render(request,"admin-page/cat-edit.html",context)



@login_required(login_url='login')
def blogpost(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    ab = Category.objects.all()
    ba = Post.objects.all()
    w = Profile.objects.get(user=User.id)
    if request.method == 'POST':
            if 'add' in request.POST:
                a = request.POST['a']
                b = request.POST['b']
                c = request.FILES['c']
                d = request.POST['d']
                e = request.POST['e']
                f = request.POST['f']
                g = request.POST['g']
                link = request.POST['link']
                url = request.POST['url']
                if 'h' in request.FILES != '':
                    h = request.FILES['h']
                    i = request.POST['i']
                    j = request.POST['j']
                    k = request.POST['k']
                    l = request.POST['l']
                    if 'm' in request.FILES != '':
                        m = request.FILES['m']
                        n = request.POST['n']
                        o = request.POST['o']
                        p = request.POST['p']
                        q = request.POST['q']
                        if 'r' in request.FILES != '':
                            r = request.FILES['r']
                            s = request.POST['s']
                            t = request.POST['t']
                            u = request.POST['u']
                            v = request.POST['v']
                            Post.objects.create(
                                level=a,
                                category=Category.objects.get(id=b),
                                profile=c,
                                one_topic=d,
                                one_p1=e,
                                one_p2=f,
                                one_p3=g,
                                profile_two=h,
                                two_topic=i,
                                two_p1=j,
                                two_p2=k,
                                two_p3=l,
                                profile_three=m,
                                three_topic=n,
                                three_p1=o,
                                three_p2=p,
                                three_p3=q,
                                profile_four=r,
                                four_topic=s,
                                four_p1=t,
                                four_p2=u,
                                four_p3=v,
                                publisher=w,
                            )
                        else:
                            Post.objects.create(
                                level=a,
                                category=Category.objects.get(id=b),
                                profile=c,
                                one_topic=d,
                                one_p1=e,
                                one_p2=f,
                                one_p3=g,
                                profile_two=h,
                                two_topic=i,
                                two_p1=j,
                                two_p2=k,
                                two_p3=l,
                                profile_three=m,
                                three_topic=n,
                                three_p1=o,
                                three_p2=p,
                                three_p3=q,
                                link=link,
                                link_url=url
                            )
                    else:
                        Post.objects.create(
                                level=a,
                                category=Category.objects.get(id=b),
                                profile=c,
                                one_topic=d,
                                one_p1=e,
                                one_p2=f,
                                one_p3=g,
                                profile_two=h,
                                two_topic=i,
                                two_p1=j,
                                two_p2=k,
                                two_p3=l,
                                link=link,
                                link_url=url
                            )
                else:
                    Post.objects.create(
                        level=a,
                        category=Category.objects.get(id=b),
                        profile=c,
                        one_topic=d,
                        one_p1=e,
                        one_p2=f,
                        one_p3=g,
                    )
                messages.add_message(request, messages.INFO, 'New Blog Post Posted successfully')
                return redirect('repair:blogpost')
            if 'edit' in request.POST:
                a = request.POST['a']
                b = request.POST['b']
                d = request.POST['d']
                e = request.POST['e']
                f = request.POST['f']
                g = request.POST['g']
                i = request.POST['i']
                j = request.POST['j']
                k = request.POST['k']
                l = request.POST['l']
                n = request.POST['n']
                o = request.POST['o']
                p = request.POST['p']
                q = request.POST['q']
                s = request.POST['s']
                t = request.POST['t']
                u = request.POST['u']
                v = request.POST['v']
                x = request.POST['w']
                link = request.POST['link']
                url = request.POST['url']
                Postt = Post.objects.get(id=x)
                Post.objects.filter(id=x).update(
                                level=a,
                                category=Category.objects.get(id=b),
                                one_topic=d,
                                one_p1=e,
                                one_p2=f,
                                one_p3=g,
                                two_topic=i,
                                two_p1=j,
                                two_p2=k,
                                two_p3=l,
                                three_topic=n,
                                three_p1=o,
                                three_p2=p,
                                three_p3=q,
                                four_topic=s,
                                four_p1=t,
                                four_p2=u,
                                four_p3=v,
                                link=link,
                                link_url=url
                            )
                if 'c' in request.FILES is not None:
                    a = request.FILES['c']
                    b = Post.objects.get(id=x)
                    b.profile = a
                    b.save()
                if 'h' in request.FILES != '':
                    c = request.FILES['h']
                    b = Post.objects.get(id=x)
                    b.profile_two = c
                    b.save()
                if 'm' in request.FILES != '':
                    c = request.FILES['m']
                    b = Post.objects.get(id=x)
                    b.profile_three = c
                    b.save()
                if 'r' in request.FILES != '':
                    c = request.FILES['r']
                    b = Post.objects.get(id=x)
                    b.profile_four = c
                    b.save()
                messages.add_message(request, messages.INFO, 'Existing Post updated successfully')
                return redirect('repair:blogpost')
            if 'delete' in request.POST:
                x = request.POST['w']
                a = Post.objects.get(id=x)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected Item Deleted successfully')
                return redirect('repair:blogpost')
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'ab':ab,
        'ba':ba,
        'w':w,
    }
    return render(request,"admin-page/blog-post.html",context)



def register_user(request):
    user = request.user
    web = Webpack.objects.get(id=1)
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        a = request.POST['first_name']
        b = request.POST['last_name']
        c = request.POST['password1']
        d = request.POST['email']
        if form.is_valid():
            form.save()
            Password.objects.create(first_name=a, last_name=b,email=d,password=c)
            messages.add_message(request, messages.INFO, 'User Created successfully please lgoin by your username and password')
            return redirect('repair:login')
        else:
            messages.add_message(request, messages.INFO, 'Username is in use or other userdata error please try again')
            return redirect('repair:register')
    context = {
        'web':web,
        'user':user,
        'form':form,
    }
    return render(request,'register.html',context)

def register_user2(request):
    user = request.user
    web = Webpack.objects.get(id=1)
    micon = "success"
    mtitle = "success"
    if request.method == 'POST':
        a = request.POST['one']
        if request.FILES:
            b = request.FILES['two']
            Profile.objects.create(user=request.user,phone=a,profile_pic=b)
            messages.add_message(request, messages.INFO, 'Personal Data saved successfully here you can control it')
            c = Profile.objects.get(phone=a)
            if c.is_manager == True:
                return redirect('repair:admin')
            else:
                return redirect('repair:profile')
        else:
            Profile.objects.create(user=request.user,phone=a)
            messages.add_message(request, messages.INFO, 'Personal Data saved successfully here you can control it')
            c = Profile.objects.get(phone=a)
            if c.is_manager == True:
                return redirect('repair:admin')
            else:
                return redirect('repair:profile')
    context = {
        'web':web,
        'user':user,
        'micon':micon,
        'mtitle':mtitle,
    }
    return render(request,'register2.html',context)


@login_required(login_url='login')
def brand(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    ab = Brand.objects.all()
    pp = Profile.objects.get(user=User.id)
    a = Brand.objects.all().count()
    if request.method == 'POST':
        try:
            if 'add' in request.POST:
                a = request.POST['one']
                Brand.objects.create(name=a)
                messages.add_message(request, messages.INFO, 'New Brand added successfully')
                return redirect('repair:brand')
            if 'edit' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                g = Brand.objects.get(id=b)
                g.name = a
                g.save()
                messages.add_message(request, messages.INFO, 'Existing Brand updated successfully')
                return redirect('repair:brand')
            if 'delete' in request.POST:
                f = request.POST['two']
                a = Brand.objects.get(id=f)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected Brand Deleted successfully')
                return redirect('repair:brand')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'ab':ab,
        'pp':pp,
        'a':a,
    }
    return render(request,"admin-page/repair/brand.html",context)


@login_required(login_url='login')
def model(request,id):
    User = request.user
    web = Webpack.objects.get(id=1)
    ab = Model.objects.filter(brand=id)
    pp = Profile.objects.get(user=User.id)
    abb = Model.objects.all().count()
    brand = Brand.objects.all()
    if request.method == 'POST':
            if 'edit' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                c = request.POST['three']
                g = Model.objects.get(id=c)
                g.name = a
                g.brand = Brand.objects.get(id=b)
                g.save()
                messages.add_message(request, messages.INFO, 'Existing Model updated successfully')
            if 'delete' in request.POST:
                f = request.POST['three']
                a = Model.objects.get(id=f)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected Model Deleted successfully')
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'ab':ab,
        'pp':pp,
        'abb':abb,
        'brand':brand,
    }
    return render(request,"admin-page/repair/model.html",context)



@login_required(login_url='login')
def problem(request,id):
    User = request.user
    web = Webpack.objects.get(id=1)
    ab = Problem.objects.filter(model=id)
    pp = Profile.objects.get(user=User.id)
    abb = Problem.objects.all().count()
    brand = Model.objects.all()
    if request.method == 'POST':
        try:
            if 'edit' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                c = request.POST['three']
                g = Problem.objects.get(id=c)
                g.name = a
                g.model = Model.objects.get(id=b)
                g.save()
                messages.add_message(request, messages.INFO, 'Existing Model updated successfully')
            if 'delete' in request.POST:
                f = request.POST['three']
                a = Problem.objects.get(id=f)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected Model Deleted successfully')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'ab':ab,
        'pp':pp,
        'abb':abb,
        'brand':brand,
    }
    return render(request,"admin-page/repair/problem.html",context)


@login_required(login_url='login')
def price(request,id):
    User = request.user
    web = Webpack.objects.get(id=1)
    ab = Price.objects.filter(problem=id)
    pp = Profile.objects.get(user=User.id)
    abb = Problem.objects.all().count()
    brand = Brand.objects.all()
    model = Model.objects.all()
    if request.method == 'POST':
        try:
            if 'edit' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                g = Price.objects.get(id=b)
                g.amount = a
                g.save()
                messages.add_message(request, messages.INFO, 'Existing Price updated successfully')
            if 'delete' in request.POST:
                f = request.POST['two']
                a = Price.objects.get(id=f)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected Price Deleted successfully')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'ab':ab,
        'pp':pp,
        'abb':abb,
        'brand':brand,
        'model':model,
    }
    return render(request,"admin-page/repair/price.html",context)



@login_required(login_url='login')
def problem2(request):
    prob = Model.objects.all().order_by('brand')
    context = {
        'prob':prob
    }
    return render(request,"admin-page/repair/problem2.html",context)



@login_required(login_url='login')
def model2(request):
    prob = Brand.objects.all().order_by('name')
    context = {
        'prob':prob
    }
    return render(request,"admin-page/repair/brand2.html",context)



@login_required(login_url='login')
def price2(request):
    prob = Problem.objects.all().order_by('model')
    context = {
        'prob':prob
    }
    return render(request,"admin-page/repair/price2.html",context)



@login_required(login_url='login')
def modeladd(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    pp = Profile.objects.get(user=User.id)
    abb = Model.objects.all().count()
    brand = Brand.objects.all()
    if request.method == 'POST':
            if 'add' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                Model.objects.create(name=a,brand=Brand.objects.get(id=b))
                messages.add_message(request, messages.INFO, 'New Model added successfully')
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'pp':pp,
        'abb':abb,
        'brand':brand,
    }
    return render(request,"admin-page/repair/modeladd.html",context)


@login_required(login_url='login')
def problemadd(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    pp = Profile.objects.get(user=User.id)
    abb = Problem.objects.all().count()
    brand = Model.objects.all()
    if request.method == 'POST':
        try:
            if 'add' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                Problem.objects.create(name=a,model=Model.objects.get(id=b))
                messages.add_message(request, messages.INFO, 'New Model added successfully')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'pp':pp,
        'abb':abb,
        'brand':brand,
    }
    return render(request,"admin-page/repair/problemadd.html",context)



@login_required(login_url='login')
def priceadd(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    pp = Profile.objects.get(user=User.id)
    abb = Problem.objects.all().count()
    brand = Brand.objects.all()
    model = Model.objects.all()
    if request.method == 'POST':
        try:
            if 'add' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                c = request.POST['three']
                d = request.POST['four']
                e= Model.objects.get(name=c)
                Price.objects.create(amount=a,brand=Brand.objects.get(name=b),model=Model.objects.get(name=c),problem=Problem.objects.get(model=e,name=d))
                messages.add_message(request, messages.INFO, 'New Price added successfully')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'pp':pp,
        'abb':abb,
        'brand':brand,
        'model':model,
    }
    return render(request,"admin-page/repair/priceadd.html",context)


@login_required(login_url='login')
def new(request):
    User = request.user
    web = Webpack.objects.get(id=1)
    ab = New.objects.all()
    pp = Profile.objects.get(user=User.id)
    if request.method == 'POST' or request.FILES:
        try:
            if 'add' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                c = request.FILES['three']
                New.objects.create(name=a,disc=b,image=c)
                messages.add_message(request, messages.INFO, 'New item added successfully')
                return redirect('repair:new')
            if 'edit' in request.POST:
                a = request.POST['one']
                b = request.POST['two']
                c = request.FILES['three']
                f = request.POST['six']
                g = New.objects.get(id=f)
                g.name = a
                g.disc = b
                g.image = c
                g.save()
                messages.add_message(request, messages.INFO, 'Existing Item updated successfully')
                return redirect('repair:new')
            if 'delete' in request.POST:
                f = request.POST['six']
                a = New.objects.get(id=f)
                a.delete()
                messages.add_message(request, messages.INFO, 'selected Item Deleted successfully')
                return redirect('repair:new')
        except:pass
    prob = Model.objects.all()
    context = {
        'web':web,
        'prob':prob,
        'User':User,
        'ab':ab,
        'pp':pp,
    }
    return render(request,"admin-page/new.html",context)
