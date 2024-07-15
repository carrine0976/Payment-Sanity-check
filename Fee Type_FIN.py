import  time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import os


def create_chrome_driver(download_path:str)->webdriver.Chrome:
    options=Options()
    options.add_argument("--start-maximized")
    prefs={
        "download.default_directory":download_path,
        "download.prompt_for_download":False,
        "download.directory_upgrade":True,
        "safebrowsing.enable":True
    }
    options.add_experimental_option("prefs",prefs)
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
def get_filter_data(driver:webdriver.Chrome):

    fee_type=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[2]")
    
    return [fee.text for fee in fee_type]  

def fee_record_filter_3PL_341(driver:webdriver.Chrome):
    try:
        fee_list=[]
        fee_type=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[2]")
        fee_type.click()
        time.sleep(2)
        Test_fee='Stock-in Fee'
        Stock_in=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[4]")
        Stock_in.click()
        time.sleep(2)

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
                time.sleep(0.5)

                fee_list.extend(get_filter_data(driver))
            except Exception as e:
                print("Error navigating to next page:", e)
                break
        print(fee_list)
        all_match=all(Fee_Type==Test_fee for Fee_Type in fee_list)
        if all_match:
            print("\n")
            print(f"All Fee Type match the search value: {Test_fee} case 341 Pass!!!")

        else:
            print(f"Not all Fee Type match the search value: {Test_fee}")
        
        clear_button=driver.find_element(By.XPATH, "//button[@data-testid='Clear All']")
        clear_button.click()
        time.sleep(3)

    except Exception as e:
        print("Error",e)

def fee_record_filter_3PL_342_343(driver:webdriver.Chrome):

    multiple_fee_list=[]

    #這裡放要測試的fee
    Test_list=['Stock-out Fee','Penalty - Damage & Lost Tote']

    fee_type=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[2]")
    fee_type.click()
    time.sleep(2)
    Stockout=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[5]")
    Stockout.click()
    time.sleep(2)

    Penalty=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[13]")
    Penalty.click()
    time.sleep(2)

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
            time.sleep(0.5)

            multiple_fee_list.extend(get_filter_data(driver))
        except Exception as e:
            print("Error navigating to next page:", e)
            break
    print(multiple_fee_list)
    all_match=all(Fee_Type in Test_list for Fee_Type in multiple_fee_list)
    if all_match:
        print("\n")
        print(f"Fee Type  match the search value: {multiple_fee_list} case 342 343 Pass!!!")

    else:
        print(f"Not all Fee Type match the search value: {multiple_fee_list}")
    
    clear_button=driver.find_element(By.XPATH, "//button[@data-testid='Clear All']")
    clear_button.click()
    time.sleep(3)

def fee_record_filter_3PL_1624(driver:webdriver.Chrome):
    multiple_fee_list=[]
    Test_list=['Pick-pack Special Handling Fee (Extra Fragile SKU)']

    fee_type=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[2]")
    fee_type.click()
    time.sleep(2)
    Pick_pack=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[27]")
    Pick_pack.click()
    time.sleep(2)

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
            time.sleep(0.5)

            multiple_fee_list.extend(get_filter_data(driver))
        except Exception as e:
            print("Error navigating to next page:", e)
            break
    print(multiple_fee_list)
    all_match=all(Fee_Type in Test_list for Fee_Type in multiple_fee_list)
    if all_match:
        print("\n")
        print(f"Fee Type match the search value: {multiple_fee_list} case 1624 Pass!!!")

    else:
        print(f"Not all Fee Type match the search value: {multiple_fee_list}")

def fee_record_filter_3PL_1625(driver:webdriver.Chrome):
    multiple_fee_list=[]
    Test_list=['Pick-pack Fee (First Item)']

    fee_type=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[2]")
    fee_type.click()
    time.sleep(2)
    Pick_pack=driver.find_element(By.XPATH, "(//input[contains(@class,'ant-checkbox-input')])[24]")
    Pick_pack.click()
    time.sleep(2)

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
            time.sleep(0.5)

            multiple_fee_list.extend(get_filter_data(driver))
        except Exception as e:
            print("Error navigating to next page:", e)
            break
    print(multiple_fee_list)
    all_match=all(Fee_Type in Test_list for Fee_Type in multiple_fee_list)
    if all_match:
        print("\n")
        print(f"Fee Type match the search value: {multiple_fee_list} case 1624 Pass!!!")

    else:
        print(f"Not all Fee Type match the search value: {multiple_fee_list}")

