# Website Status Checker

The Website Status Checker is a Python script designed to monitor the availability and response times of websites. It performs HTTP GET requests to the specified URLs, checks their status codes, and measures the response times. This tool is useful for ensuring your websites are up and running and for tracking performance metrics.

## Features

- Check the status of multiple websites from a text file.
- Measure and display the response time of each website.
- Handle HTTP errors and display appropriate messages.
- Retry failed requests with a configurable delay.

## Requirements

- Python 3.x
- `requests` library (can be installed via `pip`)

## Installation

1. **Clone the repository** (or download the script):

   ```bash
   git clone https://github.com/your-username/website-status-checker.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd website-status-checker
   ```
3. **Install the required Python library**:
   ```bash
   pip install requests
   ```

## Usage
Prepare a file with the list of websites:

Create a file named `websites.txt` in the same directory as the script, and list each URL on a new line:

Example:
```
https://www.example.com
https://www.anotherexample.com
```
Run the script:
```bash
python website_checker.py
```
The script will read the URLs from websites.txt, check their status, and display the results in the console.

## Practical Usecases:
1. **Website Monitoring**:
   - **Personal Websites**: Ensure your personal blog or portfolio site is always accessible.
   - **Business Websites**: Monitor your company's website to avoid downtime and maintain customer satisfaction.
2. **Server and Network Administration**:

   - **Health Checks**: Regularly check the status of critical websites or web applications to ensure they are operational.
   - **Maintenance Alerts**: Receive alerts when a website goes down, allowing you to address issues promptly.
3. **Development and Testing**:
   - **Continuous Integration (CI)**: Integrate the script into your CI pipeline to automatically check the status of your deployed applications.
   - **Performance Testing**: Measure and monitor response times during development to identify performance issues.
4. **Scheduled Monitoring**:
   - **Automated Health Checks**: Set up the script to run periodically (e.g., every 30 minutes) using cron jobs(Linux) or Task Scheduler(Windows) to keep an eye on multiple websites. Instead we can also use airflow to create DAG and schedule the job.
5. **Reporting**:
   - **Client Reports**: Generate regular status and performance reports for clients to show uptime and response times.
   - **Performance Analytics**: Track and analyze response times over time to identify trends or issues.

## Code Explanation
`check_website_status(url, retries=3, delay=5)`:

- **Purpose**: Checks the status of a given URL and retries if needed.
- **Parameters**:
    - `url`: The URL to check.
    - `retries`: Number of retry attempts if the request fails.
    - `delay`: Delay in seconds between retry attempts.
- **Process**:
    - Measures response time.
    - Handles various HTTP status codes and exceptions.
    - Displays the status code and response time.
- **Main Script Execution**:
  - Reads URLs from `websites.txt`.
  - Calls `check_website_status()` for each URL.
  - Prints the results.

## Future Enhancements
- **Add Notification Alerts**: Integrate with email or messaging services to notify users when a website is down.
- **Expand Retry Logic**: Implement exponential backoff or more sophisticated retry strategies.
- **Performance Reporting**: Generate reports or logs of response times and status codes over time.
- **User Interface**: Create a graphical user interface (GUI) or a web interface for easier interaction.
- **Support for More Protocols**: Add support for other protocols like FTP, SMTP, etc.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.