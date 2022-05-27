from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkDetilView, BookmarkUpdateView, \
    BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    path('list/', BookmarkListView.as_view(), name='list'),  #bookmark:list
    path('add/', BookmarkCreateView.as_view(), name='add'),  #bookmark:add
    path('detail/<int:pk>', BookmarkDetilView.as_view(), name='detail'),   #bookmark:detail
    path('edit/<int:pk>', BookmarkUpdateView.as_view(), name='edit'),   #bookmark:edit
    path('delete/<int:pk>/',  BookmarkDeleteView.as_view(), name='delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

