#!/usr/bin/env python3
import requests
import time
from datetime import datetime

def ping_url(url):
    """Ping a URL and return status information"""
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = round((time.time() - start_time) * 1000, 2)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if response.status_code == 200:
            print(f"[{timestamp}] ✅ {url} is ONLINE - Response: {response_time}ms - Status: {response.status_code}")
        else:
            print(f"[{timestamp}] ❌ {url} returned status {response.status_code} - Response: {response_time}ms")
            
    except requests.exceptions.ConnectionError:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ❌ Cannot connect to {url}")
        
    except requests.exceptions.Timeout:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ❌ {url} timed out")
        
    except Exception as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ❌ Error: {str(e)}")

def main():
    # URL to monitor - change this to your desired URL
    url = "https://9a9f1f34-ac14-4cd2-bf93-0b725c128f7c-00-3ugen2u54w7my.worf.replit.dev:8080/"
    
    # Add http:// if no protocol specified
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    print(f"Starting URL ping monitor for: {url}")
    print("Checking every 30 seconds... Press Ctrl+C to stop")
    print("-" * 60)
    
    try:
        while True:
            ping_url(url)
            time.sleep(30)  # Wait 30 seconds before next ping
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    main()
