# 🚦 OX64 Traffic Light Web Server

Control GPIO LEDs from a web interface using **Buildroot + BusyBox + CGI**.

---

## 📌 Overview

This project builds a **minimal Linux system** for the **OX64 BL808** using Buildroot.  
On boot, the system:

- Connects to Wi-Fi  
- Starts a BusyBox HTTP server  
- Serves a traffic-light web interface  
- Runs a CGI script to control LEDs via **libgpiod**

The LEDs are switched in real time using **GET** requests from the webpage.

---

## 📁 Project Features

- Buildroot-based custom Linux image  
- Wi-Fi auto-configuration (`/etc/wifi.conf`)  
- BusyBox `httpd` with CGI enabled  
- GPIO control using `gpioset` (libgpiod)  
- HTML + JS UI served from `/www/`  
- LED control script in `/cgi-bin/led_control.cgi`  

---

## 🔧 GPIO Mapping

| LED     | GPIO |
|---------|------|
| Red     | 12   |
| Yellow  | 18   |
| Green   | 20   |

---

▶️ How to Use

1.Flash the Buildroot SD card image

Insert the SD card and boot the OX64

The board automatically connects to Wi-Fi

Find the OX64 IP address (via router or UART)

Open in your browser:

http://<OX64_IP>/


Control LEDs using the web interface

📦 Folder Structure
/www/
  index.html
  traffic.js

/cgi-bin/
  led_control.cgi

/etc/init.d/
  S99start.sh

