from django.http import HttpResponse, HttpRequest, JsonResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now()
    return HttpResponse(f"Oh, hi current server time is: {now}")


def hi(request: HttpRequest):
    query_set = request.GET
    try:
        numbers = list(eval(query_set.get("numbers", '')))
        if len(numbers) == 0:
            return HttpResponse("Empty list")
        sorted_numbers = sorted(numbers)
        data = {
            "status": "OK",
            "numbers": sorted_numbers,
            "message": "Numbers sorted successfully"
        }
        return JsonResponse(data, content_type="application/json")
    except TypeError:
        return HttpResponse("Empty list")
