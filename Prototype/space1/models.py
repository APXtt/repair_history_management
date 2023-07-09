from django.db import models

"""
machineModel : 1~100대의 기계들 (mM)
machineListModel : 각 기계에 들어가있는 문서들 (listM)
machineDetailModel : 각 문서에 들어가는 세부 row(데이터) (detailM)
"""

class machineModel(models.Model):
    id = models.AutoField(primary_key=True)
    n = models.IntegerField()

    def __str__(self):
        return str(self.id)
    
class machineListModel(models.Model):
    id = models.AutoField(primary_key=True)
    machine = models.ForeignKey(machineModel, on_delete=models.CASCADE)
    date = models.DateField() # 수리 일자
    name = models.TextField() # 담당자

    def __str__(self):
        return str(self.date)

class machineDetailModel(models.Model):
    machine = models.ForeignKey(machineModel, on_delete=models.CASCADE, null=True, blank=True)
    date_document = models.ForeignKey(machineListModel, on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True, blank=True) # 각부명칭
    point = models.TextField(null=True, blank=True) # 기준점
    status = models.TextField(null=True, blank=True) # 각부상태
    repair_history = models.TextField(null=True, blank=True) # 수리내역
    cut_area = models.TextField(null=True, blank=True) # 절단부위
    cut_size = models.TextField(null=True, blank=True) # 절단량
    date_in = models.DateField(null=True, blank=True) # 입고일
    date_out = models.DateField(null=True, blank=True) # 출고일

    # 수리 여부
    BEFORE = 'B'
    AFTER = 'A'
    REPAIR_CHOICES = [
        (BEFORE, '수리전'),
        (AFTER, '수리후'),
    ]
    repair_state = models.CharField(
        max_length=1,
        choices=REPAIR_CHOICES,
        default=BEFORE,
    )

    repair_point = models.TextField(null=True, blank=True) # 수리 후
    repair_component = models.TextField(null=True, blank=True) # 부품 교체 내역
    repair_count = models.TextField(null=True, blank=True) # 수량
    repair_note = models.TextField(null=True, blank=True) # 비고




    def __str__(self):
        return str(self.name)