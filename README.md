# Order Status Management System

A beginner-friendly Python project that demonstrates **object-oriented programming (OOP)** and **enumerations (`Enum`)** through a simple order status management system.

## Overview

Each order has an order ID, a customer name, and a current status. New orders start as `PENDING`. The `update_status()` method accepts an `OrderStatus` enum member, updates the order, and prints a confirmation message. Invalid inputs are rejected with a message.

## Features

- Create an order with an ID and customer name.
- Assign `PENDING` as the default status.
- Represent order statuses with Python's built-in `Enum`.
- Update an order's status when given a valid `OrderStatus` member.
- Display an order's ID, customer name, and current status.
- Print `Invalid` when an update receives a value that is not an `OrderStatus` member.

## Available Statuses

| Status | Value | Meaning |
| --- | ---: | --- |
| `PENDING` | 1 | The order is waiting to be processed. |
| `PROCESSING` | 2 | The order is being processed. |
| `SHIPPED` | 3 | The order has been shipped. |
| `DELIVERED` | 4 | The order has been delivered. |
| `CANCELED` | 5 | The order has been canceled. |

## Requirements

- Python 3
- No third-party packages required (`enum` is part of the Python standard library).

## How to Run

1. Save the Python code as `main.py` in the project folder.
2. Open a terminal in that folder.
3. Run:

   ```bash
   python3 main.py
   ```

## Example Usage

```python
order1 = Order(101, "Peter")
order1.display()

order1.update_status(OrderStatus.PROCESSING)
order1.update_status(OrderStatus.SHIPPED)
order1.update_status(OrderStatus.DELIVERED)
order1.update_status(OrderStatus.CANCELED)
```

### Expected Output

```text
Order Id: 101
Customer: Peter
Status: OrderStatus.PENDING
Order 101 updated to PROCESSING
Order 101 updated to SHIPPED
Order 101 updated to DELIVERED
Order 101 updated to CANCELED
```

## How It Works

**`OrderStatus`** is an enum defining the named statuses available to the application. **`Order`** is a class representing an individual order.

- `__init__()` stores the order ID and customer name, then sets the initial status to `OrderStatus.PENDING`.
- `update_status(new_status)` uses `isinstance(new_status, OrderStatus)` to check whether the supplied value is an enum member. If valid, it assigns the value to `self.status` and prints a confirmation. Otherwise, it prints `Invalid` and leaves the current status unchanged.
- `display()` prints the order's information.

## Current Limitations

This is a learning project, not a complete order processing system. Status changes are made manually, and the current implementation allows any valid enum status to follow any other valid enum status (for example, `DELIVERED` to `CANCELED`). It does not enforce a specific order lifecycle, save data between runs, or provide a user interface.

## What I Practiced

- Python classes and objects
- Constructors (`__init__`) and instance attributes (`self`)
- Enum classes and members
- Instance methods and arguments
- Type validation with `isinstance()`
- Conditional logic and formatted output (f-strings)

## Possible Next Steps

- Add rules for allowed status transitions.
- Return or raise an error for invalid updates instead of only printing a message.
- Add automated tests for valid and invalid status updates.
- Support multiple orders and save them to a file or database.
