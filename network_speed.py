import speedtest
import datetime
import os

LOG_FILE = "speed_log.txt"

def run_speed_test():
    print("Testing network speed... please wait.")
    st = speedtest.Speedtest()
    st.get_best_server()

    download = round(st.download() / 1_000_000, 2)
    upload = round(st.upload() / 1_000_000, 2)
    ping = round(st.results.ping, 2)

    return download, upload, ping

def log_result(download, upload, ping):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{now}]  Download: {download} Mbps  |  Upload: {upload} Mbps  |  Ping: {ping} ms"

    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

    return entry

def show_log():
    if not os.path.exists(LOG_FILE):
        print("No log file found yet. Run a speed test first.")
        return
    print(f"\n--- Speed Log ({LOG_FILE}) ---")
    with open(LOG_FILE, "r") as f:
        print(f.read())

print("Network Speed Logger")
print("--------------------")
print("1. Run speed test")
print("2. View log")
choice = input("\nChoose an option: ").strip()

if choice == "1":
    download, upload, ping = run_speed_test()
    entry = log_result(download, upload, ping)
    print(f"\nResult logged:")
    print(f"  {entry}")
elif choice == "2":
    show_log()
else:
    print("Invalid choice.")
