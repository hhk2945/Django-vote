# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView,DetailView
from bookmark.models import Bookmark

# Create your views here.

#----List View
class BookmarkLV(ListView):
    model = Bookmark
    template_name = "bookmark/bookmark_list.html"

#----Detail View
class BookmarkDV(DetailView):
    model = Bookmark
    template_name = "bookmark/bookmark_detail.html"