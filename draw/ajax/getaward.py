import random
from django.http import JsonResponse
from draw.models import Prize, Employee
from django.utils import timezone
import datetime as dt


def luckydraw(request):
    prize_id = request.GET.get('prize_id')
    prize = Prize.objects.get(id=prize_id)
    emp_list = Employee.objects.filter(is_check=True, had_award=False)
    if prize.time_qlfy != 0:
        now_date = timezone.localtime(timezone.now()).date()
        date_certi = now_date - dt.timedelta(days=prize.time_qlfy*365)
        emp_list = emp_list.filter(intime__lte=date_certi)
    cnt = emp_list.count()
    win = random.randrange(0, cnt)
    win_person = emp_list[win]
    return JsonResponse(win_person)
