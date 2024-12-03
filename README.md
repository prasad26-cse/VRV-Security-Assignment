# VRV-Security-Assignment
Log File Analysis Script

Objective
This Python script is designed to process and analyze log files, specifically focusing on tasks related to network security, such as detecting potential brute force attacks, identifying frequent access patterns, and counting requests. The script extracts relevant information from log files, processes it, and generates useful reports for cybersecurity analysis.

Core Functionalities
1. Count Requests per IP Address
The script processes the log file to extract and count the number of requests made by each IP address.
Results are sorted and displayed in descending order, showing the IP addresses and their respective request counts.
Example Output:
IP Address     Request Count
203.0.113.5         8
198.51.100.23       8
192.168.1.1         7
10.0.0.2            6
192.168.1.100       5

   
2. Identify the Most Frequently Accessed Endpoint
The script extracts the endpoints (URLs or resource paths) accessed by clients from the log entries.
It then identifies the endpoint with the highest number of accesses and displays it along with the access count.
Example Output:
Endpoint         Access Count
/home                   5
/about                  5
/dashboard              3
/contact                2
/profile                2

3. Detect Suspicious Activity
The script detects potential brute force login attempts based on failed login entries in the log file. It looks for HTTP 401 status codes or specific failure messages like "Invalid credentials".
IP addresses with failed login attempts exceeding a configurable threshold (default: 10 attempts) are flagged as suspicious.
Example Output:
Suspicious Activity Detected:
IP Address Failed Login Attempts
No suspicious activity detected.

4. Output Results
The script displays the results in a clean and organized format on the terminal, making it easy to read and analyze.
The results are saved to a CSV file (log_analysis_results.csv), which includes:
Requests per IP: Columns - IP Address, Request Count
Most Accessed Endpoint: Columns - Endpoint, Access Count
Suspicious Activity: Columns - IP Address, Failed Login Count



Clone this repository to your local machine:
Usage
To run the script, follow these steps:
Place the log file you want to analyze in the same directory as the script or specify the full path to the log file in the script.
Run the script using Python:.
after processing the log file, the script will output:

Request counts per IP address

Most frequently accessed endpoint

Suspicious IPs with failed login attempts
Additionally, the results will be saved to a CSV file named log_analysis_results.csv in the same directory.
Configuration
Threshold for Suspicious Activity:
The script flags IP addresses with failed login attempts above a configurable threshold (default: 10).
You can modify the threshold by changing the threshold parameter in the script.


Sample Log File Format
The log file should follow a format similar to this:
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:37 +0000] "GET /contact HTTP/1.1" 200 312
198.51.100.23 - - [03/Dec/2024:10:12:38 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:39 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:40 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
The script will correctly process log entries with IP addresses, HTTP status codes, and resource paths to perform its analysis.

