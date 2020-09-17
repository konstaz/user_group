from django import forms
from .models import Group


class AddUserForm(forms.Form):
    groups = Group.objects.all()
    group_choices = []
    for group in groups:
        group_choices.append((group.id, group.name))

    user_nick = forms.CharField(max_length=30, strip=True)
    group_field = forms.TypedChoiceField(choices=group_choices)


class UserForm(forms.Form):
    group_list = Group.objects.all()
    nickname = forms.CharField(label="Nickname")
    group = forms.ModelChoiceField(queryset=group_list, label="Group")


class GroupForm(forms.Form):
    name = forms.CharField(label="Name", max_length=30)
    description = forms.CharField(label="Desc", max_length=50)