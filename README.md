# Shop API

A RESTful e-commerce backend API built with FastAPI and PostgreSQL.

This project implements a complete shopping workflow including authentication, products, categories, cart, orders, and payments.

---

## Features

### Authentication
- User registration
- User login with JWT
- Password hashing
- Current user profile
- Role based authorization
- Admin protected routes

### Products
- Create products
- Update products
- Delete products
- Product listing
- Pagination
- Search
- Category filtering
- Price filtering

### Categories
- Create categories
- List categories
- Get category details
- Delete categories

### Shopping Cart
- Create user cart
- Add items
- Update quantity
- Remove items
- View cart

### Orders
- Create order from cart
- View user orders
- Get order details
- Order status management

### Payments
- Create payment
- Payment status handling
- Update order after payment

---

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- Pydantic v2
- JWT Authentication
- Pytest

---

## Project Structure

    app/
    ├── core/
    ├── database/
    ├── dependencies/
    ├── models/
    ├── schemas/
    ├── services/
    ├── routers/
    └── main.py

    tests/

---

## Installation

Clone repository:

    git clone <repository-url>

Create virtual environment:

    python -m venv .venv

Activate:

Linux:

    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

---

## Environment Variables

Create `.env` file:

    DATABASE_URL=postgresql://username:password@localhost/shop

    TEST_DATABASE_URL=postgresql://username:password@localhost/shop_test_db

    SECRET_KEY=your_secret_key

    ALGORITHM=HS256

    ACCESS_TOKEN_EXPIRE_MINUTES=30

---

## Database Migration

Run:

    alembic upgrade head

---

## Run Application

Start server:

    uvicorn app.main:app --reload

Swagger documentation:

    http://localhost:8000/docs

---

## Testing

Run tests:

    pytest

Run coverage:

    pytest --cov=app

Current status:

    25 tests passed
    90% coverage

---

## Architecture

This project uses layered architecture:

    Router
       |
       |
    Service
       |
       |
    Model
       |
       |
    Database


Router:
Handles HTTP requests and responses.

Service:
Contains business logic.

Model:
Represents database tables.

Schema:
Validates input and output data.

---

## Database Design

    User
      |
      |
    Cart
      |
      |
    CartItem
      |
      |
    Product


    User
      |
      |
    Order
      |
      |
    OrderItem
      |
      |
    Payment


---

## API Workflow

    Register
       |
    Login
       |
    Browse Products
       |
    Add To Cart
       |
    Create Order
       |
    Payment
       |
    Completed Purchase

---

## About This Project

This is my first backend project built with FastAPI.

Through this project, I practiced designing a real-world backend architecture, working with databases, authentication, authorization, testing, and building complete business workflows.

During development, I used different learning resources and tools to improve my understanding and solve problems. My goal was not only to complete the project, but also to understand the concepts behind each part and improve my backend engineering skills.

This project represents the beginning of my backend development journey, and I look forward to building more advanced systems and improving my skills in future projects.

---

## Author

Backend Developer