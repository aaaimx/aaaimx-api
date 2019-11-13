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

# class Authors(models.Model):
#     member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
#     research_id = models.ForeignKey(Research, on_delete=models.CASCADE)
#     position = models.IntegerField(blank=True, default=1)

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



# try:
#     Role.objects.bulk_create([
#         Role(name='Student'),
#         Role(name='Teacher'),
#         Role(name='Researcher'),
#         Role(name='Graduated'),
#         Role(name='Member'),
#     ])
# except Exception as err:
#     print(err)
#     pass

# try:
#     Division.objects.bulk_create([
#         Division(name='Software'),
#         Division(name='Machine Learning'),
#         Division(name='Operations'),
#         Division(name='Robotics'),
#         Division(name='Applied Maths'),
#         Division(name='Social Impact'),
#     ])
# except Exception as err:
#     print(err)
#     pass

# try:
#     Line.objects.bulk_create([
#         Line(topic='Fuzzy logic'),
#         Line(topic='Neural networks'),
#         Line(topic='Pattern recognition'),
#         Line(topic='Computer vision and image processing'),
#         Line(topic='Classification and clustering'),
#         Line(topic='Genetic programming and swarm intelligence'),
#         Line(topic='Searching and sorting algorithms'),
#         Line(topic='Internet of things'),
#         Line(topic='Planning and scheduling'),
#     ])
# except Exception as err:
#     print(err)
#     pass
    

    
