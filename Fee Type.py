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
    url2=f"https://mms-staging.hkmpcl.com.hk/en/payment/fee-record"
    driver.get(url2)
    time.sleep(2)
def get_filter_data(driver:webdriver.Chrome):

    fee_type=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[2]")
    
    return [fee.text for fee in fee_type]  

def fee_record_filter_3PL_314(driver:webdriver.Chrome):
    try:
        fee_list=[]
        fee_type=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[2]")
        fee_type.click()
        time.sleep(2)
        Test_fee='Storage Fee'
        storage=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[2]")
        storage.click()
        time.sleep(1)

        Apply=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'Apply')]")
        Apply.click()
        time.sleep(2)

        fee_list.extend(get_filter_data(driver))

        while True:
            try:   
                next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
                next_button=next_page_button.get_attribute("class")

                if "ant-pagination-disabled" in next_button:
                    break

                next_page_button.click()
                time.sleep(2)

                fee_list.extend(get_filter_data(driver))
            except Exception as e:
                print("Error navigating to next page:", e)
                break
        print(fee_list)
        all_match=all(Fee_Type==Test_fee for Fee_Type in fee_list)
        if all_match:
            print(f"All invoice values match the search value: {Test_fee}")

        else:
            print(f"Not all invoice values match the search value: {Test_fee}")
    except Exception as e:
        print("Error",e)
def fee_record_filter_3PL_315(driver:webdriver.Chrome):

    multiple_fee_list=[]

    #這裡放要測試的fee
    Test_list=['Storage Fee','Tote Deposit','Stock-in Fee','Pick-pack Fee (First Item)']

    fee_type=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[2]")
    fee_type.click()
    time.sleep(2)
    storage=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[2]")
    storage.click()
    time.sleep(2)

    deposit=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[16]")
    deposit.click()
    time.sleep(2)

    stock_in=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[4]")
    stock_in.click()
    time.sleep(2)

    pick_pack=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[24]")
    pick_pack.click()
    Apply=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'Apply')]")
    Apply.click()
    time.sleep(2)
    multiple_fee_list.extend(get_filter_data(driver))

    while True:
        try:   
            next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
            next_button=next_page_button.get_attribute("class")

            if "ant-pagination-disabled" in next_button:
                break

            next_page_button.click()
            time.sleep(2)

            multiple_fee_list.extend(get_filter_data(driver))
        except Exception as e:
            print("Error navigating to next page:", e)
            break
    print(multiple_fee_list)
    all_match=all(Fee_Type in Test_list for Fee_Type in multiple_fee_list)
    if all_match:
        print(f"All invoice values match the search value: {multiple_fee_list} case Pass!!!")

    else:
        print(f"Not all invoice values match the search value: {multiple_fee_list}")


if __name__=='__main__':
    driver=create_chrome_driver()
    wait = WebDriverWait(driver, 10)
    login_MMS(driver)
    fee_record_filter_3PL_314(driver)
    fee_record_filter_3PL_315(driver)
    driver.quit()