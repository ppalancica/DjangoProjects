from django.urls import path

from .views import todo_list, todo_detail

app_name = 'todos'

urlpatterns = [
    path('', todo_list),
    path('<id>/', todo_detail),
    # path('<id:int>/', todo_detail),
    # path('<todo_id>/', todo_detail),
]
