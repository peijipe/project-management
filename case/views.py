from django.shortcuts import render, get_object_or_404
from .models import Case
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import csv
import io
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .forms import CSVUploadForm


def paginator_queryset(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

@login_required
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
    page_obj = paginator_queryset(request, projects, 4)
    context = {
        'projects': page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'case/pj_list.html', context)


@login_required
def pj_detail(request, pk):
    project = get_object_or_404(Case, pk=pk)
    return render(request, 'case/pj_detail.html', {'project': project})


class CaseImport(generic.FormView):
    template_name = 'case/import.html'
    success_url = reverse_lazy('case:pj_list')
    form_class = CSVUploadForm

    def form_valid(self, form):
        csvfile = io.TextIOWrapper(form.cleaned_data['file'], encoding='utf-8')
        reader = csv.reader(csvfile)

        for row in reader:
            case, created = Case.objects.get_or_create(pk=row[0])
            case.title = row[1]
            case.text = row[2]
            case.created_date = row[3]
            case.updated_date = row[4]
            case.category.name = row[5]
            case.number = row[6]
            case.start_at = row[7]
            case.end_at = row[8]
            case.place = row[9]
            case.member = row[10]
            case.first_skill = row[11]
            case.second_skill = row[12]
            case.personal_skill = row[13]
            case.lower_cost = row[14]
            case.upper_cost = row[15]
            case.company.name = row[16]
            case.comment = row[17]
            case.save()
        return super().form_valid(form)


def case_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cases.csv"'
    writer = csv.writer(response)
    for case in Case.objects.all():
        writer.writerow([case.pk, case.title,case.text, case.created_date, case.updated_date, case.category,
                         case.number, case.start_at, case.end_at, case.place, case.member, case.first_skill,
                         case.second_skill, case.personal_skill, case.lower_cost, case.upper_cost,
                         case.company, case.comment])
    return response
