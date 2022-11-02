from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from myapp.models import *
import json

# Create your views here.




# @login_required
#公共页面
def common_page(request):
    return render(request,'common_page.html')


# @login_required
#首页
def home(request):
    return render(request,'common_page.html',{'whichHTML':"home.html",'oid':''})

#子页面嵌套
def child(request,eid,oid):
    res=child_json(eid,oid)
    return render(request,eid,res)


#控制不同页面返回不同的数据：数据分发器
def child_json(eid,oid=''):
    res={}
    if eid =='home.html':
        date=DB_home_href.objects.all()
        res={'hrefs':date}
    if eid == 'api_project.html':
        date=DB_project.objects.all()
        res={'project':date}
    if eid=='apis.html':
        project_name=DB_project.objects.filter(id=oid)[0]
        res={'project_name':project_name}
    if eid=='api_cases.html':
        project_name=DB_project.objects.filter(id=oid)[0]
        res={'project_name':project_name}
    if eid=='project_setting.html':
        project_name=DB_project.objects.filter(id=oid)[0]
        res={'project_name':project_name}
    if eid=='apis.html':
        project_name=DB_project.objects.filter(id=oid)[0]
        apis=DB_apis.objects.filter(project_id=oid)
        print(apis)
        res={'project':project_name,"apis":apis}
    return res

 #登录页面
def login(request):

    return render(request,'login.html')


#登录操作
def login_action(request):
    username=request.GET['username']
    password=request.GET['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        request.session['user']=username
        return HttpResponse('成功')
    else:
        return HttpResponse('失败')

 #注册
def register_action(request):
    username = request.GET['username']
    password = request.GET['password']
    print(username,password)
    try:
        user=User.objects.create_user(username=username,password=password)
        user.save()
        return HttpResponse('注册成功~')
    except:
        return HttpResponse('注册失败，用户已存在！')


#退出登录
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

# @login_required
def feedback(request):
    return render(request,'common_page.html',{'whichHTML':'feedback.html','oid':''})


#反馈
def api_feedback(request):
    feedback_text=request.GET['feedback_text']
    DB_feedback.objects.create(user=request.user.username,text=feedback_text)
    return HttpResponse('success')


# @login_required
#帮助
def api_help(request):
    return render(request,'common_page.html',{'whichHTML':'help.html','oid':''})

# @login_required
#项目页
def api_project(request):
    return render(request,'common_page.html',{'whichHTML':'api_project.html','oid':''})


#删除项目
def delete_project(request):
    id=request.GET['project_id']
    DB_project.objects.filter(id=id).delete()
    DB_apis.objects.filter(project_id=id).delete()

    return HttpResponse('True')

#增加项目
def add_project(request):
    project_name=request.GET['project_name']
    remark_name=request.GET['remark_name']
    DB_project.objects.create(name=project_name,remark=remark_name,user=request.user.username,other_user='')

    return HttpResponse('')



#打开接口项目
def open_apis(request,id):
    project_id=id
    return render(request,'common_page.html',{'whichHTML':'apis.html','oid':project_id})


#打开接口项目
def open_api_cases(request,id):
    project_id=id
    return render(request,'common_page.html',{'whichHTML':'api_cases.html','oid':project_id})


#打开接口项目
def open_project_setting(request,id):
    project_id=id
    return render(request,'common_page.html',{'whichHTML':'project_setting.html','oid':project_id})



#保存修改项目设置
def save_project_setting(request,id):
    project_id=id
    name=request.GET['name']
    remark=request.GET['remark']
    other_user=request.GET['other_user']
    DB_project.objects.filter(id=project_id).update(name=name,remark=remark,other_user=other_user)

    return HttpResponse('')


#项目列表增加项目接口
def project_api_add(request,Pid):
    project_id=Pid
    DB_apis.objects.create(project_id=project_id)
    return HttpResponseRedirect(f'/apis/{project_id}/')



#删除项目中的接口
def project_api_del(request,id):
    project_id=DB_apis.objects.filter(id=id)[0].project_id
    DB_apis.objects.filter(id=id).delete()
    return HttpResponseRedirect(f'/apis/{project_id}')

#保存项目接口备注
def save_bz(request):
    id=request.GET['api_id']
    print(id)
    bz_calue=request.GET['bz_value']
    DB_apis.objects.filter(id=id).update(des=bz_calue)
    return HttpResponse('')

#获取项目中的接口备注
def get_bz(request):
    api_id=request.GET['api_id']
    bz_calue=DB_apis.objects.filter(id=api_id)[0].des
    return HttpResponse(bz_calue)


#保存接口
def api_save(request):
    api_id=request.GET['api_id']
    api_name=request.GET['api_name']
    ts_method=request.GET['ts_method']
    ts_url=request.GET['ts_url']
    ts_host=request.GET['ts_host']
    ts_header=request.GET['ts_header']
    ts_body_method=request.GET['ts_body_method']
    ts_api_body=request.GET['ts_api_body']

    if ts_body_method== '返回体':
        api=DB_apis.objects.filter(id=api_id)[0]
        ts_body_method=api.last_body_method
        ts_api_body=api.last_api_body

    else:
        ts_api_body=request.GET['ts_api_body'][0]

    DB_apis.objects.filter(id=api_id).update(
        name=api_name,
        api_method=ts_method,
        api_url=ts_url,
        api_host=ts_host,
        api_header=ts_header,
        body_method=ts_body_method,
        api_body=ts_api_body,
    )

    return HttpResponse('success')


#获取接口ID获取接口数据
def get_api_data(request):
    api_id=request.GET['api_id']
    res=DB_apis.objects.filter(id=api_id).values()[0]

    return HttpResponse(json.dumps(res),content_type='application/json')


#前端接口调试请求
def api_send(request):
    api_id = request.GET['api_id']
    api_name = request.GET['api_name']
    ts_method = request.GET['ts_method']
    ts_url = request.GET['ts_url']
    ts_host = request.GET['ts_host']
    ts_header = request.GET['ts_header']
    ts_body_method = request.GET['ts_body_method']
    # ts_api_body = request.GET['ts_api_body']
    if ts_body_method== '返回体':
        api=DB_apis.objects.filter(id=api_id)[0]
        ts_body_method=api.last_body_method
        ts_api_body=api.last_api_body

        if ts_body_method in ['',None]:
            return HttpResponse('请先选择好请求体编码格式和请求体，再点击send按钮发送请求')
    else:
        ts_api_body=request.GET['ts_api_body']
        api=DB_apis.objects.filter(id=api_id)
        api.update(last_body_method=ts_body_method,last_api_body=ts_api_body)


    return HttpResponse('{"code":200}')




