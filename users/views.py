from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import User, Group
from .forms import UserForm, GroupForm


def index(request):
    """The home page for users"""
    users = len(User.objects.all())
    groups = len(Group.objects.all())
    context = {"users": users, "groups": groups}
    return render(request, "index.html", context)


def users_list(request):
    """The page with users list."""
    users = User.objects.all()
    groups = Group.objects.all()
    form = UserForm()
    context = {"users": users, "groups": groups, "form": form}
    return render(request, "users_list.html", context)


def add_user(request):
    """Add a new user."""
    nick = request.POST["nickname"]
    group_id = request.POST["group"]
    chosen_group = Group.objects.get(id=group_id)
    try:
        User.objects.create(nickname=nick, group=chosen_group)
    # Do not add nick which has already existed.
    except IntegrityError:
        messages.info(request, "This nickname is occupied, please choose another.")
    finally:
        return redirect("users:users_list")


def delete_user(request, user_id):
    """Delete a chosen user."""
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect("users:users_list")


def edit_user(request, user_id):
    """Edit a chosen user."""
    user = get_object_or_404(User, id=user_id)

    if request.method != "POST":
        form = UserForm()
    else:
        form = UserForm(data=request.POST)
        if form.is_valid():
            user.nickname = request.POST["nickname"]
            user.group = Group.objects.get(id=request.POST["group"])
            user.save()
            return redirect("users:users_list")

    context = {"user": user, "form": form}
    return render(request, "edit_user.html", context)


def groups_list(request):
    """The page with groups list."""
    groups = Group.objects.all()
    form = GroupForm()
    context = {"groups": groups, "form": form}
    return render(request, "groups_list.html", context)


def add_group(request):
    """Add a new group."""
    name = request.POST["name"]
    description = request.POST["description"]
    try:
        Group.objects.create(name=name, description=description)
    except IntegrityError:
        messages.info(request, "This group is already exists.")
    finally:
        return redirect("users:groups_list")


def delete_group(request, group_id):
    """Delete a chosen group."""
    group = get_object_or_404(Group, id=group_id)
    try:
        group.delete()
    # Can't delete if the user is assigned to this group.
    except ProtectedError:
        messages.info(request, "Unable to delete if at least one user is assigned to this group.")
    finally:
        return redirect("users:groups_list")


def edit_group(request, group_id):
    """Edit a chosen group."""
    group = get_object_or_404(Group, id=group_id)

    if request.method != "POST":
        form = GroupForm()
    else:
        form = GroupForm(data=request.POST)
        if form.is_valid():
            group.name = request.POST["name"]
            group.description = request.POST["description"]
            group.save()
            return redirect("users:groups_list")

    context = {"group": group, "form": form}
    return render(request, "edit_group.html", context)
