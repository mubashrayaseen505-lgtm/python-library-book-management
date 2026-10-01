# Library Book Management

A beginner-friendly Python project that demonstrates Object-Oriented Programming through a simple library book management system.

## Features

- Create a book object
- Store book title and author
- Track book availability
- Display book information
- Borrow an available book
- Return a borrowed book
- Prevent borrowing an unavailable book
- Prevent returning a book that is already available

## OOP Concepts Used

This project demonstrates:

- Classes and objects
- `__init__()` constructor
- Instance attributes
- Instance methods
- Conditional statements
- Boolean values
- Updating object attributes
- Object state management

## How It Works

The project contains a `Book` class with information about the book and methods for managing its availability.

### Book

The `Book` class stores:

- Book title
- Author
- Availability status

It provides three main methods:

- `display()` — displays the book information
- `borrow()` — changes the book status to unavailable
- `return_book()` — changes the book status back to available

## Example

The book starts as available:

```text
Title: Python Basics
Author: Harry
Available: True
