# .http files

IDEs sometimes will support .http type files, such as, VSCode. Then with an extension these files can be read and executed via a REST client or http client.

If using Visual Studio Code, the extension is called [Rest Client ](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

# File Format

```http
POST https://example.com/comments HTTP/1.1
content-type: application/json

{
    "name": "sample",
    "time": "Wed, 21 Oct 2015 18:27:50 GMT"
}
```

# Multiple Requests in File

```http
POST https://example.com/comments HTTP/1.1
content-type: application/json

{
    "name": "sample",
    "time": "Wed, 21 Oct 2015 18:27:50 GMT"
}

###

POST https://example.com/comments HTTP/1.1
content-type: application/json

{
    "name": "sample",
    "time": "Wed, 21 Oct 2015 18:27:50 GMT"
}
```

# Multiple Requests in File

```http
POST https://example.com/comments HTTP/1.1
content-type: application/json
Authorization: {{$token}}

{
    "name": "sample",
    "time": "Wed, 21 Oct 2015 18:27:50 GMT"
}

###

POST https://example.com/comments HTTP/1.1
content-type: application/json
Authorization: {{$token}}

{
    "name": "sample",
    "time": "Wed, 21 Oct 2015 18:27:50 GMT"
}
```

# Environment Variables

"rest-client.environmentVariables": {
    "$shared": {
        "version": "v1",
        "prodToken": "foo",
        "nonProdToken": "bar"
    },
    "local": {
        "version": "v2",
        "host": "localhost",
        "token": "{{$shared nonProdToken}}",
        "secretKey": "devSecret"
    },
    "production": {
        "host": "example.com",
        "token": "{{$shared prodToken}}",
        "secretKey" : "prodSecret"
    }
}


# References
- [Rest Client for VSCode](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)