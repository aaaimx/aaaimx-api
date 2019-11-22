from django.db import models
from uuid import uuid4
from datetime import datetime
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

class Role(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=100, unique=True)

class Division(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=100, unique=True)
    story = models.TextField(default="", blank=True)
    logo = models.ImageField(
        default=None, null=True, blank=True, upload_to='logos')

class Partner(models.Model):
    def __str__(self):
        return self.alias
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    name = models.CharField(default="", editable=True, max_length=255, unique=True)
    alias = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(
        default=None, blank=True, upload_to='logos', storage=gd_storage)
    type = models.CharField(max_length=100, default="")

class Member(models.Model):
    def __str__(self):
        return self.fullname
    fullname = models.CharField(default="", unique=True, max_length=200)
    email = models.EmailField(default="", blank=True, max_length=100)
    divisions = models.ManyToManyField(Division, blank=True, verbose_name="divisions")
    active = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role, verbose_name="list of roles")
    charge = models.CharField(max_length=100)
    adscription = models.ForeignKey(Partner, null=True, related_name="adscription_institute", on_delete=models.SET_NULL)

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
    collaborators = models.ManyToManyField(Member, blank=True, verbose_name="collaborators")
    institute = models.ForeignKey(Partner, null=True, on_delete=models.SET_NULL)
    lines = models.ManyToManyField(Line, blank=True, verbose_name="interest areas")

class Research(models.Model):
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "research"
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    title = models.TextField(default="", blank=False)
    lines = models.ManyToManyField(Line, blank=True, verbose_name="research lines")
    projects = models.ManyToManyField(Project, blank=True, verbose_name="related projects")
    resume = models.TextField(default="", blank=True)
    year = models.IntegerField(default=2018, blank=True)
    grade = models.CharField(default="", max_length=100, blank=True)
    event = models.CharField(default="", max_length=200, blank=True)
    pub_in = models.CharField(default="", max_length=200, blank=True)
    pub_type = models.CharField(default="", max_length=200, blank=True)
    type = models.CharField(default="", max_length=200, blank=True)
    link = models.URLField(default="", max_length=200, blank=True)


class Advisor(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    thesis = models.ForeignKey(Research, related_name="advisors", on_delete=models.CASCADE)
    position = models.IntegerField(blank=True, default=1)

class Author(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    research = models.ForeignKey(Research, default=None, related_name="authors", on_delete=models.CASCADE)
    position = models.IntegerField(blank=True, default=1)


# from setup_data import *
# from .collaborators import *
# from .projects import *
# from .research import *