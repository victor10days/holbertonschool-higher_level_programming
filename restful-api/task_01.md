## ✅ Task 1: Consume Data from an API Using Command Line Tools (`curl`)

### ✅ Step-by-Step Instructions

#### ✅ 1. Check if `curl` is installed

```bash
curl --version
```

> Should show version details like `curl 7.68.0`.

---

#### ✅ 2. Fetch a simple webpage

```bash
curl http://example.com
```

> Output: HTML content of the page.

---

#### ✅ 3. Fetch data from an API

```bash
curl https://jsonplaceholder.typicode.com/posts
```

> Output: JSON array of posts like:

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat...",
    "body": "quia et suscipit..."
  }
]
```

---

#### ✅ 4. Get only headers

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

> Output:

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Cache-Control: public, max-age=14400
...
```

---

#### ✅ 5. Make a POST request

```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

> Output:

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

---
