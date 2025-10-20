import os.path

from django.core.paginator import Paginator
from django.db.models.functions import datetime
from django.http import HttpResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from helloWorld.forms import StudentForm
from helloWorld.models import StudentInfo, BookInfo, BookTypeInfo


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


# 删除视图
class Delete(DeleteView):
    model = StudentInfo
    template_name = "student/delete.html"
    success_url = '/student/list'
    context_object_name = 'student'
    pk_url_kwarg = 'id'
    extra_context = {"title": "删除学生信息"}


# 内置模板引擎
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def index(request):
    # 演示过滤器
    str = "hello"
    date = datetime.datetime.now()
    myDict = {"tom": 666, "cat": 999, 'wzw': '333'}
    # 创建一个对象
    zhangsan = Person("zhangsan", 20)
    myList = ["java", "Python", "C"]
    myTuple = ("python", 222, 3.14, False)
    context_value = {
        "msg": str, "msg2": myDict, "msg3": zhangsan,
        "msg4": myList, "msg5": myTuple, "date": date
    }
    context = {
        "str_data": "模板变量示例",
        "dict_data": {"tom": 666, "cat": 999},
        "obj_data": Person("张三", 25),
        "list_data": ["Java", "Python", "C"],
        "tuple_data": ("Python", 222, 3.14)
    }
    return render(request, 'index.html', context=context_value)


# 视图函数
def to_course(request):
    return render(request, 'course.html')


# 图书列表查询
def bookList(request):
    # bookList = BookInfo.objects.all()
    # # 获取数据集的第一条数据的bookName属性值
    # print(bookList[0].bookName)
    # # 返回前2条数据 select * from t_book limit 2
    # bookList = BookInfo.objects.all()[:2]
    # # 查询指定字段
    # bookList = BookInfo.objects.values("bookName", "price")
    # # 查询指定字段 数据以列表方式返回，列表元素以元组表示
    # bookList = BookInfo.objects.values_list("bookName", "price")
    # # 获取单个对象，一般是根据id查询
    # book = BookInfo.objects.get(id=2)
    # print(book.bookName)
    # # 返回满足条件id=2的数据，返回类型是列表
    # bookList = BookInfo.objects.filter(id=2)
    # bookList = BookInfo.objects.filter(id=1, price=100)
    # # filter的查询条件可以设置成字典格式
    # d = dict(id=1, price=100)
    # bookList = BookInfo.objects.filter(**d)
    # # SQL的or查询，需要引入Q，from django.db.models import Q
    # # 语法格式：Q(field=value)|Q(field=value) 多个Q之间用"|"隔开
    # bookList = BookInfo.objects.filter(Q(id=1) | Q(price=88))
    # # SQL的不等于查询，在Q查询中用“~”即可
    # # SQL select * from t_book where not (id=1)
    # bookList = BookInfo.objects.filter(~Q(id=1))
    # # 也可以使用exclude 返回满足条件之外的数据 实现不等于查询
    # bookList = BookInfo.objects.exclude(id=1)
    # # 使用count()方法，返回满足查询条件后的数据量
    # t = BookInfo.objects.filter(id=2).count()
    # print(t)
    # # distinct()方法，返回去重后的数据
    # bookList = BookInfo.objects.values("bookName").distinct()
    # print(bookList)
    # # 使用order_by设置排序
    # # bookList = BookInfo.objects.order_by("price")
    # # bookList = BookInfo.objects.order_by("price")
    # bookList = BookInfo.objects.order_by("id")
    # # annotate类似于SQL里面的GROUP BY方法
    # # 如果不设置values，默认对主键进行GROUIP BY分组
    # # SQL: select bookType_id，SUM(price) AS 'price_sum' from t_book GROUP BYbookType_id
    # r = BookInfo.objects.values('bookType').annotate(Sum('price'))
    # # SQL: select bookType_id，AVG(price) AS 'price_sum' from t_book GROUP BYbookType_id
    # r2 = BookInfo.objects.values('bookType').annotate(Avg('price'))
    # print(r)
    # print(r2)

    bookList = BookInfo.objects.all().order_by('id')
    # Paginator(object_list ,per_page)
    # object_list 结果集/列表
    # per_page 每页多少条记录
    p = Paginator(bookList, 2)
    # 获取第几页的数据
    bookListPage = p.page(1)
    print("图书总记录数:", BookInfo.objects.all().count())
    # 模糊查询图书名称含有"编程"的所有数据
    # bookList = BookInfo.objects.filter(bookName__contains='编程')
    # 查询图书价格大于等于50的所有数据
    bookList = BookInfo.objects.filter(price__gte=50)

    content_value = {'title': "图书列表", "bookList": bookList}
    return render(request, 'book/list.html', context=content_value)


# 多表查询
def bookList2(request):
    # 正向查询
    book: BookInfo = BookInfo.objects.filter(id=2).first()
    print("图书类别：", book.bookType.bookTypeName)

    # 反向查询
    bookType: BookTypeInfo = BookTypeInfo.objects.filter(id=1).first()
    print("图书名称：", bookType.bookinfo_set.first().bookName)
    print("图书类别：", bookType.bookinfo_set.all())
    content_value = {"title": "图书列表"}
    return render(request, 'book/list.html', context=content_value)


# 预处理，添加操作
def preAdd(request):
    bookTypeList = BookTypeInfo.objects.all()
    print(bookTypeList)
    context_value = {"title": "图书添加", "bookTypeList": bookTypeList}
    return render(request, 'book/add.html', context=context_value)


# 图书添加
def add(request):
    # print("bookName:", request.POST.get("bookName"))
    # print("price:", request.POST.get("price"))
    # print("publishDate:", request.POST.get("publishDate"))
    # print("bookType_id:", request.POST.get("bookType_id"))
    book = BookInfo()
    book.bookName = request.POST.get("bookName")
    book.publishDate = request.POST.get("publishDate")
    book.bookType_id = request.POST.get("bookType_id")
    book.price = request.POST.get("price")
    book.save()
    print("id:", book.id)
    return bookList(request)
