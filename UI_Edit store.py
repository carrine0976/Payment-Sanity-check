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

def fee_record_3PL_311(driver:webdriver.Chrome):
    list=[]
    list2=[]
    text=[]
    text2=[]
    span=[]
    filter_list=[]
    expect_list1=['Fee Record ID','Fee Type','Store ID','SKU ID','Is Fragile','Is Extra Fragile','Is Sensitive','Unit Price','QTY','Total Price']
    expect_list2=['Last Updated Date','Invoice No.','Plan Type']       
    expect_text=['Settlement Status','Period Cover','Subscription No.']
    expect_text2=['Booking No.','Sub-Order No.','Waybill No.','Waybill Status']
    span_tab=['Invoice No.','Store ID','SKU ID','Sub-Order No.','Waybill No.','Booking No.','Fee Record ID']
    expect_filter=['Fee Type','Is Fragile','Is Extra Fragile','Settlement Status','Last Updated Date']
    try:
        url=f"https://mms-staging.hkmpcl.com.hk/payment/fee-record"
        driver.get(url)
        print("開始檢查search bar")
        time.sleep(0.5)
        invoice_button=driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item']")
        invoice_button.click()
        time.sleep(1)

        invoice=driver.find_element(By.XPATH, "(//span[text()='Invoice No.'])[3]").text
        span.append(invoice)
        print(f"Tab:{invoice}")
        time.sleep(0.5)

        Store=driver.find_element(By.XPATH, "(//span[text()='Store ID'])[2]").text
        span.append(Store)
        print(f"Tab:{Store}")
        time.sleep(0.5)

        SKUID=driver.find_element(By.XPATH, "(//span[text()='SKU ID'])[2]").text
        span.append(SKUID)
        print(f"Tab:{SKUID}")
        time.sleep(0.5)

        Sub_Order=driver.find_element(By.XPATH, "//span[text()='Sub-Order No.']").text
        span.append(Sub_Order)
        print(f"Tab:{Sub_Order}")
        time.sleep(0.5)

        Waybill_No=driver.find_element(By.XPATH, "//span[text()='Waybill No.']").text
        span.append(Waybill_No)
        print(f"Tab:{Waybill_No}")
        time.sleep(0.5)

        Booking=driver.find_element(By.XPATH, "//span[text()='Booking No.']").text
        span.append(Booking)
        print(f"Tab:{Booking}")
        time.sleep(0.5)

        Fee_Record_ID=driver.find_element(By.XPATH, "(//span[text()='Fee Record ID'])[2]").text
        span.append(Fee_Record_ID)
        print(f"Tab:{Fee_Record_ID}")
        time.sleep(0.5)

        assert operator.eq(span,span_tab),"Headers do not match expected values." 
        print("Data are all match!!!!")
        print("\n")

        
        print("開始檢查table items")
        time.sleep(0.5)
        for i in range(1,11):
            table_head=driver.find_element(By.XPATH, f"(//th[@class='ant-table-cell ant-table-column-has-sorters'])[{i}]")
            table_text=table_head.text
            list.append(table_text)
            print(f"Header:{table_text}")
            time.sleep(1)

        assert operator.eq(list,expect_list1), "Headers do not match expected values."            
        print("Header assertion passed for expect_list1")
        print("\n")

        script = "document.querySelector('.ant-table-body').scrollLeft += 10000;"  
        driver.execute_script(script)
        time.sleep(2) 

        for i in range(11,14):     
            table_head2=driver.find_element(By.XPATH, f"(//th[@class='ant-table-cell ant-table-column-has-sorters'])[{i}]")
            table_head2=table_head2.text
            list2.append(table_head2)
            print(f"Header:{table_head2}")
            time.sleep(0.5)

        assert operator.eq(list2,expect_list2), "Headers do not match expected values." 
        print("Headers match expected_text.")
        time.sleep(1)

        script = "document.querySelector('.ant-table-body').scrollLeft -= 500;"  
        driver.execute_script(script)
        time.sleep(2)
        print("開始檢查table items -->text")
        for i in range(1,4):
            text_=driver.find_element(By.XPATH, f"(//th[@class='ant-table-cell'])[{i}]")
            text_text=text_.text
            text.append(text_text)
            print(f"Header:{text_text}")
            time.sleep(0.5)
        assert operator.eq(text,expect_text), "Headers do not match expected values." 
        print("Header assertion passed for expect_text")
        time.sleep(1)

        script = "document.querySelector('.ant-table-body').scrollLeft += 10000;"  
        driver.execute_script(script)
        time.sleep(2)

        for i in range(4,8):

            text2_=driver.find_element(By.XPATH, f"(//th[@class='ant-table-cell'])[{i}]")
            text_text2=text2_.text
            text2.append(text_text2)
            print(f"Header:{text_text2}")
            time.sleep(0.5)

        assert operator.eq(text2,expect_text2), "Headers do not match expected values." 
        print("Header assertion passed for expect_text2")
        print("\n")
        time.sleep(1)
        print("開始檢查filter")
        time.sleep(0.5)

        for i in range(1,6):
            filter_type=driver.find_element(By.XPATH, f"(//span[@class='ant-select-selection-placeholder'])[{i}]")
            filter_text=filter_type.text
            filter_list.append(filter_text)
            print(f"filetr_text:{filter_text}")
            time.sleep(0.5)

        assert operator.eq(filter_list,expect_filter),"Headers do not match expected values." 
        print("Data are all match!!!1")
        print("\n")

    except Exception as e:
        print("Element not found:", e)

def fee_record_3PL_317(driver:webdriver.Chrome):
    try:
       
        select_edit_store=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'Edit Store')]")
        select_edit_store.click()
        time.sleep(2)
        radio_value = "B9069001"
        select_store=driver.find_element(By.XPATH, f"//input[contains(@value,'{radio_value}')]")
        select_store.click()
        time.sleep(2)

        save=driver.find_element(By.XPATH, "//button[@class='ant-btn css-1tpk6qc ant-btn-primary button--root']")
        save.click()
        time.sleep(2)

        confirm=driver.find_element(By.XPATH, "//button[@class='ant-btn css-1tpk6qc ant-btn-primary button--root']")
        confirm.click()
        time.sleep(2)
    except Exception as e:
        print("Element not found", e)

def fee_record_3PL_318(driver:webdriver.Chrome):
    list=[]
    expected_headers=['Update Time','Original Deduct Store','Current Deduct Store','Account Name']
    try:
        view_history=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'View History')]")
        view_history.click()
        time.sleep(1)
        print("開始檢查Update History table")
        for i in range(8,12):
            table_head=driver.find_element(By.XPATH, f"(//th[@class='ant-table-cell'])[{i}]")
            table_text=table_head.text
            list.append(table_text)
            print(f"Header{i-7}:{table_text}")
            time.sleep(0.5)
            

        assert  operator.eq(list,expected_headers),"Headers do not match expected values."
        print("Header assertion passed for expect_headers")
        print("\n")
        
    except Exception as e:
        print("Element not found", e)
  
if __name__=='__main__':
    
    driver=create_chrome_driver()
    wait = WebDriverWait(driver, 10)
    login_MMS(driver)
    fee_record_3PL_311(driver)
    time.sleep(2)

    fee_record_3PL_317(driver)
    time.sleep(2)

    fee_record_3PL_318(driver)
    time.sleep(2)

    
    driver.quit()