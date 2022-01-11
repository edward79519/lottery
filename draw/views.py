from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Prize, AwardList, Employee
from .forms import AwardModelForm
# Create your views here.


def index(request):
    template = loader.get_template("index.html")
    prizes = Prize.objects.all()
    awards = AwardList.objects.all().order_by('prize_id')
    emp_noaward = Employee.objects.filter(had_award=False)
    if request.method == "POST":
        form = AwardModelForm(request.POST)
        if form.is_valid():
            award = form.save()
            winner = award.emp
            winner.had_award = True
            winner.save()
            return redirect('Draw_index')
    else:
        form = AwardModelForm()
    context = {
        'form': form,
        'prizes': prizes,
        'awards': awards,
        'emp_noaward': emp_noaward,
    }
    return HttpResponse(template.render(context, request))
