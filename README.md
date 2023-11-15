#  Chartink Scan Downloader & Telegram Sender

# Overview
This Python script is designed to automate the process of downloading scan results from the Chartink website and subsequently sending these results as an Excel file via Telegram. The script is useful for traders and analysts who regularly monitor stock scans and wish to receive updates through Telegram for convenience and speed.

# Features
Automated Login: Logs into the Chartink website using provided credentials.
Scan Identification and Download: Identifies a specified scan and downloads its results.
Telegram Integration: Sends the downloaded Excel file to a specified Telegram chat using a bot.
File Cleanup: Removes the most recently downloaded Excel file to maintain a clean workspace.

# Dependencies
Selenium: For web automation tasks.
Requests: For sending HTTP requests (used in Telegram communication).
Python Standard Libraries: os, glob, time.

# Functions
send_excel_file_with_telegram(file_path, caption="")
Sends an Excel file to a specified Telegram chat using a bot.

file_path: Path to the Excel file to be sent.
caption: Optional caption for the message.
delete_most_recent_xlsx(path_to_directory)
Deletes the most recent xlsx file in a specified directory.

path_to_directory: The directory to search for xlsx files.
get_recent_xlsx_file(download_dir)
Retrieves the most recent xlsx file from a specified directory.

download_dir: The directory to search for xlsx files.
download_scan_result(driver, scan_name, download_dir)
Navigates to the Chartink website, finds a specific scan, and downloads its result.

driver: The Selenium WebDriver.
scan_name: The name of the scan to be downloaded.
download_dir: The directory where the file will be downloaded.
Usage
To use this script:

Ensure all dependencies are installed.
Set the Telegram Bot Token and Group ID in the send_excel_file_with_telegram function.
Provide your Chartink login credentials in the download_scan_result function.
Specify the scan name you wish to download.
Run the script.
# The script will automatically log in to Chartink, download the specified scan result, send it to the Telegram chat, and clean up the downloaded file.

