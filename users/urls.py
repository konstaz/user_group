from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
    # Home
    path("", views.index, name="index"),
    # Users
    path("users/", views.users_list, name="users_list"),
    path("add_user/", views.add_user, name="add_user"),
    path("delete_user/<int:user_id>/", views.delete_user, name="delete_user"),
    path("users/edit_user/<int:user_id>/", views.edit_user, name="edit_user"),
    # Groups
    path("groups/", views.groups_list, name="groups_list"),
    path("add_group/", views.add_group, name="add_group"),
    path("delete_group/<int:group_id>/", views.delete_group, name="delete_group"),
    path("groups/edit_group/<int:group_id>/", views.edit_group, name="edit_group"),
]
