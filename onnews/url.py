from django.urls import path
from . import views

app_name='main'
urlpatterns = [
    path('',views.home,name='home'),
    path('addeditor/',views.add_editor,name='addeditor'),
    path('editeditor/<int:id>/',views.update_editor,name='updateeditor'),
    path('deleteeditor/<int:id>/',views.deleteeditor,name='deleteeditor'),
    path('login/',views.Loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
]+[
    path('blog',views.blogpage,name='blogpage'),
    path('blog_add',views.blogadd,name='blog_add'),
    path('blog_edit/<int:id>',views.blogedit,name='blog_edit'),
    path('blog_delete/<int:id>',views.blogdelete,name='blog_delete'),
    path('profile',views.profile,name="profile")
]
