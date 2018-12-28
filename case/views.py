from django.shortcuts import render, get_object_or_404
from .models import Case, Company
from django.db.models import Q


def pj_list(request):
    keyword = request.GET.get("keyword")
    if keyword:
        projects = Case.objects.all().filter(
            Q(title__contains=keyword) | Q(text__contains=keyword)
        )
        projects = projects.order_by('created_date')
        return render(request, 'case/pj_list.html', {'projects': projects})

    category_list = request.GET.getlist("category")
    cost = request.GET.get("cost")

    if category_list and cost:
        print(category_list)
        queryset = {}
        for num in range(len(category_list)):
            queryset[num] = Case.objects.all()
            queryset[num] = queryset[num].filter(category=category_list[num]).order_by('created_date')
            num += 1
        projects = Case.objects.none()
        count = 0
        while count < len(category_list):
            projects = projects | queryset[count]
            count += 1

        projects = projects.filter(lower_cost__lte=cost).order_by('created_date')
        return render(request, 'case/pj_list.html', {'projects': projects})

    if category_list:
        queryset = {}
        for num in range(len(category_list)):
            queryset[num] = Case.objects.all()
            queryset[num] = queryset[num].filter(category=category_list[num]).order_by('created_date')
            num += 1
        projects = Case.objects.none()
        count = 0
        while count < len(category_list):
            projects = projects | queryset[count]
            count += 1
        return render(request, 'case/pj_list.html', {'projects': projects})

    if cost:
        projects = Case.objects.all().filter(
            Q(lower_cost__lte=cost, upper_cost__gte=cost) |
            Q(lower_cost=None, upper_cost__gte=cost) |
            Q(lower_cost__lte=cost, upper_cost=None)
        )
        projects = projects.order_by('created_date')
        return render(request, 'case/pj_list.html', {'projects': projects})

    projects = Case.objects.all().order_by('created_date')
    return render(request, 'case/pj_list.html', {'projects': projects})


def pj_detail(request, pk):
    project = get_object_or_404(Case, pk=pk)
    return render(request, 'case/pj_detail.html', {'project': project})
