from os import path

from accounts import views

app_name = 'accounts'

urlpatterns =[
    path('registr/', views.register, name='register'),  # accounts:register
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
]