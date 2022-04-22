from django.shortcuts import render

# 기능 추가
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    #참고: render(request, 'bookmark/bookmark_list.html', {'bookmark_list': Bookmark.objects.all()}

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']    #'__al__'
    template_name_suffix = '_create'    #bookmark_form.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')  #성공했을 때 bookmark 리스트 페이지로 감


class BookmarkDetilView(DetailView):
    model = Bookmark
    
    
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['name', 'url']    # '__all__'
    template_name_suffix = '_update'    #bookmark_update.html
    # success_url = reverse_lazy('bookmark:list')  #수정 성공시 bookmark list로 넘김
    # success_url이 없으면 model의 get_absolute_url()호출
