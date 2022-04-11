from django.shortcuts import render

# 기능 추가

from django.views.generic import ListView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    #참고: render(request, 'bookmark/bookmark_list.html', {'bookmark_list': Bookmark.objects.all()}