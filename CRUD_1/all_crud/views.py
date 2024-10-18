from django.shortcuts import render,redirect
from all_crud.models import stu_record

# Create your views here.
def index(request,): 
    all_rec=stu_record.objects.all()
    return render(request,"index.html",{"all_rec":all_rec})
  
    
def add_stu(request):
    if request.method=="GET":
        return render(request,"add.html")
    rollNo=request.POST.get("rollNo")
    FullName=request.POST.get("FullName")
    PhoneNumber=request.POST.get("PhoneNumber")
    City=request.POST.get("City")
    Course=request.POST.get("Course")
    a=stu_record(fullName=FullName,phoneNo=PhoneNumber,city=City,course=Course,rollNo=rollNo)
    a.save()
    return redirect("index")

def edit_stu(request):
    if request.method=="GET":
        rollNo=request.GET["rollNo"]
        all_data=stu_record.objects.get(rollNo=rollNo)
        return render(request,"edit.html",{"all_data":all_data})
    # rollNo=request.POST["rollNo"]
    
    rollNo=request.GET["rollNo"]
    FullName=request.POST["FullName"]
    PhoneNumber=request.POST["PhoneNumber"]
    City=request.POST["City"]
    Course=request.POST["Course"]
    b=stu_record.objects.get(rollNo=rollNo)
    b.rollNo=rollNo
    b.fullName=FullName
    b.phoneNo=PhoneNumber
    b.city=City
    b.course=Course
    b.save()
    return redirect("index")
    
def del_stu(request):
    rollNo=request.GET["rollNo"]
    b=stu_record.objects.get(rollNo=rollNo)
    b.delete()

    return redirect("index") 