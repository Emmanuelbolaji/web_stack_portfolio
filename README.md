OJA - E-Commerce Web Application
OJA is a dynamic e-commerce web application built with Django, providing a platform for users to buy and sell items in a smooth and user-friendly environment. The application incorporates essential features like user authentication, item listing, category filtering, and messaging functionality.

Features
User Authentication: Sign up, log in, and manage accounts.
Item Listing: Display products for sale with images, descriptions, and pricing.
Category Filtering: Users can filter items by categories to streamline their browsing experience.
Search Functionality: Search for items by name or category.
Responsive Design: Optimized for both mobile and desktop devices with a responsive layout.
Messaging System: Allows users to send and receive messages within conversations related to the items.
Project Structure
oja/
core/: Contains the base templates, user authentication views (login, signup), and forms for user management.

base.html: The main template that is extended across the application.
login.html, signup.html: Templates for user login and registration.
dashboard/: The user's dashboard where they can manage their account and items.

index.html: Template displaying the user's dashboard overview.
conversation/: Implements the messaging system, allowing users to manage their conversations.

models.py: Defines the database models for the conversation and messages.
views.py: Handles views related to conversation interactions.
urls.py: URL configuration for the conversation module.
item/: Manages the items for sale.

models.py: Defines models for items, their categories, and their details.
views.py: Handles item listing, detail views, and item-related actions.
items.html: Template for listing items with a responsive layout for mobile and desktop views.
detail.html: Template for displaying individual item details.
form.html: Form template for creating and editing items.
media/: Stores uploaded media files, including item images.

item_images/: Contains all images related to the listed items.
Other Files
manage.py: Django project management script.
db.sqlite3: SQLite database containing all project data.
settings.py: Contains the configuration for the Django application.
urls.py: The root URL configuration of the Django project.
wsgi.py: WSGI configuration for deploying the application.
asgi.py: ASGI configuration for handling asynchronous connections.
Installation
To run this project locally, follow these steps:

Prerequisites
Make sure you have Python 3.x installed and pip is available.

Steps
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/oja.git
cd oja
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply database migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser (admin) to access the Django admin panel:

bash
Copy
Edit
python manage.py createsuperuser
Run the server:

bash
Copy
Edit
python manage.py runserver
Open your browser and navigate to:

bash
Copy
Edit
http://127.0.0.1:8000/
You can log in with the superuser credentials or sign up as a new user.

Usage
For Users:
Browse Items: Navigate through various categories and view items listed for sale.
Search Items: Use the search bar to find specific items.
Send Messages: Engage in conversations with sellers about items.
For Admins:
Manage Users: Approve or delete user accounts.
Manage Items: Add, edit, or delete items listed by users.
View Conversations: View and manage user conversations within the admin panel.
Technologies Used
Django: Web framework used to build the application.
HTML/CSS: For the layout and styling of the pages.
Tailwind CSS: Utility-first CSS framework for fast UI development.
SQLite: Database used to store user and item data.
JavaScript: For client-side interactivity (mobile/desktop view switching).
Contributing
Fork this repository.
Create a new branch (git checkout -b feature-name).
Make your changes.
Commit your changes (git commit -m 'Add feature').
Push to the branch (git push origin feature-name).
Create a new pull request.
