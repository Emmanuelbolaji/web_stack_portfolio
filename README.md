OJA - E-Commerce Web Application
Overview
OJA is a dynamic e-commerce web application built with Django, providing a platform for users to buy and sell items in a smooth and user-friendly environment. The application incorporates essential features like user authentication, item listing, category filtering, and messaging functionality.
Features

User Authentication

Sign up, log in, and manage accounts
Secure user data management
Role-based access control


Item Management

Display products for sale with images, descriptions, and pricing
Category-based filtering
Advanced search functionality by name or category
Intuitive item listing interface


Responsive Design

Optimized for both mobile and desktop devices
Fluid and adaptive layout
Seamless user experience across all devices


Messaging System

Real-time conversation capabilities
Message threading for item-specific discussions
Inbox management features



Project Structure
Copyoja/
├── core/                   # Core functionality
│   └── templates/
│       └── base.html      # Main template
│       └── login.html     # Authentication templates
│       └── signup.html
├── dashboard/             # User dashboard
│   └── templates/
│       └── index.html     # Dashboard overview
├── conversation/          # Messaging system
│   ├── models.py         # Conversation models
│   ├── views.py          # Conversation logic
│   └── urls.py           # URL routing
├── item/                 # Product management
│   ├── models.py         # Item/category models
│   ├── views.py          # Item-related views
│   └── templates/
│       ├── items.html    # Item listing
│       ├── detail.html   # Item details
│       └── form.html     # Item creation/editing
├── media/                # Media storage
│   └── item_images/      # Product images
├── manage.py             # Django CLI
├── db.sqlite3            # Database
├── settings.py           # Project settings
├── urls.py               # Main URL routing
├── wsgi.py              # WSGI configuration
└── asgi.py              # ASGI configuration
Prerequisites

Python 3.9 or higher
pip package manager
Virtual environment (recommended)

Installation

Clone the repository:

bashCopygit clone https://github.com/Emmanuelbolaji/web_stack_portfolio.git
cd web_stack_portfolio

For Users

Browse Items

Navigate through categories
Use filters to refine search
View detailed item information


Search Items

Use the search bar for specific items
Filter by category or price range
Sort results by various criteria


Send Messages

Contact sellers directly
Manage conversations in inbox


For Administrators

User Management

Manage user accounts
Monitor user activity


Item Management

Review listed items
Manage categories
Handle reported items


System Monitoring

View conversation logs
Monitor system performance
Manage site settings


Technologies Used

Backend Framework: Django
Frontend:

HTML/CSS
Tailwind CSS
JavaScript


Database: SQLite
Development Tools:

Git for version control
VSCode (recommended editor)


Developer: Emmanuel Bolaji
Project Link: https://github.com/Emmanuelbolaji/web_stack_portfolio
