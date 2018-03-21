# Palindrome Test Rest API


### Explanation:

 * Run server:
```
pip install -r requirements.txt
python manage.py runserver
```

 * Endpoint: '/palindrome/'
 * HTTP Method: POST
 * Request data: {"string": "anypalindromestringhere"}
 * Response Success:
 ```
 HTTP: 200
 Data:
 {"string": "anypalindromestringhere"}
 ```
 * Response Fail:
 ```
 HTTP: 400
 Data:
 {
    "string": [
        "Given string is not palindrome"
    ]
}
 ```
