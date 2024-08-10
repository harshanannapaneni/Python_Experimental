import requests
import time

def check_website_status(url, retries=3, delay=5):
    attempt = 0
    while attempt < retries:
        try:
            start_time = time.time()

            response = requests.get(url)

            end_time = time.time()
            response_time = end_time - start_time

            if response.status_code == 200:
                print(f"Website: {url} is up!")
                print(f"Response Time: {response_time:.2f} seconds\n")
                return  # Exit the function on success
            else:
                print(f"Website '{url}' returned status code {response.status_code}")
                print(f"Response Time: {response_time:.2f} seconds\n")

        except requests.RequestException as e:
            print(f"Website '{url}' is down or could not be reached.")
            print(f"Error: {e}\n")

        attempt += 1
        time.sleep(delay)  # Wait before retrying 



if __name__ == "__main__":
    with open("websites.txt",'r') as file:
        websites = file.readlines()
        # Prompt the user to enter a URL
    
    for website in websites:
        # Check the status of the website
        check_website_status(website.strip())