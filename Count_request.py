# Program for Count IP Requests
from collections import defaultdict

# Function to count requests from each IP address
def count_requests(file_path):
    ip_counts = defaultdict(int)  # Store the count for each IP
    
    # Open the log file
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line and get the IP address (assuming it's the first part)
                parts = line.split()
                ip = parts[0]  # The first part is the IP address
                ip_counts[ip] += 1  # Increment the count for that IP address
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return
    
    # Sort IP addresses by the number of requests in descending order
    sorted_ip = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print the sorted IPs and their counts
    print(f"{'IP Address':<20} {'Request Count'}")
    print('-' * 40)
    for ip, count in sorted_ip:
        print(f"{ip:<20} {count}")


log_file_path = "C:\Users\VICTUS\OneDrive\Desktop\VRV security Assignments\sample.txt"  # Replace with the path to your log file
count_requests(log_file_path) # calling the function
