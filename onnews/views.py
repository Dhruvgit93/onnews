from django.shortcuts import render,redirect,get_object_or_404
from .form import add_Editor,update_Editor,Loginform,blog_add
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import blogs

def home(request):
    if request.user.is_authenticated:
        data=blogs.objects.all()
        return render(request,'main/home.html',{'blogs':data})
    return redirect('main:blogpage')

def add_editor(request):
    if request.user.is_authenticated and request.user.is_superuser: 
        if request.method=="POST":
            form=add_Editor(request.POST)
            if form.is_valid():
                user=form.save()
                name=user.username
                user.is_staff=True
                user.save()
                messages.success(request,f'{name} is created successfully')
                return redirect('main:addeditor')
        else:
            form=add_Editor()
        
        data={
            'form':form,
            'data':User.objects.all()
        }
        return render(request,"main/addeditor.html",data)
    return redirect('main:home')

def update_editor(request,id):
    if request.user.is_authenticated and request.user.is_superuser: 
        editor=User.objects.get(id=id)
        form=update_Editor(instance=editor)
        if request.method=="POST":
            form=update_Editor(request.POST,instance=editor)
            if form.is_valid():
                user=form.save()
                name=user.username
                messages.success(request,f'{name} has been updated')
                return redirect('main:addeditor')
        data={
            'form':form,
            'data':User.objects.all()
        }
        return render(request,"main/addeditor.html",data)
    return redirect('main:home')

def deleteeditor(request,id):
    if request.user.is_authenticated and request.user.is_superuser: 
        if request.method=="POST":
            editor=User.objects.get(id=id)
            name=editor.username
            editor.delete()
            messages.warning(request,f'{name} was deleted')
            return redirect('main:addeditor')
        return redirect('main:blogpage')
    return redirect('main:home')

def Loginview(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=Loginform(request,request.POST)
            if form.is_valid():
                valusername = form.cleaned_data.get('username')
                valpassword = form.cleaned_data.get('password')
                editor=authenticate(username=valusername,password=valpassword)
                if editor is not None:
                    login(request,editor)
                    messages.success(request,f'welcome!! {valusername} you are now log-in')
                    return redirect('main:home')
        else:
            form=Loginform()
        data={
            'form':form,
        }
        return render(request,"main/login.html",data)
    return redirect('main:home')

def logoutview(request):
    if request.method=="POST":
        logout(request)
        messages.error(request,'You are now log-out')
        return redirect('main:blogpage')
    return redirect('main:blogpage')

def blogadd(request):
    if request.user.is_authenticated: 
        data=blogs.objects.all()
        if request.method=="POST":
            form=blog_add(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Blog has been created!!')
                return redirect('main:blog_add')        
        else:
            form=blog_add()
        data={
            'form':form,
            'blogs':data
        }
        return render(request,'main/blog_manage.html',data)
    return redirect('main:blogpage')

def blogpage(request):
    data=blogs.objects.all()
    return render(request,'main/blogpage.html',{'blogs':data})

def blogedit(request,id):
    if request.user.is_authenticated:
        blog=blogs.objects.get(id=id)
        blogdata=blogs.objects.all()
        if request.method=="POST":
            form=blog_add(request.POST,instance=blog)
            if form.is_valid():
                form.save()
                messages.success(request,'Blog hs been updated')
                return redirect('main:blog_add')
        else:
            form=blog_add(instance=blog)
        data={
            'form':form,
            'blogs':blogdata
        }
        return render(request,'main/blog_manage.html',data)
    return redirect('main:blogpage')

def blogdelete(request,id):
    if request.method=="POST":
        blog=blogs.objects.get(id=id)
        blog.delete()
        messages.warning(request,'blog has been deleted!!')
        return redirect('main:blog_add')
    return redirect('main:blogpage')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'main/profile.html')
    return redirect('main:blogpage')
