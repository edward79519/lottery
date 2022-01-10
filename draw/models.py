import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Title(models.Model):
    name = models.CharField(max_length=20)
    grade = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(str(self.grade).zfill(2), self.name)


class Department(models.Model):
    sn = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}_{}".format(self.sn, self.name)


class Employee(models.Model):

    class Location(models.TextChoices):
        TAIPEI = "台北"
        PINGTUNG = "屏東"

    class Gender(models.TextChoices):
        MALE = "男"
        FEMALE = "女"

    sn = models.CharField(max_length=10, unique=True)
    dept = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employee",
    )
    name = models.CharField(max_length=20)
    title = models.ForeignKey(
        Title,
        on_delete=models.PROTECT,
        related_name="employee",
    )
    intime = models.DateField()
    location = models.CharField(
        max_length=10,
        choices=Location.choices,
        default=Location.TAIPEI,
    )
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        default=Gender.MALE,
    )
    is_check = models.BooleanField(default=True)
    had_award = models.BooleanField(default=False)

    def __str__(self):
        return "{}_{}".format(self.sn, self.name)

    def job_period(self):
        period = timezone.localtime(timezone.now()).date() - self.intime
        return period


class Prize(models.Model):
    cate = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    cnt = models.IntegerField(default=1)
    time_qlfy = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=0, default=0)

    def __str__(self):
        return "{}_{}".format(self.cate, self.name)


class AwardList(models.Model):
    emp = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name="awardlist",
    )
    prize = models.ForeignKey(
        Prize,
        on_delete=models.PROTECT,
        related_name="awardlist",
    )
    addtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}_{}".format(self.prize, self.emp.name)
