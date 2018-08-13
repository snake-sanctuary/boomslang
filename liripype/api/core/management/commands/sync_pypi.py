from django.core.management.base import BaseCommand, CommandError

import requests
import multiprocessing as mp
from xml.etree import ElementTree


class Command(BaseCommand):
    help = ''

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # zzz = requests.post('https://pypi.python.org/simple', data = {})
        #resp = requests.get('https://pypi.python.org/simple')
        # tree = ElementTree.fromstring(resp.content)
        # print([a.text for a in tree.iter('a')])
        resp = requests.get('https://pypi.python.org/pypi/django/')
        from pprint import pprint
        pprint(resp.content)
