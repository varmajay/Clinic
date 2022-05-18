from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import date



# def check_login(request):
#     try: 
#         uid = User.objects.get(email=request.session['email'])
#         return redirect(True)
#     except:
#         return redirect('login')




# Create your views here.
def main_index(request): 
    doc_count = User.objects.filter(roles ='doctor').count()
    pat_count = User.objects.filter(roles ='patients').count()
    doc = User.objects.filter(roles ='doctor')
    return render(request,'main-index.html',{'doc_count':doc_count,'pat_count':pat_count,'doc':doc})




def index(request):
    try:
        doc_count = User.objects.filter(roles ='doctor').count()
        pat_count = User.objects.filter(roles ='patients').count()
        app_count = Appoinment.objects.filter().count()
        print(app_count)
        admin = User.objects.get(email=request.session['email'])
        return render(request,'index.html',{'admin':admin,'pat_count':pat_count,'app_count':app_count,'doc_count':doc_count})
    except:
        return redirect('login')


def index_doc(request):
    try:
        doc_count = User.objects.filter(roles ='doctor').count()
        pat_count = User.objects.filter(roles ='patients').count()
        app_count = Appoinment.objects.all().count()
        uid = User.objects.get(email=request.session['email'])
        return render(request,'index-doc.html',{'uid':uid,'pat_count':pat_count,'app_count':app_count,'doc_count':doc_count})
    except:
        return redirect('login')


def index_pat(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'index-pat.html',{'uid':uid})
    except:
        return redirect('login')




def login(request):
        try:
            uid = User.objects.get(email=request.session['email'])
            if uid.roles == "admin":
                return redirect('index')
            elif uid.roles =="doctor":
                return redirect('index-doc')
            else:
                return redirect('index-pat')
        except:
            # print(User.roles)
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
                    msg = "Please Enter Valid Email"
                    return render(request,'login.html',{'msg':msg})
        return render(request,'login.html') 



def logout(request):
    del request.session['email']
    return redirect('main-index')




#-------------------------------------------------Doctor------------------------------------------------------# 
# @login_required(login_url='login')
# @check_login()
def create_doctor(request):
    try:
        # uid = User.objects.get(email=request.session['email'])
        admin = User.objects.get(email=request.session['email'])
        if request.method == "POST":
            try:
                User.objects.get(email=request.POST['email'])
                msg = "Doctor Email is already Exits "
                return render(request,'create-doctor.html',{'msg':msg,'admin':admin})
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
        return render(request,'create-doctor.html',{'admin':admin})
    except:
        return redirect('login')
        



def view_doctor(request):
    try:
        admin = User.objects.get(email=request.session['email'])
        uid = User.objects.all().filter(roles ='doctor')
        return render(request,'view-doctor.html',{'admin':admin,'uid':uid})
    except:
        return redirect('login')



def update_doctor(request,pk):
    try:
        admin = User.objects.get(email=request.session['email'])
        uid = User.objects.get(id=pk)
        if request.method == 'POST':
            uid.name=request.POST['name']
            uid.clinic_name = request.POST['clinic_name']
            uid.gender = request.POST['gender']
            uid.specialty = request.POST['specialty']
            uid.address = request.POST['address']
            uid.save()
        return render(request,'update-doctor.html',{'admin':admin,'uid':uid})
    except:
        return redirect('login')





def delete_doctor(request,pk):
    doc = User.objects.get(id=pk)
    doc.delete()
    return redirect('view-doctor')


def profile_doc(request):
    try:
        admin = User.objects.get(email=request.session['email'])
        uid = User.objects.get(email=request.session['email'])
        if request.method == 'POST':
            uid.name = request.POST['name']
            uid.clinic_name = request.POST['clinic_name']
            uid.gender = request.POST['gender']
            uid.specialty = request.POST['specialty']
            uid.address = request.POST['address']
            uid.save()
            # return redirect('index-doc')
        return render(request,'profile-doc.html',{'uid':uid})
    except:
        return redirect('login')



#---------------------------------------------------------patient-----------------------------------------------#

def create_patient(request):
    try:
        admin = User.objects.get(email=request.session['email'])
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
        return render(request,'create-patient.html',{'admin':admin})
    except:
        return redirect('login')



