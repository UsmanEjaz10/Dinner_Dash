# Dinner Dash - Online Restaurant Ordering System

Dinner Dash is an online ordering system for a restaurant that allows customers to place orders and administrators to manage those orders efficiently.

## Features

### Unauthenticated Users

As an unauthenticated user, you can:

- Browse all available items on the menu.
- Filter items by category.
- Add items to your shopping cart.
- View your shopping cart.
- Remove items from your cart.
- Adjust the quantity of items in your cart.
- Log in (your cart items will persist).

### Authenticated Users (Non-Administrators)

Authenticated users have all the privileges of unauthenticated users, plus:

- Log out securely.
- Access a history of your past orders.
- View detailed information about each past order, including items ordered, order status, total price, order submission time, and timestamps for completed or canceled orders.
- If any item is retired from the menu, you can still access its description but cannot add it to a new cart.

### Administrators

As an authenticated administrator, you can:

- Create new item listings, providing a name, description, price, and uploading a photo.
- Modify existing items, including their name, description, price, and photo.
- Create named categories for items (e.g., "Small Plates").
- Assign items to one or more categories or remove them from categories.
- Retire items from the menu, hiding them from non-administrator users.
- Access an order "dashboard" to manage orders efficiently:
    - View a listing of all orders, categorized by status (ordered, paid, canceled, completed).
    - Access individual order details, including order date, purchaser's information, item details, total order price, and order status.
    - Transition orders to different statuses, including canceling, marking as paid, and marking as completed.

## Data Validity

Data validity is crucial in the system:

### Item

- An item must have a title, description, and price.
- An item must belong to at least one category.
- The title and description cannot be empty strings.
- The title must be unique among all items.
- The price must be a valid decimal numeric value greater than zero.
- The photo is optional, and a stand-in photo is used if not provided.

### User

- A user must have a valid, unique email address.
- A user must have a non-blank full name.
- An optional display name, if provided, must be between 2 and 32 characters long.

### Order

- An order must be associated with a user.
- An order must contain one or more items currently available on the menu.

## Getting Started

Follow these instructions to get your Dinner Dash project up and running on your local machine.

### Prerequisites 

- Python (version 3.10.11)
- Django (version 4.1.7)
- sqlparse==0.4.3
- virtualenv==20.24.2


### Installation 

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/dinner-dash.git

2. Navigate to project directory

   ```bash
   cd dinner-dash

3. Install dependencies from requirements.txt

   ```bash
   pip install -r requirements.txt

4. Migrate

   ```bash
   python manage.py migrate

### Running Server

1. Run project:

   ```bash
   python manage.py runserver

(You can access the application in you local host server)

## Lincense
[None]

## Signoff
[Usman Ejaz]
