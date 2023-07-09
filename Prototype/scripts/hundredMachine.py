import os
import sys
import django

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from space1.models import machineModel

def hundredMachineModel():
    for i in range(1, 101):
        machineModel.objects.create(n=i)

hundredMachineModel()