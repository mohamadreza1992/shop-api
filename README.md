# Shop API

A RESTful e-commerce backend API built with FastAPI and PostgreSQL.

This project implements a complete shopping workflow including authentication, products, categories, cart, orders, and payments.

---

# Features

## Authentication

* User registration
* User login with JWT
* Password hashing
* Current user profile
* Role-based authorization
* Admin protected routes

## Products

* Create products
* Update products
* Delete products
* Product listing
* Pagination
* Search
* Category filtering
* Price filtering

## Categories

* Create categories
* List categories
* Get category details
* Delete categories

## Shopping Cart

* Create user cart
* Add items
* Update quantity
* Remove items
* View cart

## Orders

* Create order from cart
* View user orders
* Get order details
* Order status management

## Payments

* Create payment
* Payment status handling
* Update order after payment

---

# Tech Stack

* Python 3.12
* FastAPI
* SQLAlchemy 2.0
* PostgreSQL 16
* Alembic
* Pydantic v2
* JWT Authentication
* Pytest
* Docker
* Docker Compose

---

# Project Structure

```
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

alembic/
docker-compose.yml
Dockerfile
```

---

# Running With Docker (Recommended)

Make sure Docker is installed.

Clone repository:

```bash
git clone <repository-url>
```

Create environment file:

```bash
cp .env.example .env
```

Configure your database and application settings inside `.env`.

Build and start containers:

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up -d
```

The API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

# Docker Commands

Stop containers:

```bash
docker compose down
```

Stop and remove database volume:

```bash
docker compose down -v
```

View running containers:

```bash
docker ps
```

View logs:

```bash
docker compose logs
```

---

# Environment Variables

Create `.env` file:

```
DATABASE_URL=postgresql://username:password@postgres:5432/shop

TEST_DATABASE_URL=postgresql://username:password@postgres:5432/shop_test_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Database Migration

Run migrations:

```bash
docker compose exec api alembic upgrade head
```

---

# Local Installation (Without Docker)

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
uvicorn app.main:app --reload
```

---

# Testing

Run tests inside Docker:

```bash
docker compose exec api pytest
```

Run locally:

```bash
pytest
```

Current status:

```
25 tests passed
```

---

# Architecture

This project follows a layered architecture:

```
Router
   |
Service
   |
Model
   |
Database
```

### Router

Handles HTTP requests and responses.

### Service

Contains business logic and application rules.

### Model

Represents database tables.

### Schema

Handles request validation and response serialization.

---

# Database Design

```
User
 |
Cart
 |
CartItem
 |
Product
```

```
User
 |
Order
 |
OrderItem
 |
Payment
```

---

# API Workflow

```
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
```

---

# About This Project

This is my first backend project built with FastAPI.

Through this project, I practiced building a real-world backend system including:

* REST API design
* Database modeling
* Authentication and authorization
* Business logic implementation
* Automated testing
* Docker-based development workflow

The main goal of this project was to understand backend engineering concepts by building a complete application from the ground up.

This project is the beginning of my backend development journey, and I will continue improving my skills by building more advanced systems and exploring production-level practices.

---

## Author

Mohamadreza Khosh Niat

Backend Developer | Python | FastAPI

GitHub: https://github.com/mohamadreza1992 
LinkedIn: https://www.linkedin.com/in/mohamadreza-khosh-niat-91b964366/