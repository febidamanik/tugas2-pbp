from django.urls import path
from todolist.views import registrasi_user, login_user, logout_user, show_todolist, create_task, update_status, show_todolist_json, add_task, delete_task

app_name = 'todolist'

urlpatterns=[
    path('', show_todolist, name='show_todolist'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('login/', login_user, name='login_user'),
    path('register/', registrasi_user, name='registrasi_user'),
    path('create-task/', create_task, name='create_task'),
    path('add/', add_task, name='add_task'),
    path('update-status/<int:id>', update_status, name='update_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('logout/', logout_user, name='logout'),
]