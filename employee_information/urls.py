from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView
from .views import RegisterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login', auth_views.LoginView.as_view(template_name = 'employee_information/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    path('about', views.about, name="about-page"),
    path('departments', views.departments, name="department-page"),
    path('manage_departments', views.manage_departments, name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
    path('employees', views.employees, name="employee-page"),
    path('employees_child', views.employees_child, name="employee-page-child"),
    path('employees-operator', views.employees_operator, name="employee-page-operator"),
    path('employees-ariza', views.employees_ariza, name="employee-page-ariza"),
    path('manage_employees', views.manage_employees, name="manage_employees-page"),
    path('manage_employees_my', views.manage_employees_my, name="manage_employees-page-my"),
    path('manage_employees_operator', views.manage_employees_operator, name="manage_employees-page-oprarator"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('save_employee_tel', views.save_employee_tel, name="save-employee-tel"),
    path('save_employee_operator', views.save_employee_operator, name="save-employee-page-operator"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('view_employee', views.view_employee, name="view-employee-page"),
    path('ariza_not', views.ariza_not, name="ariza_not"),
    path('ariza_qaytish', views.ariza_qaytish, name="ariza_qaytish"),
    path('sriza_commit', views.sriza_commit, name="sriza_commit"),
    path('summa_limet', views.summa_limet, name="summa_limet"),
    path('summa_limit_save', views.summa_limit_save, name="summa_limit_save"),
    path('ariza_tel', views.ariza_tel, name="ariza_tel"),
    path('enter_summa', views.enter_summa, name="enter_summa"),
    path('ariza_employee_sms', views.ariza_employee_sms, name="save-employee-sms"),
    path('maxshulot_summasi', views.maxshulot_summasi, name="maxshulot_summasi"),
    path('view_summa', views.view_summa, name="view_summa"),
    path('ariza_not_m', views.ariza_not_m, name="ariza_not_m"),
    path('ariza_ok', views.ariza_ok, name="ariza_ok"),
    path('send_shartnoma', views.send_shartnoma, name="send_shartnoma"),
    path('enter_shartnoma', views.enter_shartnoma, name="enter_shartnoma"),
    path('save_shartnoma', views.save_shartnoma, name="save_shartnoma"),


    


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
