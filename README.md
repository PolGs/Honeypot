# Honeypot
This honeypot creates a listening socket. When a connection is made to this socket, it will send a fake login prompt asking for a username and password

This code creates a dictionary called ip_logins that keeps track of the number of attempted logins for each IP address that connects to the honeypot. Each time a connection is made, the IP address is added to the dictionary if it's not already there, and the number of attempted logins for that IP is incremented by one. After the fake login credentials are received, the IP address and number of attempted logins is logged to a file called honeypot_log.txt.

![image](https://user-images.githubusercontent.com/19478700/214123183-82346faf-0917-48a4-8707-9f52885a816b.png)

#### Nmap Scan:
![image](https://user-images.githubusercontent.com/19478700/214123709-662c07ad-0c45-4ece-9894-9ce111e63630.png)
