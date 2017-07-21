from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """
    项目
    """

    """
    项目名
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Version(models.Model):
    """
    版本
    """

    """
    版本号
    """
    number = models.CharField(max_length=20)

    """
    关联的项目
    """
    project = models.ForeignKey(Project)

    def __str__(self):
        return '{}{}'.format(self.project.name, self.number)


class DevType(models.Model):
    """
    开发类型
    """

    """
    名称
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class DevModel(models.Model):
    """
    模块
    """

    """
    名称
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    任务
    """

    PRIORITY_CHOICES = ((0, 'P0'), (1, 'P1'), (2, 'P2'), (3, 'P3'),)

    """
    版本
    """
    version = models.ForeignKey(Version)

    """
    开发类型
    """
    dev_type = models.ForeignKey(DevType)

    """
    模块
    """
    dev_model = models.ForeignKey(DevModel)

    """
    任务描述，功能点
    """
    description = models.CharField(max_length=500)

    """
    优先级
    """
    priority = models.SmallIntegerField(default=0, choices=PRIORITY_CHOICES)

    """
    产品责任人
    """
    product_liable = models.ForeignKey(User, related_name='product_liable')

    """
    技术责任人
    """
    development_liable = models.ForeignKey(User, related_name='development_liable')

    """
    进度
    """
    progress = models.CharField(max_length=20)

    """
    评审时间
    """
    review_time = models.DateTimeField(blank=True, null=True)

    """
    开始开发时间
    """
    dev_start_time = models.DateTimeField(blank=True, null=True)

    """
    完成开发时间
    """
    dev_complete_time = models.DateTimeField(blank=True, null=True)

    """
    提测时间
    """
    test_start_time = models.DateTimeField(blank=True, null=True)

    """
    发布时间
    """
    release_time = models.DateTimeField(blank=True, null=True)
