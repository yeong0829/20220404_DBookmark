from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from accounts import views
from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkDetilView, BookmarkUpdateView, \
    BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    # path('list/', BookmarkListView.as_view(), name='list'),  #bookmark:list
    path('list2/', views.list_bookmark, name='list'),
    #path('add/', BookmarkCreateView.as_view(), name='add'),  #bookmark:add
    path('add2/', views.create_bookmark, name='add'),  #bookmark:add
    # path('detail/<int:pk>', BookmarkDetilView.as_view(), name='detail'),   #bookmark:detail
    path('detail2/<int:pk>', views.detail_bookmark, mane = 'detail'),       #bookmark:detail
    path('edit/<int:pk>', BookmarkUpdateView.as_view(), name='edit'),   #bookmark:edit
    # path('delete/<int:pk>/',  BookmarkDeleteView.as_view(), name='delete')
    path('delete2/<int:pk>/',  views.delete_bookmark, name='delete')    #bookmark:delete
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

