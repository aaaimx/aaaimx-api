from django.db import models
from uuid import uuid4
from datetime import datetime


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
    uuid = models.UUIDField(default=uuid4, editable=True)
    name = models.CharField(default="", editable=True, max_length=200, primary_key=True, unique=True)
    alias = models.CharField(max_length=100)
    logo = models.ImageField(
        default=None, blank=True, upload_to='logos')
    type = models.CharField(max_length=100, default="")
    
class Member(models.Model):
    def __str__(self):
        return self.fullname
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    fullname = models.CharField(default="", unique=True, max_length=200)
    email = models.EmailField(default="", blank=True, max_length=100)
    divisions = models.ManyToManyField(Division, verbose_name="divisions")
    active = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role, verbose_name="list of roles")
    charge = models.CharField(max_length=100)
    adscription = models.ForeignKey(Partner, null=True, on_delete=models.SET_NULL)


class Line(models.Model):
    def __str__(self):
        return self.topic
    topic = models.CharField(default="", unique=True, max_length=200)

class Project(models.Model):
    def __str__(self):
        return self.title
    title = models.TextField(default="", blank=True)
    start = models.DateTimeField(default=datetime.now, blank=True)
    end = models.DateTimeField(default=datetime.now, blank=True)
    responsible = models.CharField(default="", max_length=100, blank=True)
    collaborators = models.ManyToManyField(Member, verbose_name="collaborators")
    insitute = models.ForeignKey(Partner, null=True, on_delete=models.SET_NULL)
    lines = models.ManyToManyField(Line, verbose_name="interest areas")

class Research(models.Model):
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "research"
    title = models.TextField(default="", blank=True)
    autors = models.ManyToManyField(Member, verbose_name="list of autors")
    lines = models.ManyToManyField(Line, verbose_name="research lines")
    order = models.CharField(default="", unique=True, max_length=100)
    projects = models.ManyToManyField(Project, verbose_name="related projects")

class Thesis(models.Model):
    def __str__(self):
        return self.research.title
    class Meta:
        verbose_name_plural = "theses"
    research = models.OneToOneField(
        Research,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    resume = models.TextField(default="", blank=True)
    year = models.IntegerField(default=2018)
    grade = models.CharField(max_length=100)
    advisors = models.ManyToManyField(Member, verbose_name="list of adivisors")
    order = models.CharField(default="", unique=True, max_length=100)

class Presentation(models.Model):
    def __str__(self):
        return self.research.title
    research = models.OneToOneField(
        Research,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    resume = models.TextField(default="", blank=True)
    year = models.IntegerField(default=2018)
    event = models.CharField(default="", max_length=200, blank=True)

class Article(models.Model):
    def __str__(self):
        return self.research.title
    research = models.OneToOneField(
        Research,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    resume = models.TextField(default="", blank=True)
    year = models.IntegerField(default=2018)
    published_in = models.CharField(default="", max_length=200, blank=True)
    type = models.CharField(default="", max_length=200, blank=True)
    link = models.URLField(default="", max_length=200, blank=True)


"""
ROLES = ['Student', 'Teacher', 'Researcher', 'Graduated', 'Member']
for r in ROLES:
    try:
        role = Role(name=r)
        role.save()
    except:
        pass


DIVISIONS = ['Software', 'Machine Learning', 'Operations', 'Robotics', 'Applied Maths', 'Social Impact']
for d in DIVISIONS:
    try:
        div = Division(name=d)
        div.save()
    except:
        pass

LINES = ['Fuzzy logic','Neural networks','Pattern recognition','Computer vision and image processing',
    'Classification and clustering','Genetic programming and swarm intelligence','Searching and sorting algorithms',
    'Internet of things','Planning and scheduling']
for l in LINES:
    try:
        line = Line(topic=l)
        line.save()
    except:
        pass
"""


