# Shop API

A production-oriented RESTful e-commerce backend API built with **FastAPI**, **PostgreSQL**, and **Docker**.

This project provides a complete shopping workflow with authentication, product management, shopping cart, order processing, and payment handling.

The goal of this project was to design and implement a scalable backend architecture following clean separation of responsibilities and real-world development practices.

---

# Features

## Authentication & Authorization

* User registration and login
* JWT-based authentication
* Secure password hashing
* User profile management
* Role-based authorization
* Protected admin routes

## Product Management

* Create, update, and delete products
* Product listing
* Pagination
* Search functionality
* Category filtering
* Price filtering

## Category Management

* Create categories
* List categories
* Category details
* Category deletion

## Shopping Cart

* Create user carts
* Add products to cart
* Update item quantities
* Remove cart items
* View cart summary

## Order Management

* Create orders from cart items
* View user orders
* Order details
* Order status management

## Payment System

* Create payments
* Track payment status
* Update order status after payment

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

# Project Architecture

The project follows a layered architecture:

```
                Client

                  |
                  |

               Router

                  |

               Service

                  |

                Model

                  |

              Database
```

### Router Layer

Responsible for handling HTTP requests, validation, and responses.

### Service Layer

Contains business logic and application rules.

### Model Layer

Defines database entities and relationships.

### Schema Layer

Handles data validation and serialization.

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

Dockerfile

docker-compose.yml
```

---

# Running With Docker

Clone the repository:

```bash
git clone <repository-url>
```

Create environment file:

```bash
cp .env.example .env
```

Start the application:

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up -d
```

API:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

# Environment Configuration

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@postgres:5432/shop

TEST_DATABASE_URL=postgresql://username:password@postgres:5432/shop_test_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Database Migration

Apply migrations:

```bash
docker compose exec api alembic upgrade head
```

---

# Testing

Run tests:

```bash
docker compose exec api pytest
```

Current test status:

```
25 tests passed
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

# Database Relationships

```
User
 |
 +---- Cart
 |       |
 |       +---- CartItem
 |                |
 |                +---- Product
 |
 +---- Order
         |
         +---- OrderItem
                  |
                  +---- Product

Order
 |
 Payment
```

---

# Security

Implemented security features:

* JWT authentication
* Password hashing
* Protected routes
* Role-based permissions
* Environment-based configuration

---

# Future Improvements

Planned improvements:

* Redis caching
* Background tasks
* CI/CD pipeline
* API versioning
* Rate limiting
* Production deployment
* Monitoring and logging

---

# About

This project was built to practice backend engineering concepts by creating a complete e-commerce system.

Through this project, I gained practical experience with:

* REST API design
* Database modeling
* Authentication and authorization
* Business logic implementation
* Automated testing
* Docker-based development workflow

---

## Author

**Mohamadreza Khosh Niat**

Backend Developer | Python | FastAPI

GitHub:
https://github.com/mohamadreza1992

LinkedIn:
https://www.linkedin.com/in/mohamadreza-khosh-niat-91b964366/
