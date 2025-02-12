# CPU Usage Monitor

## Overview
This Python script will monitor the CPU usage of your system using the psutil library. It will continuously check the CPU usage and alerts if exceeds a defined threshold(70%).

## Properties
It will trackers CPU usage in real-time.
It will alert when CPU usage exceeds the defined threshold.
Handles keyboard interruption gracefully.

## Prerequisites
Ensure your machine have Python 3.x installed.

## Library requirements
Install psutil using:**pip install psutil**

## Custom Threshold
You can modify the threshold by passing a different value in the function call inside if __name__ == "__main__": monitor_cpu(threshold=70)   

## Exception Handling
Handles KeyboardInterrupt to allow the user to stop monitoring with **Ctrl + C**.
Any others unexpected errors and prints the error message with error codes

## Images
![Alt text](https://github.com/ankitanand200193/PythonAssignement/blob/b1935eb54d7a8d0ae3817888f730709c6103f929/CPU_usage_screenshot.png)




