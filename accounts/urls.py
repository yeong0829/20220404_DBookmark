from os import path

from accounts import views

app_name = 'accounts'

urlpatterns =[
    path('registr/', views.register, name='register'),  # accounts:register
]