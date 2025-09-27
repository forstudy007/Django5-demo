import os.path

from django.http import HttpResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from helloWorld.forms import StudentForm
from helloWorld.models import StudentInfo


# Create your views here.
def index(request):
    return render(request, 'http.html')
    # print('页面请求中')
    # return redirect('/static/new.html', permanent=True)
    # content_value = {'msg': '学python，上www.python222.com'}
    # return render(request, 'index.html', context=content_value)
    # html = "<font color='red'>学python.上www.python222.com</font>"
    # return HttpResponse(html)
    # return HttpResponseNotFound()
    # return JsonResponse({'hello': 'world'})


def bolg(request, id):
    if id == 0:
        return redirect("/static/error.html")
    else:
        return HttpResponse('id是' + str(id) + '的博客页面')


def blog2(request, year, month, day, id):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day) + ' id是：' + str(id) + ' 的博客页面')


def blog3(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day) + ' 的博客页面')


# 定义文件路径
file_path = "E:\\软件安装包\\2.必备工具\\ChromeSetup.rar"


def download_file1(request):
    file = open(file_path, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="file1.rar"'
    return response


def download_file2(request):
    file = open(file_path, 'rb')
    response = StreamingHttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="file2.rar"'
    return response


def download_file3(request):
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="file3.rar"'
    return response


def get_test(request):
    """
    get请求测试
    :param request:
    :return:
    """
    print("请求方式：", request.method)
    # 常用属性
    print("请求头的数据格式：", request.content_type)
    print("请求头上的参数：", request.content_params)
    print("客户端信息：", request.COOKIES)
    print("是什么协议：", request.scheme)
    # 常用方法
    print("是否是Https协议：", request.is_secure())
    print("获取服务器域名：", request.get_host())
    print("路由地址：", request.get_full_path())
    # 请求参数
    print("name:", request.GET.get("name"))
    print("pwd:", request.GET.get("pwd"))
    print("获取不存在的参数:", request.GET.get("aaa", "666"))

    return HttpResponse("http get ok")


def post_test(request):
    """
    post请求测试
    :param request:
    :return:
    """
    print("请求方式:", request.method)
    print("name:", request.POST.get('name'))
    print("pwd:", request.POST.get('pwd'))
    print("获取不存在的参数:", request.POST.get('sdf'))
    return HttpResponse("http post ok")


# Session&Cookie
def to_login(request):
    """
    跳转登录页面
    :param request:
    :return:
    """
    return render(request, 'login.html')


def login(request):
    """
    登录
    :param request:
    :return:
    """
    user_name = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    print("user_name:", user_name)
    print("pwd:", pwd)
    if user_name == 'admin' and pwd == '123456':
        request.session['currentUserName'] = user_name  # session中存一个用户名
        print("获取session", request.session['currentUserName'])
        print("获取所有的session", request.session.items())
        response = render(request, "main.html")
        response.set_cookie('remember', True)  # 设置cookie
        print("Cookie:", request.COOKIES['remember'])
        return response
    else:
        content_value = {"error_info": "用户名或者密码错误!"}
        return render(request, 'login.html', context=content_value)


def to_upload(request):
    """
    跳转文件上传页面
    :param request:
    :return:
    """
    return render(request, "upload.html")


def upload(request):
    """
    文件上传
    :param request:
    :return:
    """
    # 定义上传目录
    upload_dir = "D:\\PracticeDjango\\"

    # 获取上传的文件，如果没有文件，默认为None
    myfile = request.FILES.get('myfile', None)
    if myfile:
        try:
            # 检查并创建目录(如果不存在)
            exist_ok = True
            os.makedirs(upload_dir, exist_ok=True)
            # 打开特定的文件进行二进制的写操作
            with open(os.path.join(upload_dir, myfile.name), 'wb+') as f:
                # 分块写入文件
                for chunk in myfile.chunks():
                    f.write(chunk)
            return HttpResponse("文件上传成功")
        except Exception as e:
            return HttpResponse(f"文件上传失败：{str(e)}")
    else:
        return HttpResponse("没发现文件")


# 列表视图
class List(ListView):
    # 设置模版文件
    template_name = "student/list.html"
    # 设置模型外的数据
    extra_context = {'title': '学生信息列表'}
    # 查询结果集
    queryset = StudentInfo.objects.all()
    # 每页展示5条数据
    paginate_by = 5
    # 设置上下文对象名称
    context_object_name = 'student_list'


# 详情视图
class Detail(DetailView):
    # 设置模版文件
    template_name = "student/detail.html"
    # 设置模型外的数据
    extra_context = {'title': '学生信息详情'}
    # 指定查询模型
    model = StudentInfo
    # 设置上下文对象名称
    context_object_name = 'student'
    # 指定URL中用于获取对象的唯一标识符的参数名称，默认为'pk'
    # pk_url_kwarg = 'id'


# 新增视图
class Create(CreateView):
    # 设置模版文件
    template_name = "student/create.html"
    # 设置模型外的数据
    extra_context = {'title': '学生信息添加'}
    # 指定form
    form_class = StudentForm
    # 执行成功后跳转地址
    success_url = '/student/list'


# 更新视图
class Update(UpdateView):
    # 设置模版文件
    template_name = "student/update.html"
    # 设置模型外的数据
    extra_context = {'title': '学生信息修改'}
    # 设置查询模型
    model = StudentInfo
    # 指定form
    form_class = StudentForm
    # 执行成功后跳转地址
    success_url = '/student/list'
