# automated-light-house-system/app.py
from flask import Flask, request
import serial
import serial.tools.list_ports
import time
import os

app = Flask(__name__)

# Connect to Arduino automatically
def connect_arduino(target_port="COM9", baud_rate=9600):
    print("🔍 Scanning available COM ports...\n")
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("❌ No COM ports found. Connect your Arduino.")
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
        print("💡 Ensure no other app (like Arduino IDE) is using it.")
        return None

# Only connect Arduino once (debug reload safe)
arduino = None
if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    arduino = connect_arduino()

# Logs storage
logs = []

# HTML dashboard
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Automated Light House Dashboard</title>
<link href="https://cdn.jsdelivr.net/npm/daisyui@2.51.5/dist/full.css" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
function startVoiceCommand() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'en-US';
  recognition.start();
  recognition.onresult = function(event) {
    const command = event.results[0][0].transcript.toLowerCase();
    if(command.includes('led on')) document.getElementById('led-on').click();
    if(command.includes('led off')) document.getElementById('led-off').click();
    if(command.includes('buzzer on')) document.getElementById('buzzer-on').click();
    if(command.includes('buzzer off')) document.getElementById('buzzer-off').click();
  };
}
</script>
</head>
<body class="bg-gradient-to-r from-blue-100 to-blue-200 min-h-screen flex flex-col items-center p-6">

<div class="bg-white shadow-xl rounded-2xl p-8 w-full max-w-md text-center mb-6">
  <h1 class="text-3xl font-bold text-blue-600 mb-6">💡 Automated Light House Dashboard</h1>

  <form method="POST">
    <div class="grid grid-cols-2 gap-4 mb-4">
      <button id="led-on" name="action" value="led-on" class="btn btn-success w-full">LED ON 💡</button>
      <button id="led-off" name="action" value="led-off" class="btn btn-error w-full">LED OFF 💡</button>
      <button id="buzzer-on" name="action" value="buzzer-on" class="btn btn-success w-full">Buzzer ON 🔊</button>
      <button id="buzzer-off" name="action" value="buzzer-off" class="btn btn-error w-full">Buzzer OFF 🔊</button>
    </div>
    <button type="button" onclick="startVoiceCommand()" class="btn btn-primary w-full mb-4">🎤 Voice Command</button>
  </form>

  <div class="bg-gray-100 p-4 rounded-lg text-left h-40 overflow-y-auto">
    <h2 class="font-semibold text-blue-600 mb-2">Logs & Diagnostics:</h2>
    {% for log in logs %}
      <p>{{ log }}</p>
    {% endfor %}
  </div>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    global arduino, logs
    if request.method == "POST":
        action = request.form.get("action")
        if arduino is None:
            logs.append("❌ Arduino not connected.")
        else:
            try:
                if action == "led-on":
                    arduino.write(b'1')
                    logs.append("🟢 LED ON")
                elif action == "led-off":
                    arduino.write(b'0')
                    logs.append("🔴 LED OFF")
                elif action == "buzzer-on":
                    arduino.write(b'2')
                    logs.append("🟢 Buzzer ON")
                elif action == "buzzer-off":
                    arduino.write(b'3')
                    logs.append("🔴 Buzzer OFF")
            except Exception as e:
                logs.append(f"⚠️ Error sending command: {e}")

    return HTML_PAGE.replace("{% for log in logs %}", "\n".join(f"<p>{l}</p>" for l in logs))

if __name__ == "__main__":
    app.run(debug=True)
