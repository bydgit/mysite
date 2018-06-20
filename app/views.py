#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/18 下午10:48
# @Author : bydong
# @Site : 
# @File : views.py
# @Software: PyCharm
from django.shortcuts import render
from models import *


def IndexView(request):

    books=BookInfo.objects.all()
    for book in books:
        for b in book.authors.all():
            print(b.name)

    authors=AuthorInfo.objects.all()
    for author in authors:
        for book in author.bookinfo_set.all():
            print(book.title)
    context={"authors":authors,"books":books}
    return render(request,'app/index.html',context)