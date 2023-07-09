from django.shortcuts import render, redirect
from django.db.models import Q
from .models import machineModel as mM, machineListModel as listM, machineDetailModel as DetailM
from django.core.paginator import Paginator
from .forms import addMachineListForm as listF, addMachineDataForm as DetailF
from django.http import QueryDict


def index(request):
    query = request.GET.get('q')
    if query:
        mList = mM.objects.filter(
            Q(n=query)
        )
    else:
        mList = mM.objects.all()

    paginator = Paginator(mList, 25)
    page = request.GET.get('page') # 페이지 번호 (1~4)
    showPage = paginator.get_page(page)

    context = {'machine': showPage}
    return render(request, 'space1/index.html', context)


def detail(request, n):
    m = listM.objects.filter(Q(machine=n)).order_by('-date')

    context = {'machine': m,
               'n': n}
    return render(request, 'space1/detail.html', context)


def view(request, n, m):
    detailList = DetailM.objects.filter(
        Q(machine=n) & Q(date_document=m))
    date = listM.objects.get(id=m).date
    name = listM.objects.get(id=m).name

    context = {'machine': detailList,
               'n': n,
               'm': m,
               'date': date,
               'name': name
               }
    return render(request, 'space1/view.html', context)


def short(request, n):
    m = mM.objects.get(n=n)

    context = {'machine': m}
    return render(request, 'space1/short.html', context)


def edit(request, n):
    if request.method == 'POST':
        data = request.POST.copy()
        data.update({'machine': n})
        form = listF(data)
        if form.is_valid():
            form.save()
            return redirect('edit', n=n)
    else:
        form = listF()
    machineList = listM.objects.filter(Q(machine=n)).order_by('-date')

    context = {'form': form,
               'n': n,
               'machine': machineList}
    return render(request, 'space1/edit.html', context)



"""
formStatus
1 : Edit
2 : Delete
3 : Create
4 : Repair Status Change
5 : Re Repair Status Change
"""
def edit2(request, n, m):
    if request.method == 'POST':
        data = request.POST.copy()
        formOption = data.getlist('formStatus')[0]
        inputCount = len(data.getlist('date_in'))

        if formOption == '3':  # Create
            for i in range(0, inputCount):
                if data.getlist('date_in')[i]:
                    query_di = data.getlist('date_in')[i]
                    query_do = data.getlist('date_out')[i]
                    query_n = data.getlist('name')[i]
                    query_p = data.getlist('point')[i]
                    query_s = data.getlist('status')[i]
                    query_rh = data.getlist('repair_history')[i]
                    query_ca = data.getlist('cut_area')[i]
                    query_cs = data.getlist('cut_size')[i]
                    query_tmp = QueryDict('date_in={}&date_out={}&name={}&point={}&status={}&repair_history={}&cut_area={}&cut_size={}&machine={}&date_document={}'.format(
                        query_di, query_do, query_n, query_p, query_s, query_rh, query_ca, query_cs, n, m))
                    form = DetailF(query_tmp)
                    if form.is_valid():
                        form.save()
        elif formOption == '1' and inputCount == 1:  # Edit
            if data.getlist('select_ids'):
                ids = data.getlist('select_ids')
                query_di = data.getlist('date_in')[-1]
                query_do = data.getlist('date_out')[-1]
                query_n = data.getlist('name')[-1]
                query_p = data.getlist('point')[-1]
                query_s = data.getlist('status')[-1]
                query_rh = data.getlist('repair_history')[-1]
                query_ca = data.getlist('cut_area')[-1]
                query_cs = data.getlist('cut_size')[-1]
                for i in ids:
                    DetailM.objects.filter(id=i).update(date_in=query_di, date_out=query_do, name=query_n, point=query_p, status=query_s, repair_history=query_rh, cut_area=query_ca, cut_size=query_cs)
        elif formOption == '2' and inputCount == 1:  # Delete
            if data.getlist('select_ids'):
                ids = data.getlist('select_ids')
                for i in ids:
                    DetailM.objects.filter(id=i).delete()
        elif formOption == '4' and inputCount == 1:  # Repair Status Change
            if data.getlist('select_ids'):
                ids = data.getlist('select_ids')
                rp = data.getlist('repair_point')[0]
                rc = data.getlist('repair_component')[0]
                rct = data.getlist('repair_count')[0]
                rn = data.getlist('repair_note')[0]
                for i in ids:
                    DetailM.objects.filter(
                        id=i).update(repair_state='A', repair_point=rp, repair_component=rc, repair_count=rct, repair_note=rn)
        elif formOption == '5' and inputCount == 1:  # Re Repair Status Change
            if data.getlist('select_ids'):
                ids = data.getlist('select_ids')
                for i in ids:
                    DetailM.objects.filter(
                        id=i).update(repair_state='B')
        return redirect('edit2', n=n, m=m)
    else:
        form = DetailF()
    date = listM.objects.get(id=m).date
    detailList = DetailM.objects.filter(
        Q(machine=n) & Q(date_document=m))
    context = {'date': date,
               'n': n,
               'm': m,
               'form': form,
               'machine': detailList}
    return render(request, 'space1/edit2.html', context)


def edit_delete(request, n):
    if request.method == 'POST':
        ids = request.POST.getlist('delete_ids')
        for i in ids:
            listM.objects.filter(id=i).delete()
    return redirect('edit', n=n)


def iolist(request):
    return render(request, 'space1/iolist.html')
