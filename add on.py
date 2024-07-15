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
import re,operator
DELAY=time.sleep(6)

def create_chrome_driver()->webdriver.Chrome:
    options=Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

def fee_record_add_on_storage(driver:webdriver.Chrome,account:str,password:str,add_on_storage:str):

    url=f"https://mms-staging.hkmpcl.com.hk/en/login"
    driver.get(url)
    DELAY
    fill_in_account=driver.find_element(By.ID,"account")
    fill_in_account.send_keys(f"{account}")
    time.sleep(2)

    fill_in_pwd=driver.find_element(By.ID,"password")
    fill_in_pwd.send_keys(f"{password}")

    login_click=driver.find_element(By.XPATH,"//button[@data-testid='Continue']")
    login_click.click()
    time.sleep(3)
    url3=f"https://mms-staging.hkmpcl.com.hk/account"
    driver.get(url3)
    time.sleep(5)
    storage_fee=driver.find_element(By.XPATH, "(//div[@class='ant-col css-1tpk6qc'])[17]")
    storage_fee_per_tote=storage_fee.text
    a=int(storage_fee_per_tote[1:3])
    print(f"{a}")
    DELAY
    subscription=driver.find_element(By.XPATH, "(//div[@class='ant-col css-1tpk6qc'])[8]")
    subscription_text=subscription.text
    subscription_date=int(subscription_text[-1])
    print(f"{subscription_date}")
    DELAY

   
    
    url2=f"https://mms-staging.hkmpcl.com.hk/3pl-management/storage-space/dashboard"
    driver.get(url2)
    time.sleep(8)

    Add_on_storage=driver.find_element(By.XPATH, "//button[@data-testid='Add-On Storage']")
    Add_on_storage.click()
    DELAY

    input_amount=driver.find_element(By.XPATH, "//input[@data-testid='inputNumber']")
    input_amount.send_keys(f"{add_on_storage}")
    DELAY

    apply=driver.find_element(By.XPATH, "//button[@data-testid='Apply']")
    apply.click()
    time.sleep(8)

    upgrade_button=driver.find_element(By.XPATH, "//button[@data-testid='Upgrade Subscription']")
    upgrade_button.click()
    time.sleep(8)

    today=datetime.now()
    current_month=today.month
    print(f"當天日期:{today}")
    print(f"當月月份:{current_month}")

    
    '''計算當期合約剩餘天數'''
    if subscription_date<today.day:
        contract_start_date=datetime(today.year,current_month+1,subscription_date)
        print(f"下期合約日期:{contract_start_date}")
    else :
        contract_start_date=datetime(today.year,current_month,subscription_date)
        print(f"下期合約日期:{contract_start_date}")
    remaining_days=(contract_start_date-today).days
    print(f"本期剩餘天數:{remaining_days}")

    '''計算當期合約天數'''
    if current_month/2!=0 :
        month=int(31)
        print(f"當期合約天數:{month}")
    elif current_month/2==0:
        month=int(30)
        print(f"當期合約天數:{month}")
    add_on_storage_=int(add_on_storage)
    add_on_storage_fee=round((((add_on_storage_*a)/month)*(remaining_days+1)),2)
    print(f"Add on storage Fee 預期為: {add_on_storage_fee}")

    url4=f"https://mms-staging.hkmpcl.com.hk/payment/fee-record"
    driver.get(url4)
    time.sleep(10)
    Total_price=driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[@data-row-key='14726']/td[10]")
    Total_price_text=Total_price.text
    match =re.search(r'HKD \$([\d,\.]+)',Total_price_text)
    if match :
        number=float(match.group(1).replace(',',''))
        print(f"MMS顯示價格:{number}")
    assert operator.eq(number,add_on_storage_fee),"add on storage fee not correct"
    print("CASE 248 PASS!!")
if __name__=='__main__':
    account="carrine.shih+26@shoalter.com"
    password="Gmjmr3SQGnx7"
    add_on_storage="100"
    driver=create_chrome_driver()
    wait = WebDriverWait(driver, 10)
    fee_record_add_on_storage(driver,account=account,password=password,add_on_storage=add_on_storage)
    
