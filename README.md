[![wakatime](https://wakatime.com/badge/user/bdc21cbc-aa7c-4598-8214-34428f55f625/project/018d5f0c-c576-46e1-9304-efbb926e54d4.svg)](https://wakatime.com/badge/user/bdc21cbc-aa7c-4598-8214-34428f55f625/project/018d5f0c-c576-46e1-9304-efbb926e54d4)
[![wakatime](https://wakatime.com/badge/github/sjtgs/Health-Record-System.svg)](https://wakatime.com/badge/github/sjtgs/Health-Record-System)

# Health-Record-System

The Health Record System is a user-friendly digital platform that efficiently manages patient data and facilitates the scheduling of appointments for cancer treatment. This system enables the seamless recording of patient information, including medical history and relevant details. Doctors can easily access and review this data, empowering them to set appointments and provide timely, personalized care for their patients undergoing cancer treatment. Open Source Project.

![alt text](<health_system/images/Health Record SyStem Dashboard - Login.png>)
<br>
![alt text](<health_system/images/Health Record SyStem Dashboard - Administrator.png>)
<br>
![alt text](<health_system/images/Health Record SyStem Dashboard - Visual.png>)
<br>
![alt text](<health_system/images/Health Record SyStem Dashboard - Doctor Form.png>)
<br>
![alt text](<health_system/images/Unauthorized Health Record SyStem Dashboard.png>)

## Text Based - Flow Chart

```

    Start:
        System initialization and login.

    Dashboard:
        Display key metrics and notifications.

    Patient Records:
        Choose "Patient Records" option.
        Enter or search for a patient's information.

    Data Entry:
        Record or update patient data using user-friendly forms.

    Appointment Management:
        Navigate to "Appointment Scheduler."
        Set, reschedule, or cancel appointments.

    Data Viewing:
        Access "View Records" for reviewing patient history and details.

    Security Check:
        Verify user authentication.

    Notification System:
        Automated reminders for upcoming appointments.

    End:
        Logout or exit the system.

```

## Setup Health Record SyStem

#### Python 2

```
~$ python -m venv healthvenv
```

#### Python 3

```
~$ python3 -m venv healthvenv
```

### Activate the Virtual Enviroment

#### Windows

```
~$ healthvenv\Scripts\activate
```

#### Linux and OS X

```
source healthvenv/bin/activate
```

### Installing Health System Record Requirements

```
(healthvenv) ~$ python -m pip install --upgrade pippython -m pip install --upgrade pip
```

```
(healthvenv) ~$ python -m pip install -r requirements.txt
```

## Running the Health Record System application

This command runs the Django Web Application .

```
(healthvenv) ~/health_system$ python manage.py runserver   
```

## Migrate Health Record System

This command runs database migrations to ensure your database schema is up to date.

```
(healthvenv) ~/health_system$ python manage.py migrate 
```

## Create Dummy User  - Administrator , Doctor , Nurse and Patient

This command will create dummy users for each user type (Administrator, Doctor, Nurse, and Patient) along with appropriate group assignments. Adjust the logic and number of users as per your requirements

```
(healthvenv) ~/health_system$ python manage.py create_dummy_users
```

### Administration App

The Dashboard application serves as a centralized platform for healthcare administration, providing comprehensive insights into patient records, appointments, and review schedules. Built on Django, it offers administrators a user-friendly interface to monitor and manage various aspects of patient care, facilitating informed decision-making and streamlined operations. From patient records to appointment scheduling and review dates, the Dashboard ensures efficient management of healthcare services, optimizing overall performance and enhancing patient outcomes.

### Doctor App

The Doctor App, developed with Django, facilitates the management of doctor profiles, encompassing personal details, contact information, medical qualifications, and specialization. It incorporates robust user authentication to ensure secure access to doctor records. Additionally, the app enables doctors to view patient records, including medical histories, diagnoses, treatment plans, and prescriptions, facilitating informed decision-making in patient care. With features for appointment scheduling and patient referrals, the Doctor App streamlines administrative tasks and fosters efficient healthcare delivery.

### Nurse  App

The Nurse App, built on Django, streamlines the management of nurse profiles, encompassing personal details, contact information, medical qualifications, and specialization. It integrates robust user authentication to ensure secure access to nurse records. Additionally, the app empowers nurses to access patient records, including medical histories, diagnoses, treatment plans, and prescriptions, facilitating informed decision-making in patient care. With features for appointment scheduling and patient referrals, the Nurse App simplifies administrative tasks and fosters efficient healthcare delivery.

### Patient App

The Patient App is a Django application designed to manage patient information within a healthcare system. It includes models, views, and templates to facilitate the creation, retrieval, updating, and deletion of patient records. The app allows healthcare providers to store detailed information about patients, such as personal details, medical history, diagnoses, treatments, insurance information, and contact details. Additionally, it supports user authentication and authorization, ensuring that only authorized users can access and modify patient records. The Patient App aims to streamline the management of patient data, enhance communication between healthcare professionals, and improve the overall efficiency of healthcare services.

## Health Record SyStem - URLS

[1]: Administrator  - <http://127.0.0.1:8000/administrator/admin-dashboard/>
<br>
[1.1] Administrator / Doctor - <http://127.0.0.1:8000/administrator/doctor-form/>
<br>
[1.2] Administrator / Nurse - <http://127.0.0.1:8000/administrator/nurse-form/>
<br>
[1.3] Administrator / Patient - <http://127.0.0.1:8000/administrator/patient-form/>
<br>
[2]: Doctor / Doctor Lists - <http://127.0.0.1:8000/doctor/doctor-lists/>  
<br>
[3]: Doctor / Patient Lists - <http://127.0.0.1:8000/doctor/patient-lists/>
<br>
[4]: Doctor / Nurse Lists -  <http://127.0.0.1:8000/doctor/nurse-lists/>
<br>
[5]: Nurse / Nurse Lists - <http://127.0.0.1:8000/nurse/nurse-lists/>
<br>
[6]: Nurse / Patient Lists - <http://127.0.0.1:8000/nurse/patient-lists/>
<br>
[7]: API - Doctor / Lists - <http://127.0.0.1:8000/api/doctors/doctors/>
<br>
[8]: API - Nurse /  Lists - <http://127.0.0.1:8000/api/nurses/nurses/>
<br>
[9]: API - Patient / Lists - <http://127.0.0.1:8000/api/patients/patients/>
<br>
[10]: Doctor / Form - <http://127.0.0.1:8000/doctor/doctor-form/>
<br>
[11]: Doctor / Form Edit - <http://127.0.0.1:8000/doctor/><int:auto_id>/doctor-form-edit/
<br>
[12]: Nurse / Form - <http://127.0.0.1:8000/nurse/nurse-form/>
<br>
[13]: Nurse / Form Edit - <http://127.0.0.1:8000/nurse/><int:auto_id>/nurse-form-edit/
<br>
[14]: Patient / Form - <http://127.0.0.1:8000/Patient/patient-form/>
<br>
[15]: Patient / Form Edit - <http://127.0.0.1:8000/patient/><int:auto_id>/patient-form-edit/
