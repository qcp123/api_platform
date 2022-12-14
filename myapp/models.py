from django.db import models

# Create your models here.



#反馈表
class DB_feedback(models.Model):
    user=models.CharField(max_length=30,null=True)    #反馈人
    text=models.CharField(max_length=1000,null=True)    #反馈内容
    ctime=models.DateTimeField(auto_now=True)    #反馈时间


    def __str__(self):

        return str(self.user)+'  ' + str(self.text)+'  ' + str(self.ctime)

#首页链接地址表
class DB_home_href(models.Model):
    name=models.CharField(max_length=30,null=True)    #超了解文本
    href=models.CharField(max_length=2000,null=True)  #超链接

    def __str__(self):
        return self.name


#项目表
class DB_project(models.Model):
    name=models.CharField(max_length=100,null=True)
    remark=models.CharField(max_length=2000,null=True)
    user=models.CharField(max_length=15,null=True)
    other_user=models.CharField(max_length=300,null=True)
    ctime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




#接口数据库字段
class DB_apis(models.Model):
    project_id = models.CharField(max_length=10,null=True)              #项目id
    name =  models.CharField(max_length=100,null=True)                  #接口名字
    api_method =  models.CharField(max_length=10,null=True)             #请求方式
    api_url =  models.CharField(max_length=1000,null=True)              #url
    api_header =  models.CharField(max_length=1000,null=True)           #请求头
    api_login =  models.CharField(max_length=10,null=True)              #是否带登陆态
    api_host =  models.CharField(max_length=100,null=True)              #域名
    des =  models.CharField(max_length=100,null=True)                   #描述
    body_method =  models.CharField(max_length=20,null=True)            #请求体编码格式
    api_body =  models.CharField(max_length=1000,null=True)             #请求体
    result =  models.TextField(null=True)                               #返回体 因为长度巨大，所以用大文本方式存储
    sign =  models.CharField(max_length=10,null=True)                   #是否验签
    file_key =  models.CharField(max_length=50,null=True)               #文件key
    file_name =  models.CharField(max_length=50,null=True)              #文件名
    public_header =  models.CharField(max_length=1000,null=True)        #全局变量-请求头

    last_body_method=models.CharField(max_length=20,null=True)          #上次请求体编码格式
    last_api_body=models.CharField(max_length=1000,null=True)           #上次请求体


    def __str__(self):
        return self.name




