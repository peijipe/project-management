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
        return render(request, 'case/pj_list.html', {'projects': projects})  # ここでrenderで返すと02,03ｍでいかない

    keyword = request.GET.get("keyword2")
    if keyword:
        print(keyword)
        projects = Case.objects.all()
        projects = projects.filter(company=keyword)
        projects = projects.order_by('created_date')
        return render(request, 'case/pj_list.html', {'projects': projects})

    keyword = request.GET.get("keyword3")
    if keyword:
        print(keyword)
        projects = Case.objects.all()
        projects = projects.filter(
            Q(lower_cost__lte=keyword, upper_cost__gte=keyword) |
            Q(lower_cost=None, upper_cost__gte=keyword) |
            Q(lower_cost__lte=keyword, upper_cost=None)
        )
        projects = projects.order_by('created_date')
        return render(request, 'case/pj_list.html', {'projects': projects})

    projects = Case.objects.all().order_by('created_date')
    return render(request, 'case/pj_list.html', {'projects': projects})


def pj_detail(request, pk):
    project = get_object_or_404(Case, pk=pk)
    return render(request, 'case/pj_detail.html', {'project': project})
