
import subprocess
import re
import socket
import time
from datetime import datetime

DESTINATION = "10.0.200.2"
SECRET = "666be527c24e17ebfd35494758e2b984"

CONTROLLERS = [
    ("R1", "10.0.100.2", 5050),
    ("R2", "10.0.23.1", 5051)
]

THRESHOLD_MS = 30
previous_state = None


def notify_all(state):
    all_successful = True

    for name, ip, port in CONTROLLERS:
        message = f"{SECRET}:{state}\n"

        try:
            with socket.create_connection((ip, port), timeout=5) as sock:
                sock.sendall(message.encode())
                sock.shutdown(socket.SHUT_WR)

            print(f"{name} notification: {state}", flush=True)

        except Exception as error:
            print(f"{name} notification failed: {error}", flush=True)
            all_successful = False

    return all_successful


print("Adaptive Congestion Monitor Started", flush=True)

while True:
    result = subprocess.run(
        ["ping", "-c", "3", "-W", "2", DESTINATION],
        capture_output=True,
        text=True
    )

    output = result.stdout

    loss_match = re.search(r"([\d.]+)% packet loss", output)
    latency_match = re.search(
        r"= [\d.]+/([\d.]+)/[\d.]+/[\d.]+ ms", output
    )

    loss = float(loss_match.group(1)) if loss_match else 100.0
    latency = float(latency_match.group(1)) if latency_match else None

    if latency is None or latency > THRESHOLD_MS or loss > 10:
        state = "CONGESTED"
    else:
        state = "NORMAL"

    timestamp = datetime.now().strftime("%H:%M:%S")
    latency_display = f"{latency:.2f} ms" if latency is not None else "No RTT"

    print(
        f"{timestamp} | Latency: {latency_display} | "
        f"Loss: {loss}% | {state}",
        flush=True
    )

    if state != previous_state:
        if notify_all(state):
            previous_state = state

    time.sleep(4)
