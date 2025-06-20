# 🧰 Tools API Suite

This is an async-powered API suite built with **Quart + Uvicorn**, offering multiple developer utilities behind a unified API.

---


## ✅ Endpoints Overview

| Endpoint            | Method | Description                 |
| ------------------- | ------ | --------------------------- |
| `/healthz`          | GET    | Health check                |
| `/generate-uuid`    | GET    | Generate UUID v1/v3/v4/v5   |
| `/encrypt`          | POST   | AES encrypt text            |
| `/decrypt`          | POST   | AES decrypt text            |
| `/extract-pdf-text` | POST   | Extract text from PDF file  |
| `/generate-qrcode`  | POST   | Generate PNG QR code        |
| `/test-regex`       | POST   | Test regex pattern matching |
| `/chat`             | POST   | Light AI assistant (Gemma)  |

---

## 🧪 /test-regex

### 🔗 Endpoint

```
POST /api/test-regex
```

### 📤 Request Body

```json
{
  "pattern": "your-regex-pattern",
  "text": "your input text"
}
```

### 📥 Response

```json
{
  "matches": ["match1", "match2"]
}
```

### 🔥 Sample Patterns

**1. Extract numbers:**

```json
{
  "pattern": "\\d+",
  "text": "Version 3 was released in 2025."
}
```

**2. Extract email addresses:**

```json
{
  "pattern": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}",
  "text": "support@example.com or hello@dev.site"
}
```

**3. Extract capitalized words:**

```json
{
  "pattern": "\\b[A-Z][a-z]+\\b",
  "text": "Alice met Bob in New York"
}
```

---

## 🧾 Example: AES Encryption

### Request:

```json
{
  "text": "secret",
  "key": "pass1234"
}
```

### Response:

```json
{
  "cipher": "BASE64_ENCODED_ENCRYPTED_STRING"
}
```

---


## 🧾 Example: AES Decryption

### Request:

```json
{
  "cipher": "base64EncodedCipher",
  "key": "pass1234"
}
```

### Response:

```json
{
  "text": "DECRYPTED_STRING"
}
```

---

## 📦 Example: UUID Generator

**GET `/generate-uuid?version=4`**

Response:

```json
{
  "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "version": "4"
}
```

Parameters you can provide:

* Version of UUID: 1 / 3 / 4 / 5
* Name ***(Required in versions 3 and 5)***
* Namespace ***(Required in versions 3 and 5)***

📌 What are name and namespace?

* ***name***: a string you want to generate a UUID for (like a domain, filename, etc.)

* ***namespace***: a predefined UUID that provides context (like “DNS” or “URL”) 

More on name and namespace: https://docs.python.org/3/library/uuid.html#uuid.uuid3

---

## 🖼️ Example: QR Code Generator

**POST** `/generate-qrcode`

Request:

```json
{
  "text": "https://example.com"
}
```
**Note:** The version of the QR Code is decided automatically by the backend depending on the size of text. The maximum limit of the size of the text is **3000 characters**.

Response: PNG image stream (Content-Type: `image/png`)

---

## 🧠 AI Assistant (Model to be decided)
**Please note** that this API is currently under development and will take a little time as of 20th June 2025, to get the API running at the best price you people ;-)

**POST** `/chat`

```json
{
  "prompt": "Summarize benefits of yoga"
}
```

Response:

```json
{
  "response": "Yoga improves flexibility, focus..."
}
```

## 🚀 Deployment

Deployed using:

* **Quart** for Flask-compatible, but async, endpoints
* **Uvicorn** for production ASGI server 
#### All on Python version 3.12.

---

All APIs follow the REST structure of Response.

* 400 - Bad Request. You did something wrong.
* 500 - Server Error. I did something wrong.
* 200 - Ok. You good, me good.
* 404 - Not Found. Check the URL.
* Other errors are yet to be declared (Because I am going to implement authentication as well).

---

This project is under my goal of being completely open souce, and create APIs such that my fellow developers won't have to write codes for anything again and again. Just call the API from client side itself, and boom, no need to write new code, new endpoints, fall into the hassle. Just put a request on RapidAPI, and get your work done.

---

Of course this is not going to be a thing possible to be done by a single human. I need your help as well. Do post PRs, give suggestions as of what all to add, update, patch or whatever on the repository.

