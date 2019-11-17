from productivity.partners import Partners
from productivity.models import *
from django.contrib.auth.models import User
try:
    Role.objects.bulk_create([
        Role(name='Student'),
        Role(name='Teacher'),
        Role(name='Researcher'),
        Role(name='Graduated'),
        Role(name='Member'),
    ])
except Exception as err:
    print(err)
    pass

try:
    Division.objects.bulk_create([
        Division(name='Software'),
        Division(name='Machine Learning'),
        Division(name='Operations'),
        Division(name='Robotics'),
        Division(name='Applied Maths'),
        Division(name='Social Impact'),
        Division(name='General'),
        Division(name='Board'),
        Division(name='Biomedics'),
    ])
except Exception as err:
    print(err)
    pass

try:
    Line.objects.bulk_create([
        Line(topic='Fuzzy logic'),
        Line(topic='Neural networks'),
        Line(topic='Pattern recognition'),
        Line(topic='Computer vision and image processing'),
        Line(topic='Classification and clustering'),
        Line(topic='Genetic programming and swarm intelligence'),
        Line(topic='Searching and sorting algorithms'),
        Line(topic='Internet of things'),
        Line(topic='Planning and scheduling'),
    ])
except Exception as err:
    print(err)
    pass
    
try:
    Partner.objects.bulk_create([
      Partner(**Partners[0]),
      Partner(**Partners[1]),
      Partner(**Partners[2]),
      Partner(**Partners[3])
    ])
except Exception as err:
    print(err)
    pass
