from django.shortcuts import render, get_object_or_404
from .models import Case, Company
from django.db.models import Q


def pj_list(request):
    keyword = request.GET.get("keyword1")
    if keyword:
        print(keyword)
        projects = Case.objects.all()
        projects = projects.filter(
            Q(title__contains=keyword) | Q(text__contains=keyword)
        )
        projects = projects.order_by('created_date')
        return render(request, 'case/pj_list.html', {'projects': projects})

    keyword2 = request.GET.get("keyword2")
    keyword3 = request.GET.get("keyword3")
    if keyword2 and keyword3:
        projects = Case.objects.all()
        projects = projects.filter(company=keyword2, lower_cost__lte=keyword3)
        projects = projects.order_by('created_date')
        return render(request, 'case/pj_list.html', {'projects': projects})

    if keyword2:
        print(keyword2)
        projects = Case.objects.all()
        projects = projects.filter(company=keyword2)
        projects = projects.order_by('created_date')
        return render(request, 'case/pj_list.html', {'projects': projects})

    if keyword3:
        print(keyword3)
        projects = Case.objects.all()
        projects = projects.filter(
            Q(lower_cost__lte=keyword3, upper_cost__gte=keyword3) |
            Q(lower_cost=None, upper_cost__gte=keyword3) |
            Q(lower_cost__lte=keyword3, upper_cost=None)
        )
        projects = projects.order_by('created_date')
        return render(request, 'case/pj_list.html', {'projects': projects})

    category_list = request.GET.getlist("keyword4")
    if category_list:
        print(category_list)
        print(len(category_list))
        queryset = {}
        for num in range(len(category_list)):
            queryset[num] = Case.objects.all()
            queryset[num] = queryset[num].filter(category=category_list[num]).order_by('created_date')
            num += 1
        print(num)

        if num == 5:
            projects = queryset[0] | queryset[1] | queryset[2] | queryset[3] | queryset[4]
        elif num == 4:
            projects = queryset[0] | queryset[1] | queryset[2] | queryset[3]
        elif num == 3:
            projects = queryset[0] | queryset[1] | queryset[2]
        elif num == 2:
            projects = queryset[0] | queryset[1]
        else:
            projects = queryset[0]
        return render(request, 'case/pj_list.html', {'projects': projects})

    projects = Case.objects.all().order_by('created_date')
    return render(request, 'case/pj_list.html', {'projects': projects})


def pj_detail(request, pk):
    project = get_object_or_404(Case, pk=pk)
    return render(request, 'case/pj_detail.html', {'project': project})
