### A Django e-commerce project

### Features
- user authentication
- cart session management (no login required)
- cart functionality
- add a new project
- checkout with stripe

### Technologies
- Python 3.11.2
- Django
- Stripe
- Bootstrap
- HTML
- CSS

### Installation
- Create stripe account
- Get the secret and public keys
- Create a .env file in the root directory
- Add the keys to the .env file as STRIPE_KEY=your_stripe_public key
- e.g. STRIPE_KEY=pk_test_51J
- Clone the repository
- Create a virtual environment

  ```bash
    python3 -m venv venv
  ````
- Install the requirements
    
    ```bash
    pip install -r requirements.txt
    ```

- Make migrations
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
- Create a superuser
    ```bash
    python manage.py createsuperuser
    ```
  
- Run the server
    ```bash
    python manage.py runserver
    ```
- Add a new product
- Checkout with stripe
- Done!
