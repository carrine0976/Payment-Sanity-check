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
    fill_in_account.send_keys("wicky.sze+008@shoalter.com")
    time.sleep(2)

    fill_in_pwd=driver.find_element(By.ID,"password")
    fill_in_pwd.send_keys("Qwe123")

    login_click=driver.find_element(By.XPATH,"//button[@data-testid='Continue']")
    login_click.click()
    time.sleep(2)
    payment_center=driver.find_element(By.XPATH, "(//span[contains(@class, 'ant-menu-title-content')])[3]")
    payment_center.click()
    time.sleep(2)


    payment_center_fee_record=driver.find_element(By.XPATH, "//a[@href='/en/payment/fee-record']")
        
    payment_center_fee_record.click()
    time.sleep(2)

def get_invoice_data(driver:webdriver.Chrome):

    invoice_data=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[14]")
    
    return [invoice.text for invoice in invoice_data]  
      
def fee_record_3PL_312(driver:webdriver.Chrome):
    invoice_list=[]
    saerch_value="MS2312080804"
    
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

def get_store_id(driver:webdriver.Chrome):

    store_id=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[3]")
    return [(store.text) for store in store_id]


def fee_record_3PL_1146(driver:webdriver.Chrome):


    store_list1=[]
    invoice_button=driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item']")
    invoice_button.click()
    time.sleep(1)

    store_id_button=driver.find_element(By.XPATH, "(//span[text()='Store ID'])[2]")
    store_id_button.click()
    time.sleep(1)

    store='B9069002'
    close_button=driver.find_element(By.XPATH, "//span[contains(@class,'ant-input-clear-icon ant-input-clear-icon-has-suffix')]")
    close_button.click()
    search_store_id=driver.find_element(By.XPATH, "//input[contains(@data-testid,'input')]")
    search_store_id.send_keys(f"{store}")
    time.sleep(1)

    Search_button=driver.find_element(By.XPATH, "//div[contains(@data-testid,'search')]")
    Search_button.click()
    time.sleep(1)

    store_list1.extend(get_store_id(driver))

    while True:
        try:
            next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
            next_page=next_page_button.get_attribute("class")

            if "ant-pagination-disabled" in next_page:
                break
            next_page_button.click()
            time.sleep(1)
            store_list1.extend(get_store_id(driver))

        except Exception as e:
            print("Error", e)
            break
    print(store_list1)
    all_match=all(storeid==store for storeid in store_list1)

    if all_match:
        print(f"All store match data, case Pass!!!: {store}")
    else:
        print(f"Store doesn't all match:{store}")        

def get_sub_id(driver:webdriver.Chrome):

    sub_id=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[18]")
    return [(sub.text) for sub in sub_id]
def fee_record_3PL_1577(driver:webdriver.Chrome):


    sub_id_list=[]
    invoice_button=driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item']")
    invoice_button.click()
    time.sleep(1)

    Sub_Order_button=driver.find_element(By.XPATH, "//span[text()='Sub-Order No.']")
    Sub_Order_button.click()
    time.sleep(1)

    sub='H240226000008-B9069002'
    close_button=driver.find_element(By.XPATH, "//span[contains(@class,'ant-input-clear-icon ant-input-clear-icon-has-suffix')]")
    close_button.click()
    search_Sub_Order=driver.find_element(By.XPATH, "//input[contains(@data-testid,'input')]")
    search_Sub_Order.send_keys(f"{sub}")
    time.sleep(1)

    Search_button=driver.find_element(By.XPATH, "//div[contains(@data-testid,'search')]")
    Search_button.click()
    time.sleep(1)

    sub_id_list.extend(get_sub_id(driver))

    while True:
        try:
            next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
            next_page=next_page_button.get_attribute("class")

            if "ant-pagination-disabled" in next_page:
                break
            next_page_button.click()
            time.sleep(1)
            sub_id_list.extend(get_store_id(driver))

        except Exception as e:
            print("Error", e)
            break
    print(sub_id_list)
    all_match=all(subid==sub for subid in sub_id_list)

    if all_match:
        print(f"All store match data, case Pass!!!:{sub}")
    else:
        print(f"Store doesn't all match:{sub}") 
def get_waybill_No(driver:webdriver.Chrome):

    waybill=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[19]")
    return [(Waybill.text) for Waybill in waybill]
