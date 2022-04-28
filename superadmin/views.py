from itertools import count
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail



from .models import *

# Create your views here.
def index(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'index.html')

def index_doc(request):
    return render(request,'index-doc.html')

def index_pat(request):
    return render(request,'index-pat.html')




def login(request):
    uid = User.objects.all()

    # Admin login
    if uid.roles == 'admin':
        try:
            uid = User.objects.get(email=request.session['email'])
            return redirect('index')
        except:
            if request.method == 'POST':
                try:
                    uid = User.objects.get(email=request.POST['email'])
                    if request.POST['password'] == uid.password:
                        request.session['email'] = request.POST['email']
                        return redirect('index')
                    return render(request,'login.html',{'msg':'Please Enter Valid Password'})
                except:
                    return render(request,'login.html')
        return render(request,'login.html') 

    #Doctor Login    
    elif uid.roles == 'doctor':
        try:
            uid = User.objects.get(email=request.session['email'])
            return redirect('index-doc')
        except:
            if request.method == 'POST':
                try:
                    uid = User.objects.get(email=request.POST['email'])
                    if request.POST['password'] == uid.password:
                        request.session['email'] = request.POST['email']
                        return redirect('index-doc')
                    return render(request,'login.html',{'msg':'Please Enter Valid Password'})
                except:
                    return render(request,'login.html')
        return render(request,'login.html')

    # patient Login
    else:
        try:
            uid = User.objects.get(email=request.session['email'])
            return redirect('index-pat')
        except:
            if request.method == 'POST':
                try:
                    uid = User.objects.get(email=request.POST['email'])
                    if request.POST['password'] == uid.password:
                        request.session['email'] = request.POST['email']
                        return redirect('index-pat')
                    return render(request,'login.html',{'msg':'Please Enter Valid Password'})
                except:
                    return render(request,'login.html')
        return render(request,'login.html')



def logout(request):
    del request.session['email']
    return redirect('login')




#-----------------------------Doctor----------------------------# 
def create_doctor(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg = "Doctor Email is already Exits "
            return render(request,'create-doctor.html',{'msg':msg})
        except:
            password = ''.join(choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
            subject = 'welcome to Clinic'
            message = f"""Hello {request.POST['name']},
            Your Username is  {request.POST['email']},
            Your Password is {password} """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            User.objects.create(
                roles = request.POST['roles'],
                name = request.POST['name'],
                email = request.POST['email'],
                password = password,
            )

    return render(request,'create-doctor.html')




def view_doctor(request):
    uid = User.objects.all().filter(roles ='doctor')
    return render(request,'view-doctor.html',{'uid':uid})


def update_doctor(request,pk):
    uid = User.objects.get(id=pk)
    if request.method == 'POST':
        uid.name=request.POST['name']
        uid.clinic_name = request.POST['clinic_name']
        uid.gender = request.POST['gender']
        uid.specialty = request.POST['specialty']
        uid.address = request.POST['address']
        uid.save()
    return render(request,'update-doctor.html',{'uid':uid})




def delete_doctor(request,pk):
    doc = User.objects.get(id=pk)
    doc.delete()
    return redirect('view-doctor')






#----------------------------patient---------------------------------#

def create_patient(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg = "Patient Email is already Exits "
            return render(request,'create-patient.html',{'msg':msg})
        except:
            password = ''.join(choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
            subject = 'welcome to Clinic'
            message = f"""Hello {request.POST['name']},
            Your Username is  {request.POST['email']},
            Your Password is {password} """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            User.objects.create(
                roles = request.POST['roles'],
                name = request.POST['name'],
                email = request.POST['email'],
                password = password,
            )
    return render(request,'create-patient.html')



def view_patient(request):
    uid = User.objects.all().filter(roles = 'patients')
    return render(request,'view-patient.html',{'uid':uid})


def update_patient(request,pk):
    uid = User.objects.get(id=pk)
    if request.method == 'POST':
        uid.name=request.POST['name']
        uid.phone = request.POST['phone']
        uid.gender = request.POST['gender']
        uid.address = request.POST['address']
        if 'profile' in request.FILES:
            uid.profile = request.FILES['profile']
        uid.save()
    return render(request,'update-patient.html',{'uid':uid})




def delete_patient(request,pk):
    pat = User.objects.get(id=pk)
    pat.delete()
    return redirect('view-patient')