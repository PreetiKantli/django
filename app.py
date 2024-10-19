from flask import Flask, jsonify
import psutil
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop', methods=['GET'])
def htop():
    # Get system details
    full_name = "Preethi B Kantli"  # Replace with your full name
    username = os.getlogin()  # System username
    timezone = pytz.timezone('Asia/Kolkata')  # IST timezone
    server_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Get top-like system stats
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    data = {
        'Name': full_name,
        'Username': username,
        'Server_Time_IST': server_time,
        'CPU_Percent': cpu_percent,
        'Memory_Total': memory.total,
        'Memory_Used': memory.used,
        'Memory_Available': memory.available
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
