from datetime import datetime
from zoneinfo import ZoneInfo
from django.http import JsonResponse


def curr_date(request):
    current_date = datetime.now(tz=ZoneInfo('Europe/Warsaw'))
    response = JsonResponse({'datetime': current_date.strftime('%a %d %b %Y %H:%M:%S')})
    return response