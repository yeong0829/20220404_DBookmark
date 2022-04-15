from django.shortcuts import render

# 기능 추가
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    #참고: render(request, 'bookmark/bookmark_list.html', {'bookmark_list': Bookmark.objects.all()}

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']    #'__al__'
    template_name_suffix = '_create'    #bookmark_form.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')  #성공했을 때 bookmark 리스트 페이지로 감
