from django.shortcuts import redirect, render
from django.http import HttpResponse
from employee_information.models import Department, Position, Employees, Arizalar, Muddat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import CostomUser, Department
from django.core.files.storage import FileSystemStorage
from .forms import RegisterForm, ImageForm
import json
employees = [

    {
        'code':1,
        'name':"John D Smith",
        'contact':'09123456789',
        'address':'Sample Address only'
    },{
        'code':2,
        'name':"Claire C Blake",
        'contact':'09456123789',
        'address':'Sample Address2 only'
    }

]



class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'employee_information/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            if request.user.is_admin:
                Current_form = form.save()
                parent_name = CostomUser.objects.filter(id = request.user.id)
                CostomUser.objects.filter(id = Current_form.id).update(parent = str(parent_name.first()))
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')

                return redirect(to='login')
            elif request.user.is_shop:
                Current_form = form.save()
                parent_name = CostomUser.objects.filter(id = request.user.id)
                CostomUser.objects.filter(id = Current_form.id).update(parent = str(parent_name.first()), is_shop_child = True)
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')
                return redirect(to='login')

        return render(request, self.template_name, {'form': form})



# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

# Create your views here.
@login_required
def home(request):
    if request.user.is_admin:
        context = {
            'page_title':'Home',
            'employees':employees,
            'total_department':len(Department.objects.all()),
            'total_position':len(CostomUser.objects.all()),
            'total_employee':len(Arizalar.objects.all()),
        }
        return render(request, 'employee_information/home.html',context)
    elif request.user.is_shop:
        parent_name = CostomUser.objects.filter(id = request.user.id)
        parent_name_ariza = Department.objects.filter(user = request.user.id)
        context = {
            'page_title':'Home',
            'employees':employees,
            'total_department':len(Department.objects.filter(creater = request.user.username)),
            'total_position':len(CostomUser.objects.filter(parent = str(parent_name.first()))),
            'total_employee':len(Arizalar.objects.filter(parent = parent_name_ariza.first())),
        }
        return render(request, 'employee_information/home.html',context)

    elif request.user.is_shop_child:
        parent_name = CostomUser.objects.filter(id = request.user.id)
        parent_name_ariza = Department.objects.filter(user = request.user.id)
        context = {
            'page_title':'Home',
            'employees':employees,
            'total_department':len(Department.objects.filter(creater = request.user.username)),
            'total_position':len(CostomUser.objects.filter(parent = str(parent_name.first()))),
            'total_employee':len(Arizalar.objects.filter(parent = parent_name_ariza.first())),
        }
        return render(request, 'employee_information/home.html',context)
    elif request.user.is_operator:
        print(request.user.username)
        context = {
            'page_title':'Home',
            'total_employee':len(Arizalar.objects.filter( status = "Новый")),
            'total_employee_my':len(Arizalar.objects.filter(operator = request.user.username )),
        }
        return render(request, 'employee_information/home_operator.html',context)
    else:
        context = {
            'page_title':'Home',
            'employees':'',
            'total_department':'',
            'total_position':'',
            'total_employee':'',
        }
        return render(request, 'employee_information/home.html',context)

def about(request):
    context = {
        'page_title':'About',
    }
    return render(request, 'employee_information/about.html',context)

# Departments
@login_required
def departments(request):
    if request.user.is_admin:
        department_list = Department.objects.all()
        context = {
            'page_title':'Departments',
            'departments':department_list,
        }
        return render(request, 'employee_information/departments.html',context)
    else:
        department_list = Department.objects.filter(creater = request.user.username)
        context = {
            'page_title':'Departments',
            'departments':department_list,
        }
        return render(request, 'employee_information/departments.html',context)
@login_required
def manage_departments(request):
    department = {}
    if request.user.is_admin:
        if request.method == 'GET':
            data =  request.GET
            id = ''
            if 'id' in data:
                id= data['id']
            if id.isnumeric() and int(id) > 0:
            
                department = Department.objects.filter(id=id).first()
        Users = CostomUser.objects.all()
        context = {
            'department' : department,
            'User': Users,
        }
        return render(request, 'employee_information/manage_department.html',context)
    else:
        if request.method == 'GET':
            data =  request.GET
            id = ''
            if 'id' in data:
                id= data['id']
            if id.isnumeric() and int(id) > 0:
            
                department = Department.objects.filter(id=id).first()
        Users = CostomUser.objects.filter(parent = request.user.username)
        context = {
            'department' : department,
            'User': Users,
        }
        return render(request, 'employee_information/manage_department.html',context)


