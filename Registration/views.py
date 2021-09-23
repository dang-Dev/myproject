from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseServerError
from .forms import CreateUserForm, PasswordChangingForm, UserStudentForm, UserImageForm
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from .models import UserStudent, UserImage, Logbook
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_text, force_bytes, DjangoUnicodeDecodeError
from django.contrib.auth import update_session_auth_hash
from .tokens import account_activation_token
from django.core.mail import EmailMessage
import datetime
import pytz
from datetime import date
from django.http import HttpResponseForbidden
from django.http import Http404
from .filters import logbookFilter

@login_required(login_url='login')
def index(request):
    if request.user.is_superuser:
        return HttpResponseForbidden()
    elif request.user.is_staff:
        return HttpResponseForbidden()
    # is_activated = UserStudent.objects.get(username=user)
    # if not is_activated.is_activated:
    #     return redirect('confirmation')
    context = {

    }
    return render(request, 'index.html', context=context)


def register(request):
    if request.method == 'POST':
        q_email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user_type = request.POST.get('usertype')

        if password1 != password2:
            messages.success(request, "Password didn't Match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.success(request, 'Username/ID number already used.')
            return redirect('register')

        user = User.objects.create_user(username, q_email, password1)
        user.is_active = False
        user.save()

        UserStudent.objects.create(
            user=user,
            email=q_email,
            username=username,
        )
        UserImage.objects.create(user=user, username=username)

        current_site = get_current_site(request)
        mail_subject = 'Activate your MC Face Recognition account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = q_email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        # return HttpResponse('Please confirm your email address to complete the registration')
        return render(request, 'registration/confirmation.html')
    context = {

    }
    return render(request, 'registration/register.html', context=context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user)
        # return redirect('home')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render(request, 'registration/redirect.html')
        # return redirect("redirect")
    else:
        return HttpResponse('Activation link is invalid!')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {

    }
    return render(request, 'registration/login.html', context=context)


def logoutPage(request):
    logout(request)
    return redirect('login')


def confirmation(request):
    context = {

    }
    return render(request, 'registration/confirmation.html', context=context)


@login_required(login_url='login')
def change_password(request):
    form = PasswordChangingForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change-password')
        else:
            messages.error(request, 'Please correct the error below.')
    context = {
        'form': form,
    }
    return render(request, 'registration/change_password.html', context=context)


@login_required(login_url='login')
def profile(request):
    curr_user = request.user.username
    user = UserStudent.objects.get(username=curr_user)
    img = UserImage.objects.get(username=curr_user)
    context = {
        'user': user,
        'user_img': img,
    }
    return render(request, 'registration/profile.html', context=context)


@login_required(login_url='login')
def profile_edit(request):
    curr_user = request.user.username
    user = UserStudent.objects.get(username=curr_user)
    form = UserStudentForm(instance=user)
    img = UserImage.objects.get(username=curr_user)
    form_img = UserImageForm(instance=img)
    if request.method == "POST":
        # if 'infoForm' in request.POST:
        #     form = UserStudentForm(request.POST, request.FILES, instance=user)
        #     if form.is_valid():
        #         form.save()
        #         messages.success(request, 'Save Changes!')
        #         return redirect('edit_profile')
        # elif 'imageForm' in request.POST:
        #     form_img = UserImageForm(request.POST, request.FILES, instance=img)
        #     if form_img.is_valid():
        #         form_img.save()
        #         messages.success(request, 'Save Changes!')
        #         return redirect('edit_profile')
        form = UserStudentForm(request.POST, request.FILES, instance=user)
        form_img = UserImageForm(request.POST, request.FILES, instance=img)
        if form.is_valid() and form_img.is_valid():
            form.save()
            form_img.save()
            messages.success(request, 'Save Changes!')
            return redirect('edit_profile')

    context = {
        'form': form,
        'form_img': form_img,
        'user_img': img,
    }
    return render(request, 'registration/profile_edit.html', context=context)

@login_required(login_url='admin')
def getData(request, pk):
    student = UserStudent.objects.get(username=pk)
    id_number = str(student.username)
    fname = str(student.first_name)
    mname = str(student.middle_name)
    lname = str(student.last_name)
    age = str(student.age)
    gender = str(student.gender)
    address = str(student.address)
    block = str(student.block)
    course = str(student.course)
    year = str(student.year)
    myjson = '{"id_number":'+id_number+', "fname":"'+fname+'", "mname":"'+mname+'", "lname":"'+lname+'", "age": '+age + \
        ', "gender": "'+gender+'", "address":"'+address+'", "block": "'+block+'", "year":"'+year+'", "course":"'+course+'"}'
    
    return HttpResponse(myjson)
    
@login_required(login_url='admin')
def startSendSMS(request, pk):
    date_time = datetime.datetime.now(pytz.timezone('Asia/Manila'))
    student = UserStudent.objects.get(username=pk)
    cp_num = student.guardian_cp_number
    if cp_num == None:
        return HttpResponse("error1=guardian_number_missing")
    elif len(cp_num) != 11:
        return HttpResponse("error2=guardian_number")
    else:
        cp_num = cp_num[1:11]
        
    id_number = str(student.username)
    fname = str(student.first_name)
    mname = str(student.middle_name)
    lname = str(student.last_name)
    age = str(student.age)
    gender = str(student.gender)
    address = str(student.address)
    block = str(student.block)
    course = str(student.course)
    year = str(student.year)

    # import requests
    # url = "https://api.movider.co/v1/sms"
    # payload = "api_key=1xiIMVvfhjTODynI0HOurQTjYUb&api_secret=RsXRG1EVHqqrfrxt4Syx6MGwIpbzKw10sV0dmmQ0&to=%2B63"+cp_num+"&text=Hellow%20badang&from=UNITECH"
    # headers = {
    #     "Accept": "application/json",
    #     "Content-Type": "application/x-www-form-urlencoded"
    # }
    # response = requests.request("POST", url, data=payload, headers=headers)
    # print(response.text)
    curr_student = Logbook.objects.all().filter(date_time_in__gte=date_time, id_number=id_number)
    has_entrance = False
    for std in curr_student:
        if std.date_time_exit == None:
            has_entrance = True
            Logbook.objects.filter(id=std.id).update(date_time_exit=date_time)
    if not has_entrance:
        return HttpResponse("error3=no_entrance")
    
    return HttpResponse("ok")

@login_required(login_url='admin')
def startQRscanner(request):
    context = {

    }
    return render(request, 'registration/qrcodescanner.html', context=context)


def adminLogin(request):
    path = request.get_full_path()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if path == '/admin/?next=/qrcode_scanner/':
                return redirect('qrcode_scanner')
            else:
                return redirect('reports')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {

    }
    return render(request, 'admin/admin_login.html', context=context)

@login_required(login_url='admin')
def adminReports(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    context = {

    }
    return render(request, 'admin/reports.html', context=context)

def adminlogoutPage(request):
    logout(request)
    return redirect('reports')

@login_required(login_url='admin')  
def adminLogbook(request, pk):
    logbook = Logbook.objects.all()
    myfilter = logbookFilter(request.GET, queryset=logbook)
    logbook = myfilter.qs
    
    if pk == 'view':
        context = {
            'logbook': logbook,
            'myfilter': myfilter,
        }
        return render(request, 'admin/logbook.html', context=context)
    elif pk == 'print':
        IST = pytz.timezone('Asia/Manila')
        today = date.today()
        date_today = today.strftime("%b %d, %Y")
        context = {
            'date': date_today,
            'logbook': logbook,
        }
        return render(request, 'print.html', context=context)