def fee_record_3PL_1578(driver:webdriver.Chrome):


    waybill_list=[]
    invoice_button=driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item']")
    invoice_button.click()
    time.sleep(1)

    waybill_button=driver.find_element(By.XPATH, "//span[text()='Waybill No.']")
    waybill_button.click()
    time.sleep(1)

    waybill_id='TA00001627'
    close_button=driver.find_element(By.XPATH, "//span[contains(@class,'ant-input-clear-icon ant-input-clear-icon-has-suffix')]")
    close_button.click()
    search_waybill=driver.find_element(By.XPATH, "//input[contains(@data-testid,'input')]")
    search_waybill.send_keys(f"{waybill_id}")
    time.sleep(1)

    Search_button=driver.find_element(By.XPATH, "//div[contains(@data-testid,'search')]")
    Search_button.click()
    time.sleep(1)

    waybill_list.extend(get_waybill_No(driver))

    while True:
        try:
            next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
            next_page=next_page_button.get_attribute("class")

            if "ant-pagination-disabled" in next_page:
                break
            next_page_button.click()
            time.sleep(1)
            waybill_list.extend(get_waybill_No(driver))

        except Exception as e:
            print("Error", e)
            break
    print(waybill_list)
    all_match=all(waybil==waybill_id for waybil in waybill_list)

    if all_match:
        print(f"All store match data, case Pass!!!:{waybill_id}")
    else:
        print(f"Store doesn't all match:{waybill_id}")   
def get_booking_list(driver:webdriver.Chrome):

    booking_no=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[17]")
    return [(booking.text) for booking in booking_no]
def fee_record_3PL_1579(driver:webdriver.Chrome):


    booking_list=[]
    invoice_button=driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item']")
    invoice_button.click()
    time.sleep(1)

    booking_button=driver.find_element(By.XPATH, "//span[text()='Booking No.']")
    booking_button.click()
    time.sleep(1)

    Booking_No='SITY3F00002374'
    close_button=driver.find_element(By.XPATH, "//span[contains(@class,'ant-input-clear-icon ant-input-clear-icon-has-suffix')]")
    close_button.click()
    search_Booking_No=driver.find_element(By.XPATH, "//input[contains(@data-testid,'input')]")
    search_Booking_No.send_keys(f"{Booking_No}")
    time.sleep(1)

    Search_button=driver.find_element(By.XPATH, "//div[contains(@data-testid,'search')]")
    Search_button.click()
    time.sleep(1)

    booking_list.extend(get_booking_list(driver))

    while True:
        try:
            next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
            next_page=next_page_button.get_attribute("class")

            if "ant-pagination-disabled" in next_page:
                break
            next_page_button.click()
            time.sleep(1)
            booking_list.extend(get_booking_list(driver))

        except Exception as e:
            print("Error", e)
            break
    print(booking_list)
    all_match=all(booking==Booking_No for booking in booking_list)

    if all_match:
        print(f"All store match data, case Pass!!!{Booking_No}")
        time.sleep(1)
    else:
        print(f"Store doesn't all match:{Booking_No}")  
        time.sleep(1)
def get_fee_record_id(driver:webdriver.Chrome):

    fee_record_id=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[1]")
    return [(fee_record.text) for fee_record in fee_record_id]
def fee_record_3PL_fee_id(driver:webdriver.Chrome):


    fee_record_id_list=[]
    invoice_button=driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item']")
    invoice_button.click()
    time.sleep(1)

    booking_button=driver.find_element(By.XPATH, "(//span[text()='Fee Record ID'])[2]")
    booking_button.click()
    time.sleep(1)

    fee_record='9924'
    close_button=driver.find_element(By.XPATH, "//span[contains(@class,'ant-input-clear-icon ant-input-clear-icon-has-suffix')]")
    close_button.click()
    search_Booking_No=driver.find_element(By.XPATH, "//input[contains(@data-testid,'input')]")
    search_Booking_No.send_keys(f"{fee_record}")
    time.sleep(1)

    Search_button=driver.find_element(By.XPATH, "//div[contains(@data-testid,'search')]")
    Search_button.click()
    time.sleep(1)

    fee_record_id_list.extend(get_fee_record_id(driver))

    
    print(fee_record_id_list)
    all_match=all(fee==fee_record for fee in fee_record_id_list)

    if all_match:
        print(f"fee_record match data, case Pass!!!:{fee_record}")
        time.sleep(1)
    else:
        print(f"fee doesn't all match:{fee_record}") 
        time.sleep(1)  
if __name__=='__main__':
    
    driver=create_chrome_driver()
    wait = WebDriverWait(driver, 10)
    login_MMS(driver)
    
    fee_record_3PL_312(driver)
    time.sleep(2)
    fee_record_3PL_1146(driver)
    time.sleep(2)
    fee_record_3PL_1577(driver)
    time.sleep(2)
    fee_record_3PL_1578(driver)
    time.sleep(2)
    fee_record_3PL_1579(driver)
    time.sleep(2)
    fee_record_3PL_fee_id(driver)
    time.sleep(2)
    driver.quit()