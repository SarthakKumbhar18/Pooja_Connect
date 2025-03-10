# Pooja_Connect

Pooja Connect is a **Django-based** web application that helps users find local **Pandits** for performing poojas. Users can book a Pandit, manage their bookings, and Pandits can accept or reject booking requests. The system includes authentication, booking management, and profile updates.

## Features

### Users
- Register/Login
- Create a **Booking** (Fields: Name, Address, Day, Work)
- View, **Update, and Delete** their bookings

### Pandits
- Register/Login
- View all **Booking Requests**
- Accept/Cancel a booking **(with a message to the user)**
- Delete a booking
- Update their profile

## Project Structure

```
PoojaConnect/
│── poojaconnect/         # Project settings
│── pandits/              # Pandits App
│── users/                # Users App
│── bookings/             # Bookings App
│── templates/            # HTML Templates
│── static/               # CSS, JavaScript, Images
│── db.sqlite3            # Database
│── manage.py             # Django Management Script
```

## Installation

### 1. Clone the repository
```sh
git clone https://github.com/yourusername/pooja-connect.git
cd pooja-connect
```

### 2. Create a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Run database migrations
```sh
python manage.py migrate
```

### 5. Create a superuser
```sh
python manage.py createsuperuser
```

### 6. Run the server
```sh
python manage.py runserver
```

Now visit **http://127.0.0.1:8000/** in your browser.

## Models

### **Pandit Model**
```python
class Pandit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    experience = models.IntegerField()
    location = models.CharField(max_length=255)
    specializations = models.TextField()
    image = models.ImageField(upload_to='pandits/')
```

### **Booking Model**
```python
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pandit = models.ForeignKey(Pandit, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    day = models.DateField()
    work = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled')], default='Pending')
    message = models.TextField(blank=True)
```

## URLs
```python
urlpatterns = [
    path('create_booking/', views.create_booking, name='create_booking'),
    path('user_bookings/', views.user_bookings, name='user_bookings'),
    path('update_booking/<int:pk>/', views.update_booking, name='update_booking'),
    path('delete_booking/<int:pk>/', views.delete_booking, name='delete_booking'),
    path('pandit_bookings/', views.pandit_bookings, name='pandit_bookings'),
    path('update_booking_status/<int:pk>/', views.update_booking_status, name='update_booking_status'),
    path('update_pandit_profile/', views.update_pandit_profile, name='update_pandit_profile'),
]
```

## Tech Stack
- **Backend:** Django, Mysql
- **Frontend:** HTML, CSS, Bootstrap
- **Authentication:** Django Authentication

## Future Enhancements
- Add **payment gateway** for bookings
- Implement **real-time notifications** for Pandits
- Improve **UI with React or Vue.js**

## License
This project is licensed under the **MIT License**.

---

### **Contributions**
Feel free to fork this repository, raise issues, and submit pull requests.

---

🚀 **Pooja Connect – Find the right Pandit for your spiritual needs!** 🙏
