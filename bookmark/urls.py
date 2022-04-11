from django.urls import path

from bookmark.views import BookmarkListView

app_name = 'bookmark'

urlspaatterns = [
    path('list/', BookmarkListView.as_view(), name='list')  #bookmark:list
]