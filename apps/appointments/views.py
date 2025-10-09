import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import AppointmentForm
from .models import Appointment
from .config import Config

# Book appointment
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('payment_page', appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form})

# Payment page
def payment_page(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointments/payment.html', {
        "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY,
        "appointment": appointment,
        "amount": Config.appointment_amount
    })

# Create PaymentIntent
@csrf_exempt
def create_payment_intent(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=405)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        intent = stripe.PaymentIntent.create(
            amount=Config.appointment_amount * 100,  # amount in paise
            currency='inr',
            payment_method_types=['card'],
            metadata={'appointment_id': appointment.id},
        )
        # Only return client_secret; JS handles the redirect
        return JsonResponse({'client_secret': intent.client_secret})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

# Payment result page
def payment_result(request):
    status = request.GET.get('status')
    message = request.GET.get('message', '')
    payment_id = request.GET.get('payment_id', '')
    return render(request, 'appointments/payment_result.html', {
        'status': status,
        'message': message,
        'payment_id': payment_id,
    })
