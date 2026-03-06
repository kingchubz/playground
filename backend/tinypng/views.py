from django.utils import timezone
from django.http import JsonResponse


def curr_date(request):
    current_date = timezone.now()
    response = JsonResponse({'datetime': current_date.isoformat()})
    return response