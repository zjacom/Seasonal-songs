import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    URL = "https://www.melon.com/chart/index.htm"
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    driver.get(URL)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span')))
    except TimeoutException:
        print("페이지 로딩 시간 초과")
        driver.quit()
        return

    finder_tab = driver.find_element(By.XPATH,'//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span')
    finder_tab.click()
    time.sleep(1)
    
    weekly_chart = driver.find_element(By.XPATH,'//*[@id="d_chart_search"]/div/h4[1]')
    weekly_chart.click()
    time.sleep(1)

    # 메세지 확인용 변수
    decade_mapping = {1: '2020년대', 2: '2010년대'}
    year_offset = {1: (2024, -1), 2: (2019, -1)}  # (시작 연도, 증감량)
    for years in range(1, 3):
        decade_text = decade_mapping.get(years, "알 수 없는 년대")
        try:
            years_btn = driver.find_element(By.XPATH,f'//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[{years}]')
            years_btn.click()
            time.sleep(1)
        except NoSuchElementException:
            print(f"{decade_text} 구간의 데이터가 존재하지 않습니다.")
            continue

        # 연도선택
        start_year, year_change = year_offset[years]
        if years == 1 : # 2020년대
            for year_index in range(1, 6): # 2024,2023,2022,2021,2020 년대만 조회.
                year = start_year + (year_index - 1) * year_change
                try:
                    year_btn = driver.find_element(By.XPATH,f'//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[{year_index}]')
                    year_btn.click()
                    time.sleep(1)
                except NoSuchElementException:
                    print(f"{decade_text} 구간의 {year}년 데이터가 존재하지 않습니다.")
                    continue
                # 월간선택 ( 봄 : 3,4,5 겨울 1,2,12)
                target_month = [1,2,3,4,5,12]
                for month in target_month:
                    try:
                        month_btn = driver.find_element(By.XPATH,f'//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[{month}]')
                        month_btn.click()
                        time.sleep(1)
                    except NoSuchElementException:
                        print(f"{year}년 {month}월 데이터가 존재하지 않습니다.")
                        continue
                    
                    # 주간선택
                    for week in range(1, 6):
                        try:
                            week_btn = driver.find_element(By.XPATH,f'//*[@id="d_chart_search"]/div/div/div[4]/div[1]/ul/li[{week}]')
                            week_btn.click()                          
                            time.sleep(1)
                        except NoSuchElementException:
                            print(f"{year}년 {month}월 {week}주차 데이터가 존재하지 않습니다.")
                            break  # 해당 월의 주차가 더 이상 존재하지 않으므로 더 이상의 반복을 중단합니다.
                        
                        # 장르선택
                        try:
                            genre_btn = driver.find_element(By.XPATH,"""//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]""")
                            genre_btn.click()
                            search_btn = driver.find_element(By.XPATH,"""//*[@id="d_srch_form"]/div[2]/button""")
                            search_btn.click()
                            time.sleep(1)
                        except NoSuchElementException:
                            print(f"{year}년 {month}월 {week}주차의 장르종합 데이터가 존재하지 않습니다.")
                            continue
        else : 
            for year_index in range(1, 11): # 2019, 2018, ... 2010 년대 조회.
                year = start_year + (year_index - 1) * year_change
                try:
                    year_btn = driver.find_element(By.XPATH,f'//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[{year_index}]')
                    year_btn.click()
                    time.sleep(1)
                except NoSuchElementException:
                    print(f"{decade_text} 구간의 {year}년 데이터가 존재하지 않습니다.")
                    continue

                # 월간선택 ( 봄 : 3,4,5 겨울 1,2,12)
                target_month = [1,2,3,4,5,12]
                for month in target_month:
                    try:
                        month_btn = driver.find_element(By.XPATH,f'//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[{month}]')
                        month_btn.click()
                        time.sleep(1)
                    except NoSuchElementException:
                        print(f"{year}년 {month}월 데이터가 존재하지 않습니다.")
                        continue

                    # 주간선택
                    for week in range(1, 6):
                        try:
                            week_btn = driver.find_element(By.XPATH,f'//*[@id="d_chart_search"]/div/div/div[4]/div[1]/ul/li[{week}]')
                            week_btn.click()                          
                            time.sleep(1)
                        except NoSuchElementException:
                            print(f"{year}년 {month}월 {week}주차 데이터가 존재하지 않습니다.")
                            break  # 해당 월의 주차가 더 이상 존재하지 않으므로 더 이상의 반복을 중단합니다.

                        # 장르선택
                        try:
                            genre_btn = driver.find_element(By.XPATH,"""//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]""")
                            genre_btn.click()
                            search_btn = driver.find_element(By.XPATH,"""//*[@id="d_srch_form"]/div[2]/button""")
                            search_btn.click()
                            time.sleep(1)
                        except NoSuchElementException:
                            print(f"{year}년 {month}월 {week}주차의 장르종합 데이터가 존재하지 않습니다.")
                            continue

                        
                        # 페이지 로딩과 서버 부하를 고려하여 적당한 대기 시간 추가
                        # WebDriverWait(driver, 10).until(EC.staleness_of(week_btn))

    print("종료.")
    driver.quit()

if __name__ == '__main__':
    main()

