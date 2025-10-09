# a59ae98d8bf64c45a0c306ff2541f5e6

# Sofia Health

Sofia Health is a Django-based web application for managing healthcare appointments.

---

## 1. Create and Activate Virtual Environment (.venv)

### Create virtual environment
python -m venv .venv

### Activate on Windows
.venv\Scripts\activate

### Activate on macOS/Linux
source .venv/bin/activate

---

## 2. Install Dependencies

Make sure requirements.txt exists in the project root, then run:

pip install -r requirements.txt

---

## 3. Make Migrations

python manage.py makemigrations

---

## 4. Apply Migrations

python manage.py migrate

---

## 5. Run Development Server

python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

---

## (Optional) Deactivate Virtual Environment

deactivate

---

✅ Your Django project **Sofia Health** is now ready to use!


## About Stripe
Stripe is a service that lets websites and apps accept online payments safely (like cards, UPI, wallets, etc.).It makes payment integration easy for developers and handles security in the background.

### Stripe Integration in Project
Stripe is used in this project to handle online payments for booked appointments. 
When a user books an appointment, a payment intent is created using Stripe’s API, and the user is redirected to the payment page to complete the payment securely.

## URL Routes and Descriptions
/  
    – Home page of the application. Here you'll have a welcome message and Book Appointment button that leads you to book-          appointment page

/book-appointment/  
    – Page where the user is redirected to, to fill out the appointment booking form and click on Book & Pay button

/pay/<appointment_id>/  
    – Payment page for that particular appointment (identified by its ID). Enter card details and click on Pay button.

/create-payment/<appointment_id>/  
    – Backend endpoint to create a payment intent (e.g., for Stripe or any payment gateway).

/payment/result/  
    – Displays the result/status of the payment (success or failure).
