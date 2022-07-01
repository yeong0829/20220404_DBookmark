from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# 기능 추가
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from accounts.models import Profile
from bookmark.forms import BookmarkCreationForm, BookmarkChangeForm
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


def list_bookmark(request):
    # 로그인 사용자 확인하기
    user = request.user
    if user.is_authenticated:   # 로그인 되면
        profile = Profile.objects.get(user=user)
        bookmark_list = Bookmark.objects.filter(profile=profile)# 그 사용자의 북마크 가져오기
    else:   # 로그인 안되면
        bookmark_list = Bookmark.object.none()      # 북마크 없는거 가져오기

    return render(request, 'bookmark/bookmark_list.html', {'bookmark_list': bookmark_list})


def detail_bookmark(request, pk, bookmark_detail=None):
    bookmark = Bookmark.objects.get(pk=pk)
    return render(request, 'bookmark/bookmark_detail.html', {'bookmark': bookmark_detail})


def delete_bookmark(request, pk):
    if request.method == 'POST':    # 삭제 버튼 눌렀을 때
        bookmark = Bookmark.objects.get(pk=pk)
        bookmark.delete()   #DELETE FROM table WHERE 조건
        return redirect('bookmark:list')
    else:   # 처음 bookmark_delete.html 요청
        bookmark = Bookmark.objects.get(pk=pk)
        return render(request, 'bookmark/bookmark_confirm_delete.html', {'bookmark': bookmark})


@Login_required
def create_bookmark(request):
    if request.mothod == "POST":  #사용자가 입력하고 버튼 눌렀을 때
        form = BookmarkCreationForm(request.POST)  # form 가져오기
        if form.is_valid(): # is_valid()
            new_bookmark = form.save(commit=False)# new_bookmark 생성하기(name, url)
            new_bookmark.profile = Profile.objects.get(user=request.user)  # new_bookmark에 profile 추가하기
            new_bookmark.save()
            return redirect('bookmark:list')  # bookmark:list 이동하기
    else:  #빈 폼
        form = BookmarkCreationForm()
        return render(request, 'bookmark/bookmark_create.html', {'form': form})



@Login_required
def modify_bookmark(request, pk):
    if request.method == 'POST':
        form = BookmarkChangeForm(request.POST) # form 가져오기
        if form.is_valid():  #is_valid()
            bookmark = Bookmark.objects.get(pk=pk)  #pk에 해당되는 bookmark 가져오기
            bookmark.name = form.cleaned_data.get('name') # 사용자가 입력한 name set
            bookmark.url = form.cleaned_data.get('url')# 사용자가 입력한 url set
            bookmark.save()
            return redirect('bookmark:list')  # bookmark:list로 이동하기
    else:
        bookmark = Bookmark.objects.get(pk=pk)  # pk에 해당하는 bookmark 정보 가져오기
        form = BookmarkChangeForm(instance=bookmark) # bookmark 정보 넣은 form
    return render(request, 'bookmark/bookmark_update.html', {'form': form})
