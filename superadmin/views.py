from calendar import week
import json
import email
from itertools import count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail



from .models import *

# Create your views here.


def main_index(request):
    return render(request,'main-index.html')




def index(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'index.html')

def index_doc(request):
    return render(request,'index-doc.html')

def index_pat(request):
    return render(request,'index-pat.html')




def login(request):
    
    # Admin login
        try:
            
            uid = User.objects.get(email=request.session['email'])
            if uid.roles == "admin":
                return redirect('index')
            elif uid.roles =="doctor":
                return redirect('index-doc')
            else:
                return redirect('index-pat')
        except:
            print(User.roles)
            if request.method == 'POST':
                try:
                    uid = User.objects.get(email=request.POST['email'])
                    if uid.roles == "admin":
                        if request.POST['password'] == uid.password:
                            request.session['email'] = request.POST['email']
                            return redirect('index')
                        return render(request,'login.html',{'msg':'Please Enter Valid Password'})
                    elif uid.roles == "doctor":
                        if request.POST['password'] == uid.password:
                            request.session['email'] = request.POST['email']
                            return redirect('index-doc')
                        return render(request,'login.html',{'msg':'Please Enter Valid Password'})
                    else:
                        if request.POST['password'] == uid.password:
                            request.session['email'] = request.POST['email']
                            return redirect('index-pat')
                        return render(request,'login.html',{'msg':'Please Enter Valid Password'})
                except:
                    return render(request,'login.html')
        return render(request,'login.html') 



def logout(request):
    del request.session['email']
    return redirect('main-index')




#--------------------------------------------------Doctor------------------------------------------------------# 
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


def profile_doc(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.clinic_name = request.POST['clinic_name']
        uid.gender = request.POST['gender']
        uid.specialty = request.POST['specialty']
        uid.address = request.POST['address']
        uid.save
    return render(request,'profile-doc.html',{'uid':uid})



#---------------------------------------------------------patient-----------------------------------------------#

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



def profile_pat(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        uid.name = request.POST['name']
        uid.gender = request.POST['gender']
        uid.address = request.POST['address']
        if 'profile' in request.FILES:
            uid.profile = request.FILES['profile']
        uid.save()
    return render(request,'profile-pat.html',{'uid':uid})





#----------------------------------------------------------slot---------------------------------------------------#
def slot(request):
    uid = Slot.objects.all()
    data = User.objects.get(email = request.session['email'])
    if request.method == 'POST':
        Slot.objects.create(
            doctor_id = data,
            weeks = request.POST['weeks'],
            timeslot = request.POST['timeslot']
        )
    return render(request,'slot.html',{'uid':uid})


def slot_view(request):
    sess = User.objects.get(email=request.session['email'])
    uid = Slot.objects.all().order_by('weeks')
    # print(uid.doctor_name)
    return render(request,'slot-view.html',{'uid':uid,'sess':sess})


def slot_update(request,pk):
    uid = Slot.objects.get(id=pk)
    if request.method == 'POST':
        uid.weeks = request.POST['weeks']
        uid.timeslot = request.POST['timeslot']
        uid.save()
    return render(request,'slot-update.html',{'uid':uid})

def slot_delete(request,pk):
    slot = Slot.objects.get(id=pk)
    slot.delete()
    return redirect('slot-view')








#-----------------------------------------------------Appoinment---------------------------------------------#

def book_app(request):
    book = User.objects.filter(roles='doctor')
    slot = Slot.objects.all().order_by('weeks')
    
    return render(request,'book-app.html',{'book':book,'slot':slot})

def create_book_app(request):
    # print(request.POST['weeks'])
    # print(request.POST['timeslot'])
    # print(request.POST['slot_id'])
    pat = User.objects.get(email=request.session['email'])
    getslot = Slot.objects.get(id = request.POST['slot_id']) 
    if request.method == "POST":
        Appoinment.objects.create(
            slot = getslot, 
            patients_id = pat.id,
            patient_name = pat.name,
            weeks = request.POST['weeks'],
            timeslot = request.POST['timeslot'],
            description = request.POST['description'],
        )
    return redirect('book-app')



def book_app_view(request):
    return render(request,'book-app-view.html')



def get_slot_list(request):
    # print(request.GET.get("doc_n"),'-----------------------')
    week_n = request.GET.get("week_n")
    doc_v = request.GET.get("doc_v")
    # print("week_n",week_n)
    # print("week_n",doc_v)
    # book = User.objects.filter(roles='doctor')
    slot = Slot.objects.filter(doctor_id = request.GET.get("doc_n")).order_by('weeks').values('weeks')
    slot1 = Slot.objects.filter(weeks = week_n).filter(doctor_id=doc_v).order_by('timeslot').values('id','timeslot')
    # print(slot1)
    return JsonResponse({
        "instances" : list(slot),
        "instances1" : list(slot1)
    })
    
    # return HttpResponse(slot)