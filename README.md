# Portfolio_App

This is a simple Portfolio Website project built with Django.

## Topics

- Setting up Development Environment.
- Starting up the project.
- Adding Pages App
  - Creating a View.
  - Adding a Route.
  - aAdding Bootstrap to the App
- Adding The Projects App
  - Defininf a Model
  - Using of Django Shell
  - Creating Views
  - Creating/Crafting the templates.
  - Adding Routes
  - Leveraging use of the Django Admin Site
  - Upload Images

## Installation

To run this project locally on your machine, follow these steps:

- Clone the repository to your local machine:

        git@github.com:Musyoki-Wambua/Portfolio_App.git

        cd Portfolio_App

- Create a virtual environment (optional but recommended) to isolate project dependencies:

        python -m venv venv

- Activate the virtual environment:

        source venv/bin/activate

- Apply database migrations:

        python manage.py migrate

- Create a superuser for the Django admin site:

        python manage.py createsuperuser

Follow the prompts to set up your admin account.

## Usage

    Start the development server:

        python manage.py runserver

Access the development server at [http://localhost:8000/](http://localhost:8000/) in your web browser to view your portfolio website.

Access the admin site at [http://localhost:8000/](http://localhost:8000/) to manage your application's data using the superuser credentials you created earlier.

## LICENSE

This repository is distributed under the ISC License

## Author

This repository is maintained by: [Joseph Wambua](https://github.com/Musyoki-Wambua)
