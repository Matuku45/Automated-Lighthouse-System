# automated-light-house-system/app.py
from flask import Flask, request
import serial
import serial.tools.list_ports
import time
import os

app = Flask(__name__)

# ✅ Function to connect to Arduino with automatic port detection
def connect_arduino(target_port="COM9", baud_rate=9600):
    print("🔍 Scanning available COM ports...\n")
    ports = serial.tools.list_ports.comports()

    if not ports:
        print("❌ No COM ports found. Please connect your Arduino.")
        return None

    print("Available Ports:")
    for p in ports:
        print(f" - {p.device} ({p.description})")

    try:
        print(f"\n🔗 Trying to connect to {target_port}...")
        arduino = serial.Serial(target_port, baud_rate, timeout=1)
        time.sleep(2)
        print(f"✅ Successfully connected to {target_port}")
        return arduino
    except Exception as e:
        print(f"\n⚠️ Could not open {target_port}: {e}")
        print("💡 Tip: Ensure no other app (like Arduino IDE) is using it.")
        return None

# 🔌 Only connect Arduino once even if Flask reloads (debug=True)
arduino = None
if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    arduino = connect_arduino()

# 🧠 Single-page Flask + HTML
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
    global arduino
    if request.method == "POST":
        action = request.form.get("action")

        if arduino is None:
            print("❌ Arduino not connected. Cannot send command.")
            return "<h3 style='color:red;text-align:center;'>Arduino not connected. Check console logs.</h3>"

        try:
            if action == "on":
                arduino.write(b'1')  # Turn on LED & Buzzer
                print("🟢 LED & Buzzer ON")
            elif action == "off":
                arduino.write(b'0')  # Turn off LED & Buzzer
                print("🔴 LED & Buzzer OFF")
        except Exception as e:
            print(f"⚠️ Error sending command: {e}")

    return HTML_PAGE


if __name__ == "__main__":
    app.run(debug=True)
