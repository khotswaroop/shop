from django.shortcuts import render,redirect
from productapp.models import Product,UserModel
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from productapp.forms import RegisterForm,UserForm,ProductForm
from django.contrib.auth import authenticate
from productapp.models import Recommendation

# Create your views here.

def index(request):
    return render(request,'index.html')

def addproduct(request):
    if request.method=='POST':
        pid=request.POST['id']
        pshape=request.POST['shape']
        psize=request.POST['size']
        plocation=request.POST['location']
        pprice=request.POST['price']
        data=Product.objects.create(id=pid,shape=pshape,size=psize,location=plocation,price=pprice)
        print(data)
        return render(request,'addproduct.html',{'data':data})
    else:
        return render(request,'addproduct.html')

def showproduct(request):
    showproduct=Product.objects.all()
    return render(request,'showproduct.html',{'showproduct':showproduct})

def editproduct(request,rid):
    if request.method=='POST':
        pid=request.POST['id']
        pshape=request.POST['shape']
        psize=request.POST['size']
        plocation=request.POST['location']
        pprice=request.POST['price']
        update_product=Product.objects.filter(id=rid)
        update_product.update(id=pid,shape=pshape,size=psize,location=plocation,price=pprice)
        return redirect('/addproduct')
    else:
        data=Product.objects.filter(id=rid)
        return render(request,'editproduct.html',{'data':data})

def adduser(request):
    if request.method=='POST':
        uid=request.POST['id']
        uname=request.POST['name']
        uage=request.POST['age']
        uaddress=request.POST['address']
        data=UserModel.objects.create(id=uid,name=uname,age=uage,address=uaddress)
        return render(request,'adduser.html',{'data':data})
    else:
        return render(request,'adduser.html')

def edituser(request,uid):
    if request.method=='POST':
        uname=request.POST['name']
        uage=request.POST['age']
        uaddress=request.POST['address']
        update_user=UserModel.objects.filter(id=uid)
        update_user.update(name=uname,age=uage,address=uaddress)
        return redirect('/adduser')
    else:
        update_user=UserModel.objects.filter(id=uid)
        return render(request,'edituser.html',{'update_user':update_user})

def showuser(request):
    show_user=UserModel.objects.all()
    return render(request,'showuser.html',{'show_user':show_user})


def registration(request):
    if request.method=='POST':
        fm=RegisterForm(request.POST)
        print(fm.is_valid())
        if fm.is_valid():
            fm.save()
        return redirect('/register')
    else:
        fm=RegisterForm()
        return render(request,'register.html',{'fm':fm})

def addrecommendation(request):
    fm1=ProductForm()
    fm2=UserForm()    
    if request.method=='POST':
        fm1=RegisterForm(request.POST)
        fm2=UserForm(request.POST)
        if fm1.is_valid() and fm2.is_valid():
            userobject=fm1.save(commit=True)
            userobject.set_password(userobject.password)
            userobject.save()
            userobject2=fm2.save(commit=False)
            userobject2.name=userobject
            userobject2.save()
    return render(request,'addrecommendation.html',{'fm1':fm1,'fm2':fm2})

def showrecommendation(request):
    view_recommendation=Recommendation.objects.all()
    return render(request,'showrecommendation.html',{'data':view_recommendation})

def login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            # print(uname)
            # print(upass)
            u=authenticate(username=uname,password=upass)
            # print(u)
            if u:
                return redirect('/login')
    else:
        fm=AuthenticationForm()
        return render(request,'login.html',{'fm':fm})

def search(request):
    if request.method=='GET':
        q=request.GET['q']
        if q:
            data=Product.objects.filter(shape__icontains=q)
            return render(request,'search.html',{'data':data})