def get_filter_data_isFragile(driver:webdriver.Chrome):
    is_fragile=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[5]")
    return [fragile.text for fragile in is_fragile]

def get_filter_data_isFragile(driver:webdriver.Chrome):
    is_fragile=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[5]")
    return [fragile.text for fragile in is_fragile]
def get_data_result(driver:webdriver.Chrome):
    amount=driver.find_element(By.XPATH, "//div[@class='text-60% undefined']")
    return amount.text 

def fee_record_filter_3PL_1595(driver:webdriver.Chrome):
    Total_result=[]
    Test_Total_result=[]
    Total_result.append(get_data_result(driver))
    print(f"default result 數量:{Total_result}")
    Yes_or_No=[]
    Yes_or_No2=[]
    Test_list1=['Yes']
    Test_list2=['No']

    isfraile=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[3]")
    isfraile.click()
    time.sleep(2)
    yes=driver.find_element(By.XPATH, "//div[@class='dropdown__group__label' and text()='Yes']")
    yes.click()
    time.sleep(2)

    Apply=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'Apply')]")
    Apply.click()
    time.sleep(2)
    Yes_or_No.extend(get_filter_data_isFragile(driver))

    while True:
        try:   
            next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
            next_button=next_page_button.get_attribute("class")

            if "ant-pagination-disabled" in next_button:
                break

            next_page_button.click()
            time.sleep(0.5)

            Yes_or_No.extend(get_filter_data_isFragile(driver))
        except Exception as e:
            print("Error navigating to next page:", e)
            break
    print(Yes_or_No)
    all_match=all(isfragile in Test_list1 for isfragile in Yes_or_No)
    if all_match:
        print("\n")
        print(f"Fee Type match the search value: {Yes_or_No} case Pass!!!")

    else:
        print(f"Not all Fee Type match the search value: {Yes_or_No}")
    isfragile=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[3]")
    isfragile.click()
    time.sleep(2)
    no=driver.find_element(By.XPATH, "//div[@class='dropdown__group__label' and text()='No']")
    no.click()
    time.sleep(2)

    Apply=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'Apply')]")
    Apply.click()
    time.sleep(2)
    Yes_or_No2.extend(get_filter_data_isFragile(driver))

    while True:
        try:   
            next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
            next_button=next_page_button.get_attribute("class")

            if "ant-pagination-disabled" in next_button:
                break

            next_page_button.click()
            time.sleep(2)

            Yes_or_No2.extend(get_filter_data_isFragile(driver))
        except Exception as e:
            print("Error navigating to next page:", e)
            break
    print(Yes_or_No2)
    all_match=all(isfragile in Test_list2 for isfragile in Yes_or_No2)
    if all_match:
        print("\n")
        print(f"Fee Type match the search value: {Yes_or_No2} case 1595 Pass!!!")

    else:
        print(f"Not all Fee Type match the search value: {Yes_or_No2}")

    isfraile=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[3]")
    isfraile.click()
    time.sleep(2)
    clear_button=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'Clear All')]")
    clear_button.click()
    time.sleep(2)
    
    Test_Total_result.append(get_data_result(driver))
    match=all(clear_up ==Test_Total_result[0] for clear_up in Total_result)
    print(f"按完clear button 的result 數量:{Test_Total_result}")

    if match:
        print("clear up result successfully")
    else:
        print("Clear up result fail")

def get_filter_data_is_Extra_Fragile(driver:webdriver.Chrome):
    is_Extra_fragile=driver.find_elements(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@class='ant-table-row ant-table-row-level-0 cell-medium']/td[6]")
    return [fragile.text for fragile in is_Extra_fragile]


