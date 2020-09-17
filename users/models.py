from django.db import models


class User(models.Model):
    nickname = models.CharField("User's nickname", max_length=30, unique=True)
    date_created = models.DateField("Creation_date", auto_now_add=True)
    group = models.ForeignKey("Group", on_delete=models.PROTECT)

    def __str__(self):
        return self.nickname


class Group(models.Model):
    name = models.CharField("Group's name", max_length=30, unique=True)
    description = models.CharField("Group's description", max_length=50)

    def __str__(self):
        return self.name
