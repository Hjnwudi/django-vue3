from django.db import models

# Create your models here.


class Student(models.Model):
    gender_choices = (('男','男'),('女','女'))
    sno = models.IntegerField(db_column="SNo", primary_key=True, null=False) #学号
    name = models.CharField(db_column="SName", max_length=100, null=False)#名字
    gender = models.CharField(db_column="Gender", max_length=100, choices=gender_choices)#性别
    birthday = models.DateField(db_column="Birthday", null=False)#性别
    mobile = models.CharField(db_column="Mobile", max_length=100)#手机
    email = models.CharField(db_column="Email", max_length=100)#邮箱
    address = models.CharField(db_column="Address", max_length=200)#地址
    image = models.CharField(db_column="Image", max_length=200)#相片

    class Meta:
        managed = True
        db_table = "Student"

    def __str__(self):
        return "学号：%s\t姓名:%s\t性别:%s" %(self.sno,self.name,self.gender)