def fee_record_filter_3PL_1599_1(driver:webdriver.Chrome):
    try:
        result=[]
        result.append(get_data_result(driver))
        print(f"default result 數量:{result}")
        Yes_or_No=[]
        
        Test_list1=['Yes']
        

        is_Extra_fragile=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[4]")
        is_Extra_fragile.click()
        time.sleep(2)
        Yes=driver.find_element(By.XPATH, "(//div[@class='dropdown__group__label'])[1]")
        Yes.click()
        time.sleep(2)

        Apply=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'Apply')]")
        Apply.click()
        time.sleep(2)
        Yes_or_No.extend(get_filter_data_is_Extra_Fragile(driver))

        while True:
            try:   
                next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
                next_button=next_page_button.get_attribute("class")

                if "ant-pagination-disabled" in next_button:
                    break

                next_page_button.click()
                time.sleep(2)

                Yes_or_No.extend(get_filter_data_is_Extra_Fragile(driver))
            except Exception as e:
                print("Error navigating to next page:", e)
                break
        print(Yes_or_No)
        all_match=all(isfragile in Test_list1 for isfragile in Yes_or_No)
        if all_match:
            print("\n")
            print(f"Fee Type match the search value: {Yes_or_No} case Pass!!!")

        else:
            print(f"Not all Fee Type match the search value: {Yes_or_No}")
    except Exception as e:
        print("Error",e)

def fee_record_filter_3PL_1599_2(driver:webdriver.Chrome):
    Test_list2=['No']
    Yes_or_No2=[]
    result=[]
    try:
        is_Extra_fraile=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[4]")
        is_Extra_fraile.click()
        time.sleep(2)
        no=driver.find_element(By.XPATH, "(//div[@class='dropdown__group__label'])[2]")
        no.click()
        time.sleep(2)

        Apply=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'Apply')]")
        Apply.click()
        time.sleep(2)
        Yes_or_No2.extend(get_filter_data_is_Extra_Fragile(driver))

        while True:
            try:   
                next_page_button=driver.find_element(By.XPATH, "//li[@title='Next Page']")
                next_button=next_page_button.get_attribute("class")

                if "ant-pagination-disabled" in next_button:
                    break

                next_page_button.click()
                time.sleep(2)

                Yes_or_No2.extend(get_filter_data_is_Extra_Fragile(driver))
            except Exception as e:
                print("Error navigating to next page:", e)
                break
        print(Yes_or_No2)
        all_match=all(isfragile in Test_list2 for isfragile in Yes_or_No2)
        if all_match:
            print("\n")
            print(f"Fee Type match the search value: {Yes_or_No2} case 1599 Pass!!!")

        else:
            print(f"Not all Fee Type match the search value: {Yes_or_No2}")
        isfragile=driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[4]")
        isfragile.click()
        time.sleep(2)
        clear_button=driver.find_element(By.XPATH, "(//button[contains(@data-testid, 'Clear All')])[2]")
        clear_button.click()
        time.sleep(2)
        Apply2=driver.find_element(By.XPATH, "//button[contains(@data-testid, 'Apply')]")
        Apply2.click()
        time.sleep(2)
        
        Test_result=[]
        Test_result.append(get_data_result(driver))
        print(f"按完clear button 的result 數量:{Test_result}")
        match=all(clear_up ==Test_result[0] for clear_up in result)

        if match:
            print("clear up result successfully")
        else:
            print("Clear up result fail")

    except Exception as e:
        print("Error",e)

def export(driver:webdriver.Chrome):
    export_button=driver.find_element(By.XPATH, "//button[@data-testid='Export']")
    export_button.click()
    time.sleep(2)
    today_date=datetime.now().strftime("%Y%m%d")
    before_date=today_date-timedelta(days=60)
    file_name=f"FeeRecord_{before_date}-{today_date}"
    download_file=os.listdir(download_path)
    matching_file=[f for f in download_file if file_name in f ]
    if matching_file:
        print(f"{file_name}")
        print("Export Successfully, CASE 1604 PASS!!")
    else:
        print("CASE 1604 FAIL")

if __name__=='__main__':
    download_path=r"C:\Users\carrine.shih\Downloads"
    driver=create_chrome_driver(download_path)
    wait = WebDriverWait(driver, 10)
    
    login_MMS(driver)
    fee_record_filter_3PL_341(driver)
    time.sleep(2)
    fee_record_filter_3PL_342_343(driver)
    time.sleep(2)
    fee_record_filter_3PL_1624(driver)
    time.sleep(2)
    fee_record_filter_3PL_1625(driver)
    time.sleep(2)
    fee_record_filter_3PL_1595(driver)
    time.sleep(2)
    fee_record_filter_3PL_1599_1(driver)
    time.sleep(2)
    fee_record_filter_3PL_1599_2(driver)
    time.sleep(2)
    export(driver)
    time.sleep(2)
    driver.quit()