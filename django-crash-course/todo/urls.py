from django.urls import path

from .views import todo_list, todo_detail, todo_create

app_name = 'todos'

urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_detail),
    # path('<id:int>/', todo_detail),
    # path('<todo_id>/', todo_detail),
]
