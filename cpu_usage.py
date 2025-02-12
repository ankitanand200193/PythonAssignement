import psutil
import time

def monitor_cpu(threshold=70):
    print("CPU usage is being monitored...")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage method is being triggered every second
            print(f"CPU utilization is : {cpu_usage}%")
            
            if cpu_usage > threshold:
                print(f"Alert! CPU utilization  exceeds threshold: {cpu_usage}%")
            
            time.sleep(1)  # Wait for a second before checking again
    except KeyboardInterrupt:
        print("\nUser Stopped the Monitoring.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu(threshold=70)  # Set the threshold to 70%