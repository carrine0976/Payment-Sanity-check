import  time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import operator



def create_chrome_driver()->webdriver.Chrome:
    options=Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    
def login_MMS(driver:webdriver.Chrome):
    url=f"https://mms-staging.hkmpcl.com.hk/en/login"
    driver.get(url)

    time.sleep(2)
    fill_in_account=driver.find_element(By.ID,"account")
    fill_in_account.send_keys("gary+FINApprover")
    time.sleep(2)

    fill_in_pwd=driver.find_element(By.ID,"password")
    fill_in_pwd.send_keys("Qwe123")

    login_click=driver.find_element(By.XPATH,"//button[@data-testid='Continue']")
    login_click.click()
    time.sleep(2)
    url2=f"https://mms-staging.hkmpcl.com.hk/en/payment/fee-record"
    driver.get(url2)
    time.sleep(2)

def get_merchant_data(driver:webdriver.Chrome):

    merchant_data=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[4]")
    
    return [merchant.text for merchant in merchant_data]  
def get_invoice_data(driver:webdriver.Chrome):

    invoice_data=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[14]")
    
    return [invoice.text for invoice in invoice_data]  
      
def fee_record_3PL_1221(driver:webdriver.Chrome):
    merchant_list=[]
    merchant="57075"
    invoice_button=driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item']")
    invoice_button.click()
    time.sleep(1)

    merchant_button=driver.find_element(By.XPATH, "(//span[text()='Merchant ID'])[2]")
    merchant_button.click()
    time.sleep(1)

    Searching_merchant=driver.find_element(By.XPATH, "//input[contains(@data-testid,'input')]")
    Searching_merchant.send_keys(f"{merchant}")
    time.sleep(1)

    Search_button=driver.find_element(By.XPATH, "//div[contains(@data-testid,'search')]")
    Search_button.click()
    time.sleep(1)

    merchant_list.extend(get_merchant_data(driver))
    while True:
        try:   
            next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
            next_button=next_page_button.get_attribute("class")

            if "ant-pagination-disabled" in next_button:
                break

            next_page_button.click()
            time.sleep(2)

            merchant_list.extend(get_merchant_data(driver))
        except Exception as e:
            print("Error navigating to next page:", e)
            break
    print(merchant_list)
    all_match =all(merchant_id==merchant for merchant_id in merchant_list)

    if all_match:
            print(f"All invoice values match the search value: {merchant_list} PASS")
            time.sleep(2)

    else:
            print(f"Not all invoice values match the search value: {merchant_list} FAIL")
            time.sleep(2)
def get_fee_record_data(driver:webdriver.Chrome):

    fee_record=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[1]")
    
    return [fee_id.text for fee_id in fee_record]  


def fee_record_3PL_fee_1594(driver:webdriver.Chrome):

    
    fee_record_id_list=[]
    invoice_button=driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item']")
    invoice_button.click()
    time.sleep(1)

    booking_button=driver.find_element(By.XPATH, "//span[text()='Fee Record ID']")
    booking_button.click()
    time.sleep(1)

    fee_record='13822'

    search_Booking_No=driver.find_element(By.XPATH, "//input[contains(@data-testid,'input')]")
    search_Booking_No.send_keys(f"{fee_record}")
    time.sleep(1)

    Search_button=driver.find_element(By.XPATH, "//div[contains(@data-testid,'search')]")
    Search_button.click()
    time.sleep(1)

    fee_record_id_list.extend(get_fee_record_data(driver))

    
    print(fee_record_id_list)
    all_match=all(fee==fee_record for fee in fee_record_id_list)

    if all_match:
        print(f"fee_record match data, case Pass!!!:{fee_record}")
        time.sleep(1)
    else:
        print(f"Store doesn't all match:{fee_record}") 
        time.sleep(1)  

def fee_record_3PL_340(driver:webdriver.Chrome):
    invoice_list=[]
    saerch_value="MS2405081230"
    
    Searching_invoice=driver.find_element(By.XPATH, "//input[contains(@data-testid,'input')]")
    Searching_invoice.clear()
    Searching_invoice.send_keys(f"{saerch_value}")
    time.sleep(1)

    Search_button=driver.find_element(By.XPATH, "//div[contains(@data-testid,'search')]")
    Search_button.click()
    time.sleep(1)

    script = "document.querySelector('.ant-table-body').scrollLeft += 10000;"  
    driver.execute_script(script)
    time.sleep(2)

    invoice_list.extend(get_invoice_data(driver))
        

    while True:
        try:   
            next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
            next_button=next_page_button.get_attribute("class")

            if "ant-pagination-disabled" in next_button:
                break

            next_page_button.click()
            time.sleep(2)

            driver.execute_script(script)
            time.sleep(1)

            invoice_list.extend(get_invoice_data(driver))
        except Exception as e:
            print("Error navigating to next page:", e)
            break
    print(invoice_list)
    all_match =all(invoice==saerch_value for invoice in invoice_list)

    if all_match:
            print(f"All invoice values match the search value: {saerch_value}")

    else:
            print(f"Not all invoice values match the search value: {saerch_value}")
if __name__=='__main__':
    
    driver=create_chrome_driver()
    wait = WebDriverWait(driver, 10)
    login_MMS(driver)
    fee_record_3PL_1221(driver)
    time.sleep(2)
    fee_record_3PL_fee_1594(driver)
    time.sleep(2)
    fee_record_3PL_340(driver)
    

    time.sleep(2)
    driver.quit()