🧩 1. Project Overview

The Automated Lighthouse System is a smart, microcontroller-driven project designed to simulate the operation of an automated lighthouse using an Arduino Uno integrated with a Flask-based web interface.

The system enables users to remotely control an LED and buzzer (representing the lighthouse’s light and sound signals) through a web dashboard. It demonstrates how embedded systems can be managed via IoT-inspired web control for automation, learning, and prototyping purposes.

🎯 2. Problem Statement

Traditional control of small-scale embedded systems, such as LEDs or buzzers, requires manual hardware interaction, which limits accessibility and scalability.
There is a need for a simple, web-based interface that allows users to remotely control and monitor connected hardware components such as lights, sensors, and alarms in real-time.

The Automated Lighthouse System addresses this by creating a bridge between web technologies and physical devices, providing a model for both educational demonstrations and practical automation systems.

🎯 3. Objectives

✅ To design a simple Arduino-controlled automation system that can be managed from a web application.

✅ To enable bi-directional communication between the web interface and the Arduino microcontroller.

✅ To use a buzzer and LED to simulate real-world lighthouse behavior (light and sound signals).

✅ To apply modern web UI design for an intuitive and visually appealing dashboard using DaisyUI & Tailwind CSS.

✅ To demonstrate how Flask and PySerial can serve as middleware for controlling IoT devices.

🛠️ 4. Technology Stack
Layer	Technology	Purpose
Frontend	HTML5, CSS3, Tailwind CSS, DaisyUI	For building a clean, modern, and responsive user interface
Backend	Python Flask	For handling web requests and controlling hardware
Communication	PySerial	To transmit commands from Flask to Arduino through serial communication
Microcontroller	Arduino Uno (C++)	To process incoming commands and control the LED and buzzer
Server Environment	Localhost (127.0.0.1:5000)	Web server running Flask application
Hardware Components	LED (Pin 6), Buzzer (Pin 7)	Output devices controlled by the system
⚙️ 5. System Features
Feature	Description
Web-Based Control	Users can turn the LED and buzzer ON or OFF from a browser interface.
Responsive UI	The interface adapts to mobile, tablet, and desktop screens.
Real-Time Hardware Interaction	Immediate response between user input and Arduino output.
Visual Feedback	The system can be extended to show ON/OFF status visually.
Scalability	Designed for easy expansion to multiple devices or sensors.
🧠 6. System Architecture
Overview

The architecture follows a three-layer structure:

Presentation Layer (Frontend)

Developed with HTML and Tailwind CSS using DaisyUI components.

Provides buttons to send control commands to the backend.

Application Layer (Backend - Flask)

Receives user requests and translates them into serial commands.

Acts as a middleware between the web interface and the Arduino.

Hardware Layer (Arduino)

Reads serial commands and activates or deactivates the LED and buzzer accordingly.

Data Flow Diagram
User (Browser)
     ↓
Flask Web Server (Python)
     ↓
PySerial Communication
     ↓
Arduino Uno
     ↓
LED + Buzzer (Output Devices)

📊 7. Functional Requirements
ID	Requirement	Description
FR1	System should provide a web interface	The user can control the LED and buzzer from the browser.
FR2	Flask should communicate via serial	Commands must be sent through PySerial.
FR3	Arduino must respond to serial commands	It should turn LED/buzzer ON or OFF.
FR4	UI should be visually appealing	Use DaisyUI/Tailwind for consistent styling.
FR5	System should operate locally	No internet connection required for basic operation.
🧩 8. Non-Functional Requirements
Category	Requirement
Performance	Command response time must be less than 2 seconds.
Usability	Interface should be simple, intuitive, and mobile-friendly.
Reliability	System should handle communication loss gracefully.
Scalability	Support for future sensors (temperature, light, etc.).
Maintainability	Code should be modular and documented.
🖥️ 9. Hardware Components
Component	Specification	Purpose
Arduino Uno	ATmega328P	Main control board
LED	Generic 5mm	Simulates lighthouse light
Buzzer	5V Active	Simulates lighthouse sound
USB Cable	Type A to B	Connects Arduino to PC
Jumper Wires	Male-to-Male	For wiring LED and buzzer
Resistor	220Ω (for LED)	Limits LED current
🌐 10. User Interaction Flow

User opens the web app (Flask interface).

User clicks Turn ON → Flask sends a serial command “1” to Arduino.

Arduino activates LED + buzzer.

User clicks Turn OFF → Flask sends “0” → Arduino turns them off.

Web UI can be enhanced to show status or animation feedback.

🔮 11. Future Enhancements

🌡️ Integration of sensors (light, motion, or temperature).

🌍 Remote hosting using Ngrok or a cloud server.

📱 Mobile app interface for remote lighthouse control.

⚙️ Add MQTT or WebSocket for real-time communication.

🎨 Dashboard with animation and system status visualization.

📘 12. Conclusion

The Automated Lighthouse System demonstrates how embedded hardware can be seamlessly controlled using modern web technologies.
It provides an educational foundation for IoT, automation, and embedded communication.

By integrating Arduino, Flask, and PySerial, this system showcases the bridge between software intelligence and hardware control, creating an accessible, scalable, and engaging automation solution.









<img width="1898" height="1075" alt="image" src="https://github.com/user-attachments/assets/31ee5a11-b2d3-47c7-b8d0-31b232b16997" />
