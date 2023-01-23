import socket

# Create a honeypot listening on port 1234
honeypot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
honeypot.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
honeypot.bind(("0.0.0.0", 2222))
honeypot.listen(5)

# Create a dictionary to store the number of attempted logins for each IP address
ip_logins = {}

while True:
    # Wait for a connection
    client, address = honeypot.accept()
    print("Connection from", address)
    ip = address[0]

    # Add the IP to the dictionary if it's not already there
    if ip not in ip_logins:
        ip_logins[ip] = 0

    # Increment the number of attempted logins for the IP
    ip_logins[ip] += 1

    # Send a fake prompt
    client.send("Welcome to the honeypot!\n".encode())
    client.send("Username: ".encode())

    # Receive login credentials (which should be fake)
    username = client.recv(1024).strip()
    client.send("Password: ".encode())
    password = client.recv(1024).strip()
    client.send("Login failed!".encode())

    print("Received credentials:", username, password)

    # Log the IP and number of attempted logins to a file
    with open("honeypot_log.txt", "a") as log_file:
        log_file.write(f"{ip} - {ip_logins[ip]} attempted logins\n")

    # Close the connection
    client.close()
