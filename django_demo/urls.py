"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from myapp.views import *


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^common_page/',common_page),                          #首页
    re_path(r'^home/',home),                                        #介绍
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", child),            #子页面嵌套
    re_path(r'^login/',login),                                      #登录页面
    re_path(r'^login_action/',login_action),                        #登录方法
    re_path(r'^register_action',register_action),                   #注册方法
    re_path(r'^accounts/login/$',login),                            #登录状态检查，非登录状态时页面直接跳转至登录页面
    re_path(r'^logout/',logout),                                    #退出登录
    re_path(r'^api_feedback/',api_feedback),                        #反馈
    re_path(r'^api_help/',api_help),                                #帮助页面
    re_path(r'^feedback',feedback),
    re_path(r'^api_project/',api_project),                          #项目列表
    re_path('^delete_project',delete_project),                      #删除项目
    re_path('^add_project',add_project),                            #新增项目
    re_path('^apis/(?P<id>.*)/$',open_apis),                        #打开项目地址
    re_path('^api_cases/(?P<id>.*)/$',open_api_cases),              #打开接口库页面
    re_path('^project_setting/(?P<id>.*)/$',open_project_setting),  #打开项目设置页面
    re_path('^save_project_setting/(?P<id>.*)/$',save_project_setting),          #保存修改项目设置
    re_path('^project_api_add/(?P<Pid>.*)/$',project_api_add),           #项目列表页面增加接口
    re_path('^project_api_del/(?P<id>.*)/$',project_api_del),           #删除项目接口
    re_path('^save_bz/$',save_bz),                                        #保存项目接口备注
    re_path('^get_bz/$',get_bz),                                        #获取项目接口备注
    re_path('^api_save/$',api_save),                                    #保存接口
    re_path('^get_api_data',get_api_data),                              #获取接口数据
    re_path('^api_send',api_send),                                  #前端接口调试请求


]
