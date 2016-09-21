# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10,verbose_name=u'分类名称')
    class Meta:
        verbose_name = u'产品分类'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Keyword(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'关键词')
    class Meta:
        verbose_name = u'关键词'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Product(models.Model):
    spec_type=(
        ('1', '大号'),
        ('2', '中号'),
        ('3', '小号'),
    )
    name = models.CharField(max_length=10, verbose_name=u'产品名称')
    spec = models.CharField(max_length=1, choices=spec_type,verbose_name=u'产品型号')
    cate = models.ForeignKey(Category, verbose_name=u'产品类别')
    stock = models.IntegerField(default=100, verbose_name=u'库存数量')
    price = models.DecimalField(default=10.00, decimal_places=2, max_digits=8, verbose_name=u'产品价格')
    key = models.ManyToManyField(Keyword, verbose_name=u'关键词')
    #null=True, blank=True成对出现 null=True指数据库 blank=True指表单
    desc = models.TextField(null=True, blank=True, verbose_name=u'产品描述')
    class Meta:
        verbose_name = u'产品'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name



