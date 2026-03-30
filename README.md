# CN_Orange_Problem  
## Distributed Reservation System using Secure Socket Programming

---

## 📌 Project Overview

This project implements a secure distributed reservation system using TCP socket programming with SSL/TLS encryption. Multiple clients can connect to a server to book and view seats.

---

## ⚙️ Features

- TCP Socket Communication  
- SSL/TLS Encryption  
- Multi-client support (threading)  
- Concurrency control (locks)  
- JSON data persistence  
- Client inactivity timeout  
- Stress testing  

---

## 🏗️ Project Structure

CN_Orange_Problem/
- server.py
- client.py
- booking.py
- storage.py
- stress_test.py
- seats.json
- cert.pem
- key.pem
- README.md

---

## 🔐 SSL Setup
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes


Use your server IP as Common Name.

---

## 🚀 Run

Start server: python server.py


Run client:python client.py


---

## Commands

- BOOK <seat_number>
- VIEW
- EXIT

---

## ⏱ Timeout

Client auto-logs out after inactivity.

---

## 🔄 Concurrency

Uses thread locks to prevent double booking.

---

## 💾 Storage

Uses JSON file for persistence.

---

## 🧪 Stress Test
python stress_test.py


---

## 🎯 Conclusion

This project demonstrates secure, concurrent client-server communication using sockets and SSL.

---

## 👨‍💻 Authors

Pulla Jagadeeshwar Reddy

Pranav S S

Naveen Patangi
