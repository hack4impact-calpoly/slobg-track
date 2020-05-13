# SLO Botanical Garden Volunteer Hour Tracker
[![Build Status](https://travis-ci.com/hack4impact-calpoly/slobg-track.svg?branch=master)](https://travis-ci.com/hack4impact-calpoly/slobg-track)
### A volunteer hour tracker made for the <a href="https://www.slobg.org/" target="_blank">SLO Botanical Garden nonprofit</a>.

![User View](https://github.com/eric-newcomer/slobg-track/blob/master/backend/slobg_proj/slobg_app/static/slobg_app/img/user-view.png)

## Table of Contents
- [Overview](#overview)
  - [Purpose](#purpose)
  - [Team](#team)
- [Getting Started for Developers](#getting-started-for-developers)
  - [Clone the repository](#clone-the-repository)
  - [Install Requirements](#install-requirements)
  - [Run the App](#run-the-app)

### Overview

#### Purpose
The purpose of this application was to improve the volunteer tracking process at the SLO Botanical Garden nonprofit. Previously, volunteer information was written down and manually inputted into spreadsheets by nonprofit supervisors. In order to streamline this arduous task, the team built a volunteer management system that allows volunteers to record their hours and view their volunteer history, all while allowing nonprofit supervisors to keep this information and filter/export it when necessary. 

#### Team
The SLO Botanical Garden project team consisted of 5 Cal Poly Computer Science students. Over the course of 8 months, they worked in collaboration to develop and deploy this web application. The team can be seen below:

<p float="left">
  <img src="https://avatars3.githubusercontent.com/u/42504462?s=460&u=fbe279fd5e77ba14a01b2679da9970e49f5a989e&v=4" width="150" />
  <img src="https://avatars1.githubusercontent.com/u/46923410?s=460&u=034ba878c94d529d6bfb445d77c978dc94d197a3&v=4" width="150" /> 
  <img src="https://avatars3.githubusercontent.com/u/20120289?s=460&u=3e6039d2391a2d7ee4e65743a2a366ed3efc16d5&v=4" width="150" />
  <img src="https://avatars0.githubusercontent.com/u/47136824?s=460&v=4" width="150" />
  <img src="https://avatars1.githubusercontent.com/u/15805074?s=460&v=4" width="150" />
</p>

(From left to right)
- Justin Poist - Software Developer
- Jack Fales - Software Developer
- Eric Newcomer - Engineering Manager/Software Developer
- Tim Kim - Software Developer
- Cole Perry - Software Developer

### Getting Started for Developers

#### Clone the repository
``` git clone https://github.com/hack4impact-calpoly/slobg-track.git ```
```cd slobg-track/``

#### Install requirements
0. [Install Python](https://www.python.org/downloads/) (if you don't have it for some reason)
1. Clone the repo
2. [Install pip](https://pip.pypa.io/en/stable/installing/)
3. [Install Django](https://docs.djangoproject.com/en/3.0/topics/install/)
4. Install all project packages using `pip install -r requirements.txt` (make sure you are in the project root folder).

#### Run the app
1. ```cd backend/slobg_proj/```
2. ```python manage.py runserver``` or ```python3 manage.py runserver``` depending on your Python version.
3. Head over to http://127.0.0.1:8000/ to see the app!

