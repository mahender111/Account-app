from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from student.models import Account, Del_Account


def index(request):
    if request.method =="POST":
        name = request.POST.get("name")
        age= request.POST.get("age")
        status=request.POST.get("status")
        username= request.POST.get("username")
        salary= request.POST.get("salary")
        salary=int(salary)
        addarcard= request.FILES.get("file")
        obj=Account(name=name,age=age,username=username,addarcard=addarcard,salary=salary,status=status)
        obj.save()
    return render(request,"index.html")

def data_list(request):
    dict = Account.objects.filter(Q( salary__gte=2000)|Q(status="draft"))
    # for i in dict:
    #     print(i.salary)
    dict = {'dict':dict}
    return render(request,'datalist.html',dict)



#
# def switch(request):
#     if request.method =="POST":
#         obj=request.POST.get("username")
#         print(obj)
#         # user = User(username=obj)
#         # user.status="published"
#         # user.save()
#         # return render(request,'datalist.html')
#
# #
# def switch(request,status):
#     if status=="draft"or status== "published":
#         data = Account.objects.filter(status="draft")
#     else:
#         data = Account.objects.filter(status="published")

#
# def switch(request):
#     data = Account.objects.filter(status="draft")
#         return "published"

def switch(request):
    if request.method == "POST":
        username = request.POST.get("username")
        obj = Account.objects.get(username=username)
        print(obj.username)
        obj.status="published"
        obj.save()
        return redirect('/list')
    print("asdfasdf")
    return render(request, "datalist.html")




def data_salary(request):
    if request.method == "POST":
        username = request.POST.get("username")
        sal = request.POST.get("sal")
        sal=int(sal)
        # salary=request.POST.get("salary")
        obj = Account.objects.get(username=username)
        print(obj)

        obj.salary=obj.salary+sal
        if obj.salary>100000:
            o = Del_Account(username=obj.username, salary = obj.salary, age =obj.age,addarcard=obj.addarcard,status=obj.status,name=obj.name)
            o.save()
            obj.delete()
        else:
            obj.save()
        # return HttpResponse("hallo",obj)
        return redirect("/sal")
    # print("hhhhhhh")
    return render(request,"salary.html")


def data_sal(request):
    data= Account.objects.all()
    return render(request,"salary.html",{'d':data})

def delete(request):
    data=Account.objects.filter(salary__gte=100000)
    return render(request,"delete.html",{'de':data})

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"home.html")


