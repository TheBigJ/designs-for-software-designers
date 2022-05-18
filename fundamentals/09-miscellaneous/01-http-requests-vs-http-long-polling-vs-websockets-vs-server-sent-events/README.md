# HTTP Requests

![](https://github.com/aditya109/designs-for-software-designers/raw/main/assets/http-request.svg)

# HTTP AJAX Polling

**A**synchronous **J**avaScript **A**nd **X**ML

Downsides:

- Empty responses
- Regular intervals
- Unnecessary network calls
- Delay in response

Process:

1. Client opens connection and requests data from the server using regular HTTP.
2. Requested webpage sends requests to the server at regular intervals.
3. Server calculates response and sends it back, just like regular HTTP traffic.
4. Receive updates from server. 