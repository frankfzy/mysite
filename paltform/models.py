from django.db import models
# Create your models here.


class Project(models.Model):
    """
    项目表
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='项目名称')
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
    status = models.BooleanField(default=True, verbose_name='状态')
    LastUpdateTime = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    creatTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class childMoudle(models.Model):
    """
    子模块
    """
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_DEFAULT, verbose_name='所属项目',default=1)
    # project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE, verbose_name='所属项目')
    name = models.CharField(max_length=50, verbose_name='子模块')
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')