@login_required
def save_department(request):
    data =  request.POST
    users = CostomUser.objects.get(id = data['User'])
    parent_name = CostomUser.objects.filter(id = request.user.id)
    resp = {'status':'failed'}
    try:
        upload = request.FILES['gvohnoma']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        upload1 = request.FILES['Derector_pasporti']
        fss1 = FileSystemStorage()
        file1 = fss1.save(upload1.name, upload1)
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Department.objects.filter(id = data['id']).update(name=data['name'], Tel_derector=data['Tel_derector'], Tel_bugalter=data['Tel_bugalter'], Inn=data['Inn'], Xisob_raqam=data['Xisob_raqam'], Adresss=data['Adresss'], foiz_narx=data['foiz_narx'], gvohnoma = file, Derector_pasporti = file1, status = data['status'])

        else:
            upload = request.FILES['gvohnoma']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            upload1 = request.FILES['Derector_pasporti']
            fss1 = FileSystemStorage()
            file1 = fss1.save(upload1.name, upload1)
            save_department = Department(user=users, name=data['name'], Tel_derector=data['Tel_derector'], Tel_bugalter=data['Tel_bugalter'], Inn=data['Inn'], Xisob_raqam=data['Xisob_raqam'], Adresss=data['Adresss'], foiz_narx=data['foiz_narx'], status = data['status'], gvohnoma = file, Derector_pasporti = file1, creater = str(parent_name.first()))

            save_department.save()
            
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

# Positions
@login_required
def positions(request):
    if request.user.is_admin:
        position_list = CostomUser.objects.all()
        context = {
            'page_title':'Positions',
            'Users':position_list,
        }
        return render(request, 'employee_information/positions.html',context)
    else:
        parent_name = CostomUser.objects.filter(id = request.user.id)
        position_list = CostomUser.objects.filter(parent = str(parent_name.first()))
        context = {
            'page_title':'Positions',
            'Users':position_list,
        }
        return render(request, 'employee_information/positions.html',context)
    return redirect('home-page')
@login_required
def manage_positions(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'employee_information/manage_position.html',context)

