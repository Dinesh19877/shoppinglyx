
# **E-commerce System**

This is a Django-based web application that features product management, user authentication, a shopping cart system, and payment processing. The project is built using Django for the backend, and HTML, CSS, JavaScript, and jQuery for the frontend.

## **Features**

- **User Authentication**: Secure login and registration system.
- **Product Management**: Add, update, delete, and manage products.
- **Add to Cart**: Add products to the cart and dynamically update the cart.
- **Payment Processing**: Simple payment system to handle transactions.
- **Invoice Generation**: Generates a receipt after successful payment.

## **Technologies Used**

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript, jQuery
- **Database**: SQLite (default with Django)

---

## **Installation Instructions**

### 1. **Clone the repository**
First, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Dinesh19877/shoppinglyx
```


### 2. **Create a Virtual Environment**

Set up a virtual environment for Python dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```



### 3. **Set up the Database**

Apply migrations to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. **Create a Superuser (for Admin access)**

Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

### 5. **Run the Development Server**

Start the Django development server to run the application locally:

```bash
python manage.py runserver
```

Now open your browser and go to `http://127.0.0.1:8000/` to view the application.

---

## **How to Use the Application**

1. **Login or Register** as a user.
2. **Add Products** to the inventory using the product management system.
3. **Scan barcodes** or manually add products to your shopping cart.
4. **View the cart** and update the quantity or remove items.
5. **Proceed to checkout** and complete the payment.
6. **Download/Print the receipt** after a successful transaction.

---

## **Contributing**

Feel free to fork this repository and make changes. Contributions are welcome!

---

## **License**

This project is licensed under the MIT License.

---

