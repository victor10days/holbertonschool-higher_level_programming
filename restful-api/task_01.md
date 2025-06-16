### 📌 Summary: HTTP vs HTTPS

| Feature      | HTTP                                      | HTTPS                                       |
|--------------|-------------------------------------------|---------------------------------------------|
| Security     | Not secure                                | Secure via SSL/TLS encryption               |
| Port         | 80                                        | 443                                         |
| URL Prefix   | `http://`                                 | `https://`                                  |
| Encryption   | None                                      | Encrypts data in transit                    |
| Use Case     | Public websites with no sensitive content | Login forms, payments, user data, etc.      |
| Browser Info | Shows as “Not Secure”                     | Shows padlock symbol (🔒) in address bar     |

---

### 📌 Structure of an HTTP Request & Response

#### ✅ Example: Request

```
GET /api/users HTTP/1.1
Host: example.com
User-Agent: curl/7.68.0
Accept: application/json
```

#### ✅ Example: Response

```
HTTP/1.1 200 OK
Content-Type: application/json
Date: Sun, 15 Jun 2025 17:20:00 GMT

[
  {
    "id": 1,
    "name": "Alice"
  }
]
```

---

### 📌 Common HTTP Methods

| Method | Description           | Use Case Example          |
|--------|------------------------|----------------------------|
| GET    | Retrieve data         | `GET /users`              |
| POST   | Create a new resource | `POST /users` with data   |
| PUT    | Update resource       | `PUT /users/5`            |
| DELETE | Remove a resource     | `DELETE /users/5`         |

---

### 📌 Common HTTP Status Codes

| Code | Meaning                  | Scenario                                      |
|------|--------------------------|----------------------------------------------|
| 200  | OK                       | Request succeeded (GET)                      |
| 201  | Created                  | POST created a new resource                  |
| 400  | Bad Request              | Malformed request                            |
| 404  | Not Found                | Resource not found                           |
| 500  | Internal Server Error    | Server-side problem                          |

---
