# Health-Record-System
The Health Record System is a user-friendly digital platform that efficiently manages patient data and facilitates the scheduling of appointments for cancer treatment. This system enables the seamless recording of patient information, including medical history and relevant details. Doctors can easily access and review this data, empowering them to set appointments and provide timely, personalized care for their patients undergoing cancer treatment. Open Source Project 

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


##  Setup Virtual Enviroment:

#### Python 2:

```
> python -m venv healthvenv
```

#### Python 3:

```
> python3 -m venv healthvenv
```

## Activate the Virtual Enviroment 

### Windows
```
> myvenv\Scripts\activate
```

### Linux and OS X
```
$ source myvenv/bin/activate
```

## Installing Health System Record Requirements 

```
(healthvenv) ~$ python -m pip install --upgrade pippython -m pip install --upgrade pip
```

```
(healthvenv) ~$ python -m pip install -r requirements.txt
```


## Health Record System Application :
```
(healthvenv) ~$  health_system
```

## Running the Health Record System application :
```
(healthvenv) ~$  cd health_system
```

```
(healthvenv) ~/health_system$ python manage.py runserver   
```

## Migrate Health Record System
```
(healthvenv) ~/health_system$ python manage.py migrate 
```

## Create Doctor App 
```
(healthvenv) ~/health_system$ python manage.py startapp doctor_app
```

#### Migrate the Doctor App
```
(healthvenv) ~/health_system$ python manage.py makemigrations doctor_app
(healthvenv) ~/health_system$ python manage.py migrate doctor_app
```

## Create Patient App
```
(healthvenv) ~/health_system$ python manage.py startapp patient_app
```

#### Migrate the Patient App
```
(healthvenv) ~/health_system$ python manage.py makemigrations patient_app
(healthvenv) ~/health_system$ python manage.py makemigrations patient_app
```