def view_patient(request):
    try:
        admin = User.objects.get(email=request.session['email'])
        uid = User.objects.all().filter(roles = 'patients')
        return render(request,'view-patient.html',{'uid':uid,'admin':admin})
    except:
        return redirect('login')


def update_patient(request,pk):
    try:
        admin = User.objects.get(email=request.session['email'])
        uid = User.objects.get(id=pk)
        if request.method == 'POST':
            uid.name=request.POST['name']
            uid.phone = request.POST['phone']
            uid.gender = request.POST['gender']
            uid.address = request.POST['address']
            if 'profile' in request.FILES:
                uid.profile = request.FILES['profile']
            uid.save()
        return render(request,'update-patient.html',{'uid':uid,'admin':admin})
    except:
        return redirect('login')




def delete_patient(request,pk):
    pat = User.objects.get(id=pk)
    pat.delete()
    return redirect('view-patient')



def profile_pat(request):
    try:
        admin = User.objects.get(email=request.session['email'])
        uid = User.objects.get(email=request.session['email'])
        if request.method == "POST":
            uid.name = request.POST['name']
            uid.gender = request.POST['gender']
            uid.address = request.POST['address']
            if 'profile' in request.FILES:
                uid.profile = request.FILES['profile']
            uid.save()
        return render(request,'profile-pat.html',{'uid':uid,'admin':admin})
    except:
        return redirect('login')




#----------------------------------------------------------slot---------------------------------------------------#
def slot(request):
    try:
        data = User.objects.get(email = request.session['email'])
        uid = Slot.objects.filter(doctor_id__id = data.id)
        # print(uid)

        # print(uid2,'---------------------------------')
        if request.method == "POST":
            uid2 = Slot.objects.filter(doctor_id__id = data.id,timeslot= int(request.POST['timeslot']),weeks=int(request.POST['weeks'])).exists()
            if uid2:
                # print('Duplicate', int(request.POST['timeslot']))
                msg='Slot is Already Added'
                return render(request,'slot.html',{'msg':'Slot is Already Added'}) 
            else:
                # print('Non-Duplicate', int(request.POST['timeslot']))

                Slot.objects.create(
                    doctor_id = data,
                    weeks = request.POST['weeks'],
                    timeslot = request.POST['timeslot']
                )
                print('hello')
                msg = "Slot Added Sucessfully"
            return render(request,'slot.html',{'msg':msg})
        return render(request,'slot.html')
    except:
        return redirect('login')

    
        

def slot_view(request):
    try:
        sess = User.objects.get(email=request.session['email'])
        uid = Slot.objects.all().order_by('weeks','timeslot')
        # print(uid.doctor_name)
        return render(request,'slot-view.html',{'uid':uid,'sess':sess})
    except:
        return redirect('login')



def slot_update(request,pk):
    try:
        sess = User.objects.get(email=request.session['email'])
        uid = Slot.objects.get(id=pk)
        # uid = Slot.objects.filter(doctor_id__id = data.id)
        if request.method == 'POST':
            uid.weeks = request.POST['weeks']
            uid.timeslot = request.POST['timeslot']
            uid.save()
            msg = "Slot Added Sucessfully"
        return render(request,'slot-update.html',{'uid':uid})
    except:
        return redirect('login')


def slot_delete(request,pk):
    slot = Slot.objects.get(id=pk)
    slot.delete()
    return redirect('slot-view')








#-----------------------------------------------------Appoinment---------------------------------------------#

def book_app(request):
    try:
        book = User.objects.filter(roles='doctor')
        # app = Appoinment.objects.all()
        slot = Slot.objects.all().order_by('weeks')
        # print(slot,'---------------slot---------------------')
        # print(len(slot),'---------------slot---------------------')
        f_id = []
        for i in slot:
            # print(i.id)
            a = Appoinment.objects.filter(slot=i)
            # print(a)
            for a1 in a:
                f_id.append(a1.slot.id)
        # print(f_id,'===============')
        final_slot = Slot.objects.all().exclude(id__in=f_id).order_by('weeks')
        # print(final_slot,'---------------final_slot---------------------')
        return render(request,'book-app.html',{'book':book,'slot':slot})
    except:
        return redirect('login')


