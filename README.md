# DBookmark
- project/urls.py -> app/urls/.py -> app/views.py -> models.py -> templates/app/index.html
- admin.py : 관리자 사이트
- form.py: 입력 사이트
- 개발 순서 : models.py, (admin.py) views.py,(form.py) urls.py, templates
1. startproject DBookmark
   1. python -m pip install django~=3.2
   2. django-admin startproject DBookmark .
   3. python manage.py runserver