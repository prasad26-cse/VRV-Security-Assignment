#Program for Detect Suspicious Activity
from collections import defaultdict

def detect_suspicious_activity(log_file_path, attempt_threshold=10):
    # Dictionary to keep track of failed login attempts per IP address
    ip_failed_attempts = defaultdict(int)
    
    try:
        # Open and read the log file
        with open(log_file_path, 'r') as log_file:
            for entry in log_file:
                # Look for failed login indicators
                if '401' in entry or 'Invalid credentials' in entry:
                    # Split the log entry into components
                    components = entry.split()  
                    ip_address = components[0]  # Extract the IP address
                    ip_failed_attempts[ip_address] += 1  # Update the count for this IP
                
    except FileNotFoundError:
        print(f"Error: The specified file '{log_file_path}' was not found.")
        return
    
    # To display flagged IP addresses
    print("Suspicious Activity Detected:")
    print(f"{'IP Address':<20} {'Failed Login Attempts':<25}")
    print('-' * 50)
    
    # Filter IPs that exceed the defined threshold
    flagged_ips = [(ip, count) for ip, count in ip_failed_attempts.items() if count > attempt_threshold]
    
    # Output the results
    if flagged_ips:
        for ip, count in flagged_ips:
            print(f"{ip:<20} {count:<25}")
    else:
        print("No suspicious activity detected.")


log_file_path = "C:\Users\VICTUS\OneDrive\Desktop\VRV security Assignments\sample.txt"  # Replace with the actual path to your log file
detect_suspicious_activity(log_file_path)  # Call the function