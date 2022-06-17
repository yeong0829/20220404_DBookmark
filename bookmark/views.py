from django.shortcuts import render

# 기능 추가
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from accounts.models import Profile
from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    #참고: render(request, 'bookmark/bookmark_list.html', {'bookmark_list': Bookmark.objects.all()}

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:  # 로그인 하면, 호그인한 사용자의 북마크만 보이게 함
            # user -> profile -> bookmark
            profile = Profile.objects.get(user=user)    # user -> profile
            bookmark_list = Bookmark.objects.filter(profile=profile)    # profile -> bookmark_list
        else:                      # 로그인 안하면, 북마크 표시 안됨
            bookmark_list = Bookmark.objects.none()  # 북마크 안보임
            # bookmark_list = Bookmark.objects.none()  # 북마크 다 보여줌
        return bookmark_list

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['profile', 'name', 'url']    #'__al__'
    template_name_suffix = '_create'    #bookmark_form.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')  #성공했을 때 bookmark 리스트 페이지로 감

    def get_initial(self):
        # user -> profile
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return {'profile': profile}


class BookmarkDetilView(LoginRequiredMixin, DetailView):
    model = Bookmark
    
    
class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['name', 'url']    # '__all__'
    template_name_suffix = '_update'    #bookmark_update.html
    # success_url = reverse_lazy('bookmark:list')  #수정 성공시 bookmark list로 넘김
    # success_url이 없으면 model의 get_absolute_url()호출


class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')
