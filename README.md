<p align="center">
  <img src="icon.ico" alt="Just E-Shop Logo" width="180">
</p>

<h1 align="center">🛒 E-Commerce System</h1>

<p align="center">
  <img src="https://img.shields.io/badge/build-passing-brightgreen">
  <img src="https://img.shields.io/badge/license-MIT-blue">
  <img src="https://img.shields.io/badge/version-1.0.0-orange">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen">
</p>

> A simple and user-friendly **E-commerce system** built with Python, allowing users to browse products, manage a shopping cart, and authenticate securely.

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🧐 About the Project

This **E-commerce System** is a Python-based application that simulates the core functionality of an online shopping platform. It allows users to register, log in, browse products, and manage a shopping cart using a local database.

The project focuses on **clean architecture**, **modular design**, and **core e-commerce logic**, making it ideal for learning purposes, academic projects, or portfolio presentation.

---

## 🚀 Key Features

### 👤 User / Customer
- **User Authentication**  
  Secure registration and login system.

- **Product Browsing**  
  View available products with details such as name, description, and price.

- **Search & Filtering**  
  Search products and filter them by category.

- **Shopping Cart**  
  Add, remove, and update items in the cart.

- **Persistent Storage**  
  Data stored using a local SQLite database.

> ⚠️ *Admin dashboard and payment processing are intentionally excluded.*

---

## 🛠 Tech Stack

**Backend:**
- Python backend

**Database:**
- SQLite

**Frontend / GUI:**
- Python-based graphical interface

**Tools:**
- Git & GitHub

---

## 📂 System Architecture

```text
E-commerce-system/
├── controllers/        # Application logic
├── database/           # Database configuration
├── gui/                # User interface
├── models/             # Data models
├── utils/              # Helper utilities
├── ecommerce.db        # SQLite database
├── main.py             # Application entry point
└── README.md

