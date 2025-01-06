import requests
import time
import uuid
import random
import logging

# Configure logging
logging.basicConfig(filename='api_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(message)s')

# Color constants
MAGENTA = "\033[35m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# ASCII art and banner
ascii_banner = f"""
{CYAN}    
______                  _      ___                       
|  ___|                | |    / _ \                      
| |_ ___  _ __ ___  ___| |_  / /_\ \_ __ _ __ ___  _   _ 
|  _/ _ \| '__/ _ \/ __| __| |  _  | '__| '_ ` _ \| | | |
| || (_) | | |  __/\__ \ |_  | | | | |  | | | | | | |_| |
\_| \___/|_|  \___||___/\__| \_| |_/_|  |_| |_| |_|\__, |
                                                    __/ |
                                                   |___/ 
              {RESET}
"""

tagline = f"""
{YELLOW} +-+-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+
 DON'T FEAR WHEN WE ARE HERE ! NEVER PURCHASE SCRIPT FROM ANYONE
 +-+-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+ {RESET}
"""

print(f"{MAGENTA}{'=' * 70}{RESET}")
print(f"{ascii_banner}")
print(f"{tagline}")
print(f"{MAGENTA}{'=' * 70}{RESET}")
print(f"{GREEN}{BOLD}{UNDERLINE}Telegram: https://t.me/forestarmy{RESET}")
print(f"{RED}{BOLD}{UNDERLINE}YouTube: https://youtube.com/forestarmy{RESET}")
print(f"{MAGENTA}{'=' * 70}{RESET}")

# Function to send API request
def send_request(available_taps, count, token):
    url = 'https://api-gw.geagle.online/tap'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'https://telegram.geagle.online',
        'priority': 'u=1, i',
        'referer': 'https://telegram.geagle.online/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    timestamp = int(time.time())
    salt = str(uuid.uuid4())
    data = {
        "available_taps": available_taps,
        "count": count,
        "timestamp": timestamp,
        "salt": salt
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Status Code: {response.status_code}, Response Text: {response.text}")
        response.raise_for_status()  # Raise HTTP errors
        try:
            return response.json()  # Parse JSON
        except ValueError:
            error_msg = f"Error: Response is not valid JSON. Response: {response.text}"
            print(error_msg)
            logging.error(error_msg)
            return {"error": "Invalid JSON", "raw_response": response.text}
    except requests.exceptions.RequestException as e:
        error_msg = f"Request failed: {e}"
        print(error_msg)
        logging.error(error_msg)
        return {"error": str(e)}

# Load tokens from file
with open('data.txt', 'r') as file:
    tokens = [line.strip() for line in file.readlines()]

available_taps = 1000
total_requests = 0

# Main loop
while True:
    for token in tokens:
        count = random.randint(240, 270)
        response = send_request(available_taps, count, token)
        print(f"{CYAN}Response for token {token}:{RESET} {response}")
        total_requests += 1
        delay = random.uniform(2, 5)
        print(f"{YELLOW}Calculated delay:{RESET} {delay:.2f} seconds")
        time.sleep(delay)
        print(f"{GREEN}Finished delay of {delay:.2f} seconds. Moving to the next request...{RESET}")
        
        if total_requests >= 4:
            sleep_time = random.uniform(4 * 60, 6 * 60)
            print(f"{RED}Waiting for {sleep_time:.2f} seconds after 5 requests...{RESET}")
            time.sleep(sleep_time)
            total_requests = 0  # Reset the counter after sleeping
