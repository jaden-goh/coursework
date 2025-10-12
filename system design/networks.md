IP ADDRESS identifies machines (clients, server, anything) - 32Bit (IP v.4, hosts 4 billion machines), 128bit (IP v.6 - enough to host all machines ever)
- Public and Private (local networks, other networks cannot access local private IPs)
- Static vs Dynamic (static important for server side, or Dynamic DNS)
- Ports: software-based communication endpoints within a computer's operating system that direct network traffic to specific applications or services. logical ports are numbered (0-65535) and used to differentiate data for different applications (e.g., HTTP on port 80 for web traffic and SMTP on port 25 for email) e.g localhost:3000 uses port 3000

Sending data (Internet Protocal Packets, or IP Packets):
Packets Contain:
-  Metadata: IP Addresses of Sender and Receiver (IP header)
-  Transmission Control Protocol header (or TCP header, for large amounts of data, contains the sequence number, gives instructions for reassembling pieces of data)
-  Application data: HTTP

TCP (Transmission Control Protocol):
- Re-transmission of lost packets
- 3-Way Handshake: SYN, SYN-ACK, ACK
        - Syn:	Used to initiate and establish a connection. It also helps you to synchronize sequence numbers between devices.
        - ACK:	Helps to confirm to the other side that it has received the SYN.
        - SYN-ACK:	SYN message from local device and ACK of the earlier packet.
        - FIN:	Used to terminate a connection.
- Reliable but Slower than UDP

UDP (User datagram protocal):
- No connection needed between client and server
- Not as reliable in sending data packets and will not have re-transmission, and also appear out of order, but faster than TCP
- Used for real time things where speed matters over missing data some times (e.g livestream cutting off, playback in real time but last few frames missed)

DNS (Domain Name System):
- Contact list (where IP is the "phone number")
- e.g google.com points to its IP address
- client request from DNS, DNS returns server IP address
- ISP, ICANN owns these DNS
- Domain registrars (e.g GoDaddy) resells provider names
- Client's can Cache IP Addresses (in the local disk)
- " https:// " is the protocol
- ". com" are the top level domains
- "google" primary domain name
- "domains" in domains.google.com is sub-domain
- google.com/images, "images" is sub-query

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
 - SSL/TLS (secure, S in HTTPS): TLS is Transfer level security: fights against Man In The Middle Attacks, encrypting anything sent to prevent anyone intercepting and finding your information