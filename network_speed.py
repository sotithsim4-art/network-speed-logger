import urllib.request
import datetime
import time
import os

LOG_FILE = "speed_log.txt"
TEST_URL = "http://speedtest.tele2.net/10MB.zip"
FILE_SIZE_MB = 10

def run_speed_test():
    print("Testing download speed... please wait.")
    start = time.time()
    urllib.request.urlretrieve(TEST_URL, "temp_test_file.bin")
    end = time.time()

    elapsed = end - start
    speed = round(FILE_SIZE_MB / elapsed * 8, 2)

    if os.path.exists("temp_test_file.bin"):
        os.remove("temp_test_file.bin")

    return speed, round(elapsed, 2)

def log_result(speed, elapsed):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{now}]  Download Speed: {speed} Mbps  |  Time: {elapsed}s"
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")
    return entry

def show_log():
    if not os.path.exists(LOG_FILE):
        print("No log file found yet. Run a speed test first.")
        return
    print(f"\n--- Speed Log ---")
    with open(LOG_FILE, "r") as f:
        print(f.read())

print("Network Speed Logger")
print("--------------------")
print("1. Run speed test")
print("2. View log")
choice = input("\nChoose an option: ").strip()

if choice == "1":
    speed, elapsed = run_speed_test()
    entry = log_result(speed, elapsed)
    print(f"\nResult logged:")
    print(f"  {entry}")
elif choice == "2":
    show_log()
else:
    print("Invalid choice.")
