# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

class Article(models.Model):
    title = models.CharField("博客标题", max_length=100)
    category = models.CharField("博客标签", max_length=50, blank=True)
    pub_date = models.DateTimeField("发布日期", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now = True)
    content = UEditorField("文章正文", height=300, width=1000, default='', blank=True, imagePath="uploads/blog/images/", toolbars="besttome", filePath="uploads/blog/files/")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date'] 
        verbose_name = "文章"
        verbose_name_plural = "文章"
