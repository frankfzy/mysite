from django.db import models
# Create your models here.


class Project(models.Model):
    """
    项目表
    """
    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='项目名称')
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
