
<h1>Email Notification System</h1>
A Web Application designed for sending and scheduling Emails. Once created an account, you can send mails, add attachment files, schedule mail to multiple recipients.

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Objectives](#objectives)
- [Objectives completed](#objectives-completed)
- [Usage](#usage)
  - [Installation](#installation)
  - [Navigation](#navigation)
- [Team](#team)
  - [Mentors:](#mentors)
  - [Members:](#members)

## Objectives
* Send Emails
* Sned Scheduled Emails
* Send Bulk Scheduled Emails

## Objectives completed 
  1. Send Emails
  2. Send Bulk Emails

## TODO
  1. Schedule Emails.
  2. Add Edit/Delete Emails before Scheduled time.
  3. Grouped Scheduling. 

## Usage

### Installation 

Pre-requisites:

- [Python Environment along with PIP](https://www.python.org/downloads/)
- [PostgreSQL Database](https://www.postgresql.org/download/)


<details>
    <summary><b>Windows</b></summary>

   1. Clone the repository
   2. Setup PostgreSQL Database with name `EMNS`, user as `postgres`.
   3. Password of the database if already there, then write the password in the [](src\EMNS\settings.py)
   4. Setup the Virtual Environment:

- Python should be installed along with pip. 

`pip install virtualenv`

`virtualenv env`

 `env\Scripts\activate`

This should set up the virtual environment on your local folder.

`pip install -r requirements.txt`

This will install all the required dependencies and libraries in python

Make migrations for the database:

`python manage.py makemigrations`

`pyton manage.py migrate`

Finally run the server `python manage.py runserver`


</details>

<details>
    <summary><b>Linux</b></summary>

   1. Clone the repository
   2. Setup PostgreSQL Database with name `EMNS`, user as `postgres`.
   3. Password of the database if already there, then write the password in the [](src\EMNS\settings.py)
   4. Setup the Virtual Environment:

- Python should be installed along with pip. 

`pip install virtualenv`

`virtualenv env`

 `source env/bin/activate`

This should set up the virtual environment on your local folder.

`pip install -r requirements.txt`

This will install all the required dependencies and libraries in python

Make migrations for the database:

`python manage.py makemigrations`

`pyton manage.py migrate`

Finally run the server `python manage.py runserver`

</details>

<details>
    <summary><b>macOS</b></summary>

   1. Clone the repository
   2. Setup PostgreSQL Database with name `EMNS`, user as `postgres`.
   3. Password of the database if already there, then write the password in the [](src\EMNS\settings.py)
   4. Setup the Virtual Environment:

- Python should be installed along with pip. 

`pip install virtualenv`

`virtualenv env`

 `source env/bin/activate`

This should set up the virtual environment on your local folder.

`pip install -r requirements.txt`

This will install all the required dependencies and libraries in python

Make migrations for the database:

`python manage.py makemigrations`

`pyton manage.py migrate`

Finally run the server `python manage.py runserver`

</details>

###  Navigation

 - Sign Up 
 - Login
 - Send Emails
 - List of sent Emails

<details>
    <summary><b>Show instructions</b></summary>

   1. Make Admin account
 	
For creating admin, locate to the project folder src/ directory, activate the virtual environment:

- For Linux/macOS : `source env/bin/activate.sh`

- For Windows: `env\Script\activate` 

Create a super user using the command, `python manage.py createsuperuser`.

Add your credentials like email, name, password in there and there is the Admin created.

If this doesn't work, use `winpty python manage.py createsuperuser`.

Navigate to the `127.0.0.1:8000/admin/` and enter the same credentials as used for creating the admin.

   2. Google App Password
        
This should be a must for sending mails from this app, before creating a account, plaease create a app password on Google.

The sender's email must be a Gmail account.  The 2FA should be enabled on this account. You will have to create an app on your Gmail id that will handle the email sending, permissions, and the rest of the stuff for you. It's quite simple to do that, visit the [Google App Password page](https://myaccount.google.com/apppasswords). 

1. Log in with your credentials from the above link
2. Create an App  category-> Other give it any name(call it anything you like eg. djangomail, emns)
3. Now copy the password and store it securely somewhere.	

   3. Login
 
Creating Account with `Email`, `Username`, `Password` and `Google App Password`.

Once signed/logged in, that same email will be used for sending emails, it avoids spaming and mismatched email delivery. 
 

</details>


## Team

### Mentors:
Irfan Siddavatam ( irfansiddavatam@somaiya.edu )<br>
Ashwini Dalvi ( ashwinidalvi@somaiya.edu )

### Members:
| Sr No. | Name          | e-mail                    | git-profile    |
| ------ | ------------- | ------------------------- | -------------- |
| 1.     | Meet Gor      | gor.m@somaiya.edu         | Mr-Destructive |
| 2.     | Rohan Kumar   | rohan.kumar@somaiya.edu   | rohxn          |
| 3.     | Satvik Mishra | satvik.m@somaiya.edu      | Satvik049      |
| 4.     | Govind Patra  | patra.g@somaiya.edu       | Govind416      |
| 5.     | Hardik Singh  | hardik.singh1@somaiya.edu | HS-pro         |
| 6.     | Parth Jaju    | parth.jaju@somaiya.edu    | ParthJaju      |
