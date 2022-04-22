# DBookmark
- project/urls.py -> app/urls/.py -> app/views.py -> models.py -> templates/app/index.html
- admin.py : 관리자 사이트
- form.py: 입력 사이트
- 개발 순서 : models.py, (admin.py) views.py,(form.py) urls.py, templates
1. startproject DBookmark
   1. python -m pip install django~=3.2
   2. django-admin startproject DBookmark .
   3. python manage.py runserver
2. startapp bookmark
   1. python manage.py startapp bookmark
   2. add 'bookmark', to INSTALLED_APPS in settings.py
3. bookmark/models.py
   1. python manage.py makemigrations bookmark
      1. models -> DB로 옯기기 위한 py
   2. python manage.py migrate
      1. DB 테이블 만들기
   3. bookmark/admin Bookmark
      1. python manage.py createsuperuser
      2. bookmark/models Bookmark \_\_str__()
   4. bookmark/views BookmarkListview
   5. urls, bookmar/urls bookmark:list
   6. templates bookmark_list.html
   7. bookmark/views BookmarkCreateView
   8. urls, bookmark/urls bookmark: add
   9. templates bookmar_create.html
   10. bookmark/view BookmarkDetailView
   11. bookmark/urls Bookmark:detail
   12. templates bookmark_detail.html
   13. bookmark/view BookmarkUpdateview
   14. bookmark/urls bookmark:edit
   15. templates bookmark_update.html
   16. get_absolute_url() in Bookmark