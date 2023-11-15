import os
import glob
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def send_excel_file_with_telegram(file_path, caption=""):
    """
    Sends an Excel file to a specified Telegram chat using a bot.
    
    Parameters:
    - file_path: Path to the Excel file to be sent.
    - caption: Optional caption for the message.
    """
    TOKEN = "" # TELEGRAM BOT TOKEN
    chat_id = "" # TELEGRAM GROUP ID

    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': chat_id, 'caption': caption}

    response = requests.post(url, files=files, data=data)

    if response.status_code == 200:
        print("Excel file sent successfully!")
    else:
        print("Failed to send Excel file. Status code:", response.status_code)
        print(response.text)

def delete_most_recent_xlsx(path_to_directory):
    """
    Deletes the most recent xlsx file in a specified directory.
    
    Parameters:
    - path_to_directory: The directory to search for xlsx files.
    """
    xlsx_files = glob.glob(os.path.join(path_to_directory, '*.xlsx'))

    if xlsx_files:
        most_recent_file = max(xlsx_files, key=os.path.getmtime)
        os.remove(most_recent_file)
        print(f"Deleted file: {most_recent_file}")
    else:
        print("No xlsx file found...")

def get_recent_xlsx_file(download_dir):
    """
    Retrieves the most recent xlsx file from a specified directory.
    
    Parameters:
    - download_dir: The directory to search for xlsx files.
    
    Returns:
    - Path of the most recent xlsx file, or a message if no file is found.
    """
    xlsx_files = [f for f in os.listdir(download_dir) if f.endswith('.xlsx')]
    xlsx_files.sort(key=lambda x: os.path.getmtime(os.path.join(download_dir, x)), reverse=True)

    if xlsx_files:
        return os.path.join(download_dir, xlsx_files[0])
    else:
        return "No Excel files found in the directory."

def download_scan_result(driver, scan_name, download_dir):
    """
    Navigates to a website, finds a specific scan, and downloads its result.
    
    Parameters:
    - driver: The Selenium WebDriver.
    - scan_name: The name of the scan to be downloaded.
    - download_dir: The directory where the file will be downloaded.
    """
    url = "https://chartink.com/login"
    email = ""  # Your email
    password = ""  # Your password

    driver.get(url)
    wait = WebDriverWait(driver, 45)
    
    # Login
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/div/button').click()

    # Wait for scans to load
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#home > table")))
    all_scans_table = driver.find_element(By.CSS_SELECTOR, "#home > table")
    scan_table_rows = all_scans_table.find_elements(By.TAG_NAME, "tr")

    for row in (scan_table_rows[1:(len(scan_table_rows)-1)]):
        cells = row.find_elements(By.TAG_NAME, "td")
        stock_name = cells[0]
        if stock_name.text == scan_name:
            print("FOUND THE SCAN!")
            stock_name.click()

            # Download the file
            download_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0_wrapper"]/div[1]/div/button[4]')))
            download_button.click()
            time.sleep(20)  # Wait for the file to download

            recent_xlsx
