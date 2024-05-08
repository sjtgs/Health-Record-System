
[![wakatime](https://wakatime.com/badge/github/sjtgs/Health-Record-System.svg)](https://wakatime.com/badge/github/sjtgs/Health-Record-System)

# Health-Record-System

The Health Record System is a user-friendly digital platform that efficiently manages patient data and facilitates the scheduling of appointments for cancer treatment. This system enables the seamless recording of patient information, including medical history and relevant details. Doctors can easily access and review this data, empowering them to set appointments and provide timely, personalized care for their patients undergoing cancer treatment. Open Source Project.

![alt text](<health_system/images/Health Record SyStem - Home Page.png>)
<br>

![alt text](<health_system/images/Health Record SyStem Dashboard - Login.png>)
<br>

![alt text](<health_system/images/Health Record SyStem Dashboard - Administrator.png>)
<br>

![alt text](<health_system/images/Health Record SyStem Dashboard - Visual.png>)
<br>

![alt text](<health_system/images/Health Record SyStem Dashboard - Doctor Form.png>)
<br>

![alt text](<health_system/images/Health Record SyStem Dashboard - Doctor Detail.png>)
<br>

![alt text](<health_system/images/Health Record SyStem Dashboard - Nurse Detail.png>)
<br>

![alt text](<health_system/images/Unauthorized Health Record SyStem Dashboard.png>)

## Text Based - Flow Chart

```

  Start:
    System initialization and login.

Administrator:
    Access administrator dashboard.
    Manage doctor, nurse, and patient records.
    Schedule appointments.
    View system-wide metrics and notifications.

Doctor:
    Access doctor dashboard.
    View patient records.
    Update patient information.
    Schedule appointments.
    Receive notifications for upcoming appointments.

Nurse:
    Access nurse dashboard.
    View patient records.
    Update patient information.
    Schedule appointments.
    Receive notifications for upcoming appointments.

Patient:
    Access patient dashboard.
    View personal health records.
    Schedule appointments.
    Receive notifications for upcoming appointments.

End:
    Logout or exit the system.


```

## Features

- User authentication: Allows users to register, log in, and log out securely.
- CRUD operations: Enables medical personnel to create, read, update, and delete patient records.
- Interactive charts: Provides visual representation of data using Chart.js library.
- Map integration: Utilizes Django Leaflet to display pharmacy locations on interactive maps.
- Management commands: Includes management commands to generate dummy data for testing purposes.
- Cross-platform compatibility: Build script automatically creates and activates a virtual environment based on the operating system (Windows, macOS, or Linux).
- User Creation Logs: Check the User Creation Logs for the Administrator , Doctor , Nurse and Patient

## Setup and Installation Health Record SyStem

1. Clone the repository:

   ```
   git clone https://github.com/sjtgs/Health-Record-System.git
   ```

2. Navigate to the project directory:

```
cd health-record-system
```

3. Run the build script to create and activate the virtual environment:

macOS/Linux:

```
./build.sh
```

Windows:

```
build.bat
```

4. Migrate Health Record System

This command runs database migrations to ensure your database schema is up to date.

```
(healthvenv) ~/health_system$ python manage.py migrate 
```

5. Create Dummy User  - Administrator , Doctor , Nurse and Patient

This command will create dummy users for each user type (Administrator, Doctor, Nurse, and Patient) along with appropriate group assignments. Adjust the logic and number of users as per your requirements

```
(healthvenv) ~/health_system$ python manage.py create_dummy_users
```

6. Running the Health Record System application

This command runs the Django Web Application . Access the application in your web browser :

| Link Description | URL |
|------------------|-----|
| Home Page    | [Home Page](http://127.0.0.1:8000) |

```
(healthvenv) ~/health_system$ python manage.py runserver   
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

| Link Description | URL |
|------------------|-----|
| Home Page    | [Home Page](http://127.0.0.1:8000) |
| Administrator    | [Administrator](http://127.0.0.1:8000/administrator/admin-dashboard/) |
| Administrator / Doctor | [Administrator / Doctor](http://127.0.0.1:8000/administrator/doctor-form/) |
| Administrator / Nurse | [Administrator / Nurse](http://127.0.0.1:8000/administrator/nurse-form/) |
| Administrator / Patient | [Administrator / Patient](http://127.0.0.1:8000/administrator/patient-form/) |
| Doctor / Doctor Lists | [Doctor / Doctor Lists](http://127.0.0.1:8000/doctor/doctor-lists/) |
| Doctor / Patient Lists | [Doctor / Patient Lists](http://127.0.0.1:8000/doctor/patient-lists/) |
| Doctor / Nurse Lists | [Doctor / Nurse Lists](http://127.0.0.1:8000/doctor/nurse-lists/) |
| Nurse / Nurse Lists | [Nurse / Nurse Lists](http://127.0.0.1:8000/nurse/nurse-lists/) |
| Nurse / Patient Lists | [Nurse / Patient Lists](http://127.0.0.1:8000/nurse/patient-lists/) |
| API - Doctor / Lists | [API - Doctor / Lists](http://127.0.0.1:8000/api/doctors/doctors/) |
| API - Nurse / Lists | [API - Nurse / Lists](http://127.0.0.1:8000/api/nurses/nurses/) |
| API - Patient / Lists | [API - Patient / Lists](http://127.0.0.1:8000/api/patients/patients/) |
| Doctor / Form | [Doctor / Form](http://127.0.0.1:8000/doctor/doctor-form/) |
| Doctor / Form Edit | [Doctor / Form Edit](http://127.0.0.1:8000/doctor/int:auto_id/doctor-form-edit/) |
| Nurse / Form | [Nurse / Form](http://127.0.0.1:8000/nurse/nurse-form/) |
| Nurse / Form Edit | [Nurse / Form Edit](http://127.0.0.1:8000/nurse/int:auto_id/nurse-form-edit/) |
| Patient / Form | [Patient / Form](http://127.0.0.1:8000/Patient/patient-form/) |
| Patient / Form Edit | [Patient / Form Edit](http://127.0.0.1:8000/patient/int:auto_id/patient-form-edit/) |

### Usage

    1. Log in as an administrator to manage medical personnel, patient records, and pharmacy locations.
    2. Log in as a doctor, nurse, or patient to view and manage relevant data.
    3. Explore interactive charts to visualize medical statistics.
    4. Use the map feature to locate nearby pharmacies.

### Contributing

    1.Fork the repository and create your branch from main.
    2. Make your changes and ensure that the code follows PEP 8 guidelines.
    3. Write tests for your changes, if applicable.
    4. Ensure all tests pass by running python manage.py test.
    4. Commit your changes with descriptive commit messages.
    5. Push your changes to your fork and submit a pull request.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
