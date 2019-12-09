import os
import csv

from django.core.management.base import BaseCommand, CommandError
from squirrel.models import squirrel 

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*')

    def handle(self, *args, **options):
        path = args[0]
        new_names = []
        with open (path) as data:
            body = csv.reader(data)
            names = data.readline().strip().split(',')
            new_names = [x.lower().replace(' ','_').replace('/','_') for x in names]
            for row in body:
                 obj = squirrel()
                 for i, column in enumerate(row):
                     if column == 'true':
                         column = True
                     if column == 'false':
                         column = False
                    
                     setattr (obj, new_names[i], column)

                 obj.save ()
