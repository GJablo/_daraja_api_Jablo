# Django Project with M-Pesa Daraja API Integration

## Overview

This is a Django project that integrates with the M-Pesa Daraja API to enable mobile payments, allows users to make payments directly from the website. The implementation includes a form where users input their phone number and amount, triggering a pop-up on their phone for PIN entry to complete the transaction.

## Features

- User form to enter phone number and amount

- Integration with M-Pesa Daraja API

## Prerequisites

`Python 3.X`
`Django`
`Requests library`
`M-Pesa Daraja API credentials`

- To get access of the credentials use

1. Register for credentials

- [Register for M-Pesa Daraja API credentials](https://developer.safaricom.co.ke/)
- Sign up for an account if you don't have one
- Login to access the dashboard

2. Create an App

- Go to the dashboard and click on "Create an App"
- Provide a name for your app (e.g., Django M-Pesa Integration).
- Select the APIs you want to use, such as:
- `M-Pesa Express` (Lipa Na M-Pesa Online Payment)
- Click "Create App" to proceed.

3. Get Your Credentials

- Once the app is created, you'll find your:
- Consumer key
- Consumer Secret
- Passkey

## Installation

1. Clone the repo Using

```bash
git clone https://github.com/GJablo/_daraja_api_Jablo.git
cd my_site
```

2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

## Usage

1. Open your code editor and navigate to the `settings.py` file located at my_site and add your M-Pesa Daraja API credentials
2. Scroll down to see the `MPESA_DARAJA` section and add your credentials (i.e ., `CONSUMER_KEY`, `CONSUMER_SECRET`, `PASSKEY`)
3. Apply migrations using

```bash
python manage.py migrate
```

4. Run the Django development server using

```bash
python manage.py runserver
```

5. Open your web browser and navigate to `http://localhost:8000/` to test the api
