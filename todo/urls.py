from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', get_todo_page, name='todo_index'),
    url(r'delete/(\d+)$', delete_todo_item, name="make_todo_go_bye_bye"),
    url(r'toggle/(\d+)$', toggle_todo_item, name="todo_toggle"),
    url(r'edit/(\d+)$', edit_todo_item, name="todo_edit"),
    
]