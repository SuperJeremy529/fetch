# Fetch - Technical Assessment

# Overview

This is a FastAPI project that processes receipts and calculates points based on predefined rules. The project is containerized using Docker Compose for easy deployment and testing.

# Prerequisites

Ensure you have the following installed before running the project:

Docker

Docker Compose

Setup and Running the Project

To build and run the project, use the following command:

```
sudo docker compose up --build
```

This will start the FastAPI application on http://localhost:8000/.

# API Endpoints


Endpoint: POST /receipts/process

Payload: JSON receipt

Response: JSON containing an ID for the receipt

Example Request:
```
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },
    {
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    }
  ],
  "total": "35.35"
}

Example Response:

{
  "id": "7fb1377b-b223-49d9-a31a-5a02701dd310"
}
```
Get Points

Endpoint: GET /receipts/{id}/points

Response: JSON containing the number of points awarded

Example Response:
```
{
  "points": 32
}
```

# Example Calculation

```
Receipt:

{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    { "shortDescription": "Gatorade", "price": "2.25" },
    { "shortDescription": "Gatorade", "price": "2.25" },
    { "shortDescription": "Gatorade", "price": "2.25" },
    { "shortDescription": "Gatorade", "price": "2.25" }
  ],
  "total": "9.00"
}
```
