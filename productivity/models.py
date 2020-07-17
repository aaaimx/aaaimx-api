from django.db import models
from uuid import uuid4
from datetime import datetime, timedelta
from django.contrib.postgres.fields import ArrayField, JSONField


class Role(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=100, unique=True)


class Division(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=100, unique=True)
    story = models.TextField(default="", blank=True)
    logo = models.CharField(default="", max_length=100)


class Partner(models.Model):
    def __str__(self):
        return self.alias
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    name = models.CharField(default="", editable=True,
                            max_length=255, unique=True)
    alias = models.CharField(max_length=100, blank=True)
    site = models.URLField(default="", max_length=100, blank=True)
    logoName = models.CharField(max_length=100, blank=True)
    logoFile = models.CharField(
        max_length=100, blank=True, null=True, default="")
    type = models.CharField(max_length=100, default="")


class Member(models.Model):
    def __str__(self):
        return self.name + ' ' + self.surname
    name = models.CharField(default="", max_length=100)
    surname = models.CharField(default="", blank=True, max_length=100)
    email = models.EmailField(default="", blank=True, max_length=100)

    charge = models.CharField(max_length=100, default="", blank=True)
    active = models.BooleanField(default=False)
    board = models.BooleanField(default=False, blank=True)
    committee = models.BooleanField(default=False, blank=True)

    divisions = ArrayField(models.CharField(
        max_length=50, blank=True), size=10, blank=True, null=True, default=list)
    roles = ArrayField(models.CharField(
        max_length=30, blank=True), size=20, blank=True, null=True, default=list)

    thumbnailFile = models.CharField(
        max_length=100, default="", null=True, blank=True)
    adscription = models.ForeignKey(
        Partner, null=True, blank=True, related_name="adscription_institute", on_delete=models.SET_NULL)


class Line(models.Model):
    def __str__(self):
        return self.topic
    topic = models.CharField(default="", unique=True, max_length=200)


class Project(models.Model):
    def __str__(self):
        return self.title
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    title = models.TextField(default="", blank=True)
    start = models.DateField(default=datetime.now, blank=True)
    end = models.DateField(default=datetime.now, blank=True)
    responsible = models.CharField(default="", max_length=100, blank=True)
    collaborators = models.ManyToManyField(
        Member, blank=True, verbose_name="collaborators")
    institute = models.ForeignKey(
        Partner, null=True, on_delete=models.SET_NULL)
    lines = ArrayField(models.CharField(
        max_length=50, blank=True), size=20, blank=True, null=True, default=list)


class Research(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "research"
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    title = models.TextField(default="", blank=False)
    lines = ArrayField(models.CharField(
        max_length=50, blank=True), size=20, blank=True, null=True, default=list)
    projects = models.ManyToManyField(
        Project, blank=True, verbose_name="related projects")
    resume = models.TextField(default="", blank=True)
    year = models.IntegerField(default=2018, blank=True)
    grade = models.CharField(default="", max_length=100, blank=True)
    event = models.CharField(default="", max_length=200, blank=True)
    pub_in = models.CharField(default="", max_length=200, blank=True)
    pub_type = models.CharField(default="", max_length=200, blank=True)
    type = models.CharField(default="", max_length=200, blank=True)
    link = models.URLField(default="", max_length=500, blank=True)


class Advisor(models.Model):
    def __str__(self):
        return '{0}.- {1}, {2}.'.format(self.position, self.member.surname, self.member.name[0:1])
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    research = models.ForeignKey(
        Research, related_name="advisors", on_delete=models.CASCADE)
    position = models.IntegerField(blank=True, default=1)


class Author(models.Model):
    def __str__(self):
        return '{0}.- {1}, {2}.'.format(self.position, self.member.surname, self.member.name[0:1])
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    research = models.ForeignKey(
        Research, default=None, related_name="authors", on_delete=models.CASCADE)
    position = models.IntegerField(blank=True, default=1)
