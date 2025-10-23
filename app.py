# automated-light-house-system/app.py
from flask import Flask, request
import serial
import time

app = Flask(__name__)

# ✅ Set up Arduino connection (change COM3 to match your port)
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Allow Arduino time to reset

# 🧠 Single-page app: Flask + HTML combined
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Automated Light House System</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@2.51.5/dist/full.css" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-blue-100 to-blue-200 min-h-screen flex items-center justify-center">

  <div class="bg-white shadow-xl rounded-2xl p-10 w-96 text-center">
    <h1 class="text-3xl font-bold text-blue-600 mb-6">
      💡 Automated Light House System
    </h1>

    <form method="POST">
      <button name="action" value="on" class="btn btn-primary w-full mb-4">Turn ON</button>
      <button name="action" value="off" class="btn btn-secondary w-full">Turn OFF</button>
    </form>

    <p class="mt-6 text-blue-500 text-sm">
      Control your LED (Pin 6) and Buzzer (Pin 7) connected to Arduino UNO in real-time.
    </p>
  </div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "on":
            arduino.write(b'1')  # Turn ON LED + Buzzer
            print("🟢 LED & Buzzer ON")
        elif action == "off":
            arduino.write(b'0')  # Turn OFF LED + Buzzer
            print("🔴 LED & Buzzer OFF")

    return HTML_PAGE

if __name__ == "__main__":
    app.run(debug=True)
