# Program Most accessed endpoint
import re
from collections import defaultdict

# Function to find and count the most accessed endpoint
def most_accessed_endpoint(file_path):
    endpoint_counts = defaultdict(int)  # Store the count of accesses for each endpoint
    
    # Regex pattern to extract the endpoint 
    endpoint_pattern = r'"GET (\S+)'  # Matches the endpoint part of the GET request
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = re.search(endpoint_pattern, line)
                if match:
                    endpoint = match.group(1)  # Extract the endpoint
                    endpoint_counts[endpoint] += 1  # Increment the count for that endpoint
                
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return
    
    # Sort endpoints by access count in descending order
    sorted_endpoints = sorted(endpoint_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Display the sorted endpoints and their counts
    print(f"{'Endpoint':<30} {'Access Count'}")
    print('-' * 40)
    for endpoint, count in sorted_endpoints:
        print(f"{endpoint:<30} {count}")


log_file_path = "C:\Users\VICTUS\OneDrive\Desktop\VRV security Assignments\sample.txt"  # Replace with your actual log file path
most_accessed_endpoint(log_file_path) # calling the function
