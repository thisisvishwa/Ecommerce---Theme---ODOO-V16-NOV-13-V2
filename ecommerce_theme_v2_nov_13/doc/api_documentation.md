# API Documentation

This document provides detailed information about the APIs used in the `ecommerce_theme_v2_nov_13` module.

## Product API

### GET /api/products

Fetches all products.

**Parameters:**

- `category`: (optional) Filters products by category.

### GET /api/products/{id}

Fetches a specific product by its ID.

**Parameters:**

- `id`: The ID of the product.

### POST /api/products

Creates a new product.

**Parameters:**

- `name`: The name of the product.
- `category`: The category of the product.
- `price`: The price of the product.

## Category API

### GET /api/categories

Fetches all product categories.

### GET /api/categories/{id}

Fetches a specific category by its ID.

**Parameters:**

- `id`: The ID of the category.

### POST /api/categories

Creates a new product category.

**Parameters:**

- `name`: The name of the category.

## User API

### GET /api/users/{id}

Fetches a specific user by their ID.

**Parameters:**

- `id`: The ID of the user.

### POST /api/users

Creates a new user.

**Parameters:**

- `username`: The username of the user.
- `email`: The email of the user.
- `password`: The password of the user.

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of an API request. In case of an error, a JSON response will be sent with the following structure:

```json
{
  "error": {
    "code": "error_code",
    "message": "A description of the error"
  }
}
```

For more details about the APIs, refer to the source code in `controllers/main_controller.py`.