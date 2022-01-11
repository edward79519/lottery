import random
from django.http import JsonResponse
from draw.models import Prize, Employee
from django.utils import timezone
import datetime as dt
from django.core import serializers


def luckydraw(request):
    prize_id = request.GET.get('prize_id')
    prize = Prize.objects.get(id=prize_id)
    emp_list = Employee.objects.filter(is_check=True, had_award=False)
    print(emp_list)
    if prize.time_qlfy != 0:
        now_date = timezone.localtime(timezone.now()).date()
        date_certi = now_date - dt.timedelta(days=prize.time_qlfy*365)
        emp_list = emp_list.filter(intime__lte=date_certi)
        print(emp_list)
    cnt = emp_list.count()
    win = random.randrange(0, cnt)
    win_person = emp_list[win]
    res = {
        'person_id': win_person.id,
        'person_name': win_person.name,
        'prize_id': prize.id,
        'prize_name': prize.name,
    }
    return JsonResponse(res)


def getPrizeStauts(request):
    try:
        prize_id = request.GET.get('prize_id')
        prize = Prize.objects.get(id=prize_id)
        prize_remain = prize.cnt - prize.awardlist.count()
        res = {
            'status': 'OK',
            'prize_id': prize.id,
            'prize_name': prize.name,
            'prize_remain': prize_remain,
        }
    except ValueError:
        res = {
            'status': 'Error',
            'message': 'do not get prize_id'
        }
        print(res)
    return JsonResponse(res)