@login_required
def save_position(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_position = Position(name=data['name'], description = data['description'],status = data['status'])
            save_position.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_position(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
# Employees
def employees(request):
    if request.user.is_admin:
        employee_list = Arizalar.objects.all()
        employee_list_new = Arizalar.objects.filter(status = 'Новый' )
        employee_list_r = Arizalar.objects.filter(status = 'Рассматривается' )
        employee_list_ot = Arizalar.objects.filter(status = 'Отказано' )
        employee_list_of = Arizalar.objects.filter(status = 'Оформлено' )
        employee_list_otm = Arizalar.objects.filter(status = 'Отменено' )
        context = {
            'page_title':'Employees',
            'employees':employee_list,
            'employee_list_new': employee_list_new,
            'employee_list_r':employee_list_r,
            'employee_list_ot':employee_list_ot,
            'employee_list_of':employee_list_of,
            'employee_list_otm':employee_list_otm,
            'edit_no': 'edit_no'
        }
        print(employee_list_new)
        return render(request, 'employee_information/employees.html',context)
    elif request.user.is_shop:
        parent_name_ariza = Department.objects.filter(user = request.user.id)

        employee_list = Arizalar.objects.filter(parent = parent_name_ariza.first())
        # employee_list = Employees.objects.all()
        context = {
            'page_title':'Employees',
            'employees':employee_list,
        }
        return render(request, 'employee_information/employees.html',context)
    

@login_required
def employees_child(request):
    
    if request.user.is_shop_child:
        parent_name_ariza = Department.objects.filter(user = request.user.id)

        employee_list = Arizalar.objects.filter(parent = parent_name_ariza.first())
        # employee_list = Employees.objects.all()
        context = {
            'page_title':'Employees',
            'employees':employee_list,
        }
        return render(request, 'employee_information/employees_child.html',context)

@login_required
def employees_operator(request):
    if request.user.is_operator:
        employee_list = Arizalar.objects.filter(status = 'Новый', operator = None)
        context = {
            'page_title':'Employees',
            'employees':employee_list,
        }
        return render(request, 'employee_information/employees_operator.html',context)



@login_required
def employees_ariza(request):
    if request.user.is_operator:
        Ariza_my = Arizalar.objects.filter(operator = request.user.username)
        context = {
            "Ariza_my" : Ariza_my,
        }
        return render(request, 'employee_information/employees_operator_my.html',context)

    
@login_required
def manage_employees(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    muddat = Muddat.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Arizalar.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'muddat' : muddat,
        'departments' : departments,
        'positions' : positions,
        
    }
    return render(request, 'employee_information/manage_employee.html',context)



@login_required
def manage_employees_my(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    muddat = Muddat.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Arizalar.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'muddat' : muddat,
        'departments' : departments,
        'positions' : positions,
        
    }
    return render(request, 'employee_information/manage_employee_operator_my.html',context)






@login_required
def manage_employees_operator(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    muddat = Muddat.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Arizalar.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'muddat' : muddat,
        'departments' : departments,
        'positions' : positions,
        
    }
    return render(request, 'employee_information/manage_employee_operator.html',context)

@login_required
def save_employee(request):
    data =  request.POST
    parent_name_ariza = Department.objects.filter(user = request.user.id)
    muddat = Muddat.objects.filter(id = data['type_muddat'])

    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Arizalar.objects.filter(id = data['id']).update(name=data['name'], Tel_derector=data['Tel_derector'], Tel_bugalter=data['Tel_bugalter'], Inn=data['Inn'], Xisob_raqam=data['Xisob_raqam'], Adresss=data['Adresss'], foiz_narx=data['foiz_narx'], status = data['status'])

        else:
            _, file = request.FILES.popitem()
            file = file[0]
            save_Ariza = Arizalar(first_name = data['first_name'],  last_name = data['last_name'],  tel = data['tel'], type_muddat = muddat.first(), parent = parent_name_ariza.first(), pasport_seria = data['pasport_seria'], data_user = data['data_user'], pasport_photo = file) 
            save_Ariza.save()
            # form = ImageForm(request.POST, request.FILES, parent = parent_name_ariza.first())
            # if form.is_valid():
            #     form.save()
            
        resp['status'] = 'success'
    except Exception as e:
        print(e)
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def save_employee_operator(request):
    data =  request.POST
    Operator = CostomUser.objects.filter(id = request.user.id)
    # muddat = Muddat.objects.filter(id = data['type_muddat'])
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Arizalar.objects.filter(id = data['id']).update(status = "Рассматривается", operator = str(Operator.first()))
            
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


# @login_required
# def save_employee(request):
#     data =  request.POST
#     resp = {'status':'failed'}
#     if (data['id']).isnumeric() and int(data['id']) > 0:
#         check  = Employees.objects.exclude(id = data['id']).filter(code = data['code'])
#     else:
#         check  = Employees.objects.filter(code = data['code'])

#     if len(check) > 0:
#         resp['status'] = 'failed'
#         resp['msg'] = 'Code Already Exists'
#     else:
#         try:
#             dept = Department.objects.filter(id=data['department_id']).first()
#             pos = Position.objects.filter(id=data['position_id']).first()
#             if (data['id']).isnumeric() and int(data['id']) > 0 :
#                 save_employee = Employees.objects.filter(id = data['id']).update(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
#             else:
#                 save_employee = Employees(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
#                 save_employee.save()
#             resp['status'] = 'success'
#         except Exception:
#             resp['status'] = 'failed'
#             print(Exception)
#             print(json.dumps({"code":data['code'], "firstname" : data['firstname'],"middlename" : data['middlename'],"lastname" : data['lastname'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"department_id" : data['department_id'],"position_id" : data['position_id'],"date_hired" : data['date_hired'],"salary" : data['salary'],"status" : data['status']}))
#     return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Arizalar.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_employee(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Arizalar.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/view_employee.html',context)



@login_required
def ariza_not(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Arizalar.objects.filter(id = data['id']).update(status = 'Отказано')
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def ariza_qaytish(request):
    department = {}
    if request.user.is_operator:
        if request.method == 'GET':
            data =  request.GET
            id = ''
            if 'id' in data:
                id= data['id']
            if id.isnumeric() and int(id) > 0:
            
                department = Arizalar.objects.filter(id=id).first()
        context = {
            'department' : department,
        }
        return render(request, 'employee_information/ariza_qaytish.html',context)

@login_required
def sriza_commit(request):
    data =  request.POST
    resp = {'status':''}

    try:
        Arizalar.objects.filter(id = data['id']).update(commet = data['commit'], status = 'Qaytish')
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def ariza_tel(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    muddat = Muddat.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Arizalar.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'muddat' : muddat,
        'departments' : departments,
        'positions' : positions,
        
    }
    return render(request, 'employee_information/manage_employee_tel.html',context)

@login_required
def save_employee_tel(request):
    data =  request.POST
    resp = {'status':''}
    dataa = Arizalar.objects.filter(id = data['id']).first()
    try:
        if dataa.status == 'Qaytish':
            Arizalar.objects.filter(id = data['id']).update(tel = data['tel'], status = 'Рассматривается')
            resp['status'] = 'success'
        elif dataa.status == 'SMS':
            Arizalar.objects.filter(id = data['id']).update(code_pasport = data['sms'], status = 'SMS_send')
            resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def ariza_employee_sms(request):
    data =  request.POST
    Operator = CostomUser.objects.filter(id = request.user.id)
    # muddat = Muddat.objects.filter(id = data['type_muddat'])

    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Arizalar.objects.filter(id = data['id']).update(status = "SMS", operator = str(Operator.first()))
            
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def summa_limet(request):
    department = {}
    if request.user.is_operator:
        if request.method == 'GET':
            data =  request.GET
            id = ''
            if 'id' in data:
                id= data['id']
            if id.isnumeric() and int(id) > 0:
            
                department = Arizalar.objects.filter(id=id).first()
        context = {
            'department' : department,
        }
        return render(request, 'employee_information/summa_limit.html',context)

@login_required
def summa_limit_save(request):
    data =  request.POST
    resp = {'status':''}
    
    try:
        Arizalar.objects.filter(id = data['id']).update(summa_limet = data['summa_limet'], status = 'Одобрено')
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def enter_summa(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    muddat = Muddat.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Arizalar.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'muddat' : muddat,
        'departments' : departments,
        'positions' : positions,
        
    }
    return render(request, 'employee_information/enter_summa.html',context)



@login_required
def maxshulot_summasi(request):
    data =  request.POST
    resp = {'status':''}
    dataa = Arizalar.objects.filter(id = data['id']).first()
    
    try:
        if dataa.status == 'Одобрено':
            foiz = Department.objects.filter(user = request.user.id).values()
            foiz_narxx = foiz.first()['foiz_narx']
            yechiladigon_summa = ((int(data['maxshulot_summasi'])*int(foiz_narxx))/100) + int(data['maxshulot_summasi'])
            mud = Arizalar.objects.filter(id = data['id']).values()
            muddat = Muddat.objects.filter(id = mud.first()['type_muddat_id']).values()
            oylik_tolov =yechiladigon_summa/int(muddat.first()['muddat'])
            Arizalar.objects.filter(id = data['id']).update(maxshulot_summasi = data['maxshulot_summasi'],oylik_tolov = oylik_tolov, yechiladigon_summa=yechiladigon_summa, status = 'Одобрено')
            resp['status'] = 'success'
       
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")




@login_required
def view_summa(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    muddat = Muddat.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Arizalar.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'muddat' : muddat,
        'departments' : departments,
        'positions' : positions,
        
    }
    return render(request, 'employee_information/view_summa.html',context)


@login_required
def ariza_not_m(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Arizalar.objects.filter(id = data['id']).update(status = 'Отменено')
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")



@login_required
def ariza_ok(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Arizalar.objects.filter(id = data['id']).update(status = 'Оформлено')
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def send_shartnoma(request):
    data =  request.POST
    
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            upload = request.FILES['shartnoma_asli1']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            upload1 = request.FILES['shartnoma_asli2']
            fss1 = FileSystemStorage()
            file1 = fss1.save(upload1.name, upload1)
            save_department = Arizalar.objects.filter(id = data['id']).update(shartnoma_asli1 = file, shartnoma_asli2 = file1, status = 'Shartnoma')
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def enter_shartnoma(request):
    employee = {}
    
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Arizalar.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        
    }
    return render(request, 'employee_information/enter_shartnoma.html',context)


@login_required
def save_shartnoma(request):
    data =  request.POST
    
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            upload = request.FILES['selfe_photo']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)

            upload1 = request.FILES['shantnoma_imzo1']
            fss1 = FileSystemStorage()
            file1 = fss1.save(upload1.name, upload1)

            upload2 = request.FILES['shantnoma_imzo2']
            fss2 = FileSystemStorage()
            file2 = fss2.save(upload2.name, upload2)
            save_department = Arizalar.objects.filter(id = data['id']).update(selfe_photo = file, shantnoma_imzo1 = file1, shantnoma_imzo2 =file2, status = 'ok')
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")