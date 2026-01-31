from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json

def home(request):
    return render(request, "customers/index.html")


@csrf_exempt
def register_customer(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Customer.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            dob=data.get("dob"),
            address=data.get("address"),
            consent=True
        )

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"}, status=400)
def unsubscribe(request, token):
    customer = get_object_or_404(Customer, unsubscribe_token=token)
    customer.consent = False
    customer.save()

    return HttpResponse("""
        <h2>You are unsubscribed</h2>
        <p>You will no longer receive birthday emails from us.</p>
    """)