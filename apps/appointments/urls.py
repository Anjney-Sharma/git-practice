from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book-appointment/", views.book_appointment, name="book_appointment"),
    path("pay/<int:appointment_id>/", views.payment_page, name="payment_page"),
    path(
        "create-payment/<int:appointment_id>/",
        views.create_payment_intent,
        name="create_payment",
    ),
    path("payment/result/", views.payment_result, name="payment_result"),
]