def create_book_app(request):
    try:
        # print(request.POST['weeks'])
        # print(request.POST['timeslot'])
        # print(request.POST['slot_id'])
        # doc_v = request.GET.get("doc_v")
        pat = User.objects.get(email=request.session['email'])
        # print(getslot,'---------------------svkj sj--------nc hzc')
        # print(getslot,'hekkojz ffcz')
        # now = datetime.date.today()
        # print(now)
        if request.method == "POST":
            getslot = Slot.objects.get(weeks=request.POST['weeks'], timeslot = request.POST['timeslot'],doctor_id__id = request.POST['doctor_name'])
            Appoinment.objects.create(
                slot = getslot,
                patients_id = pat.id,
                patient_name = pat.name,
                weeks = request.POST['weeks'],
                timeslot = request.POST['timeslot'],
                date = request.POST['date'],
                description = request.POST['description'],
            )
        return redirect('book-app')
    except:
        return redirect('login')




def get_slot_list(request):
        # print(request.GET.get("doc_n"),'-----------------------')
    temp = User.objects.get(email = request.session['email'])
    week_n = request.GET.get("week_n")
    doc_v = request.GET.get("doc_v")
    # print("week_n",week_n)
    # print("week_n",doc_v)
    # book = User.objects.filter(roles='doctor')
    # app = Appoinment.objects.get()
    # slot = Slot.objects.filter(doctor_id = request.GET.get("doc_n")).order_by('weeks').values('id','weeks')
    # slot1 = Slot.objects.filter(weeks = week_n).filter(doctor_id=doc_v).order_by('timeslot').values('id','timeslot')

    print(temp.id,'===========')
    booked_app = []
    app = Appoinment.objects.filter(patients_id=temp.id)
    for i in app:
        booked_app.append(i.slot.id)
    print(booked_app,'----------')
    
    final_slot = Slot.objects.filter(doctor_id = request.GET.get("doc_n")).exclude(id__in=booked_app).order_by('weeks').values('id','weeks')
    print(final_slot,'---------------final_slot---------------------')

    # print(temp.id,'===========')
    booked_app1 = []
    app1 = Appoinment.objects.filter(patients_id=temp.id)
    for i in app1:
        booked_app1.append(i.slot.id)
    # print(booked_app1,'----------')
    slot1 = Slot.objects.filter(weeks = week_n).filter(doctor_id=doc_v).exclude(id__in=booked_app).order_by('timeslot').values('id','timeslot')

    return JsonResponse({
        "instances" : list(final_slot),
        "instances1" : list(slot1)
    })
    
    # return HttpResponse(slot)



def book_app_view(request):   #PATIENTS
    try:
        pat = User.objects.get(email= request.session['email'])
        uid = Appoinment.objects.filter(patients_id=pat.id)
        return render(request,'book-app-view.html',{'uid':uid})
    except:
        return redirect('login')




def view_appoinment(request): #DOCTOR
    try:
        doc = User.objects.get(email= request.session['email'])
        # print("ddd",doc)
        # slot = Slot.objects.filter(doctor_id=doc.id)
        # print(slot)
        now = date.today()
        print(now)
        uid = Appoinment.objects.filter(slot__doctor_id=doc.id)
        # print(uid)
        return render(request,'view-appoinment.html',{'uid':uid,'doc':doc,'now':now})
    except:
        return redirect('login')
  





#----------------------------------------------Status-action-------------------------------------------------#

def status_complete(request,pk):
    uid = Appoinment.objects.get(id=pk)
    # var = Slot.objects.get(id=uid.slot.id)
    # print(var)
    uid.status = 1
    uid.save()
    # var.delete()
    # var.save()
    return redirect('view-appoinment')


def status_absent(request,pk):
    uid = Appoinment.objects.get(id=pk)
    uid.status = 2
    uid.save()
    return redirect('view-appoinment')


def status_cancelled(request,pk):
    uid = Appoinment.objects.get(id=pk)
    uid.status = 3
    uid.save()
    return redirect('view-appoinment')



def pat_status_cancelled(request,pk):
    uid = Appoinment.objects.get(id=pk)
    uid.status = 3
    uid.save()
    return redirect('book-app-view')








#----------------------------------------admin view Appoinment-------------------------------#


def view_appoinment_admin(request):
    try:
        uid = Appoinment.objects.all()
        admin = User.objects.get(email=request.session['email'])
        return render(request,'view-appoinment-admin.html',{'uid':uid,'admin':admin})
    except:
        return redirect('login')

