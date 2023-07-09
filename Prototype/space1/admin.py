from django.contrib import admin
from .models import machineModel, machineListModel, machineDetailModel

# Register your models here.


@admin.register(machineModel)
class machineAdmin(admin.ModelAdmin):
    pass

@admin.register(machineListModel)
class machineListAdmin(admin.ModelAdmin):
    pass

@admin.register(machineDetailModel)
class machineDetailAdmin(admin.ModelAdmin):
    pass