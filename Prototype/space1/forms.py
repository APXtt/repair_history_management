from django import forms
from .models import machineListModel, machineDetailModel


class addMachineListForm(forms.ModelForm):
    class Meta:
        model = machineListModel
        fields = ['machine', 'date', 'name']


class addMachineDataForm(forms.ModelForm):
    class Meta:
        model = machineDetailModel
        fields = ['machine', 'date_document', 'name', 'point', 'status', 'repair_history',
                  'cut_area', 'cut_size', 'date_in', 'date_out']
