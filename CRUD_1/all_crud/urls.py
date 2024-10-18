from all_crud import views
from django.urls import path
urlpatterns = [
    path("",views.index,name="index"),
    path("add_stu/",views.add_stu,name="add_stu"),
    path("edit_stu/",views.edit_stu,name="edit_stu"),
    path("del_stu/",views.del_stu,name="del_stu"),
]
