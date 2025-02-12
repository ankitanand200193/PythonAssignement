# CPU Usage Monitor

## Overview
This is a simple Python script that monitors the CPU usage of your system using the psutil library. It continuously checks the CPU usage and alerts the user if it exceeds a defined threshold.

## Features
Monitors CPU usage in real-time.
Alerts when CPU usage exceeds the specified threshold.
Handles keyboard interruption gracefully.
Minimal dependencies.

## Prerequisites
Ensure you have Python installed on your system (Python 3.x recommended).

## Install Dependencies
This script requires the psutil library. You can install it using:
**pip install psutil**

## Usage
Run the script with:  cpu_usage.py

By default, it monitors CPU usage every second and alerts if it exceeds 70%.

## Custom Threshold
You can modify the threshold by passing a different value in the function call inside if __name__ == "__main__": monitor_cpu(threshold=70)  # Set the threshold to 70%

## Exception Handling
Handles KeyboardInterrupt to allow the user to stop monitoring with Ctrl + C.
Catches any unexpected errors and prints the error message.

## License
This project is open-source and available under the MIT License.
