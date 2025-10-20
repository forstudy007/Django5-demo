from django.db import models


# Create your models here.
class StudentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        db_table = 't_student'


# 图书类别模型（一对多的‘一’方）
class BookTypeInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    bookTypeName = models.CharField(max_length=20)  # 图书类别名称

    class Meta:
        db_table = 't_bookType'  # 表名
        verbose_name = "图书类别"  # Admin后台显示名称


# 图书模型（一对多的‘多’方）
class BookInfo(models.Model):
    id = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=20)  # 图书名称
    price = models.FloatField()  # 价格
    publishDate = models.DateField()  # 出版日期
    # 外键关联（on_delete=PROTECT 表示禁止删除被关联的类别）
    bookType = models.ForeignKey(BookTypeInfo, on_delete=models.PROTECT)

    class Meta:
        db_table = 't_book'
        verbose_name = "图书"
