Application Protocols
- Client-Server Interaction (client doesn’t need to be end user just a request maker)

RPC (remote procedure call)
- to call code on a remote machine/server (similar to how you’d call a function from another script)

HTTP (hyper text transfer protocol)
 - build on TCP and the other underlying, request-response protocol (req-res), components are the 1
        -  header (like the website name), 
        -  request method (get put post delete etc.) 
        -  request header with a lot more details sent to server 
 - CRUD (create read update delete -> mapped to post get put delete)
 - Status codes: informational response, successful, redirection, client side or server error response e.g 404, 401, 503
 - SSL/TLS (secure, tje S in HTTPS) or TLS (Transfer level security): 
    - fights against Man In The Middle Attacks
    - encrypts anything information to prevent anyone intercepting from finding your information

