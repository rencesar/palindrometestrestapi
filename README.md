# Palindrome Test Rest API


### Explanation:

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
