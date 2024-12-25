from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Chrome 옵션 설정
options = Options()
options.add_argument('--headless')  # GUI 없이 실행
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def get_news(ticker_symbol): #주식 티커 입력
    # WebDriver 생성
    driver = webdriver.Chrome(options=options)

    # URL 설정
    url = f'https://finance.yahoo.com/quote/{ticker_symbol}/news/'
    driver.get(url)

    # 페이지 로드 대기
    time.sleep(5)

    # 뉴스 헤드라인 추출
    data = pd.DataFrame(index=range(20), columns=['title', 'content', 'link'])  # DataFrame 생성

    for i in range(1, 21):  # li 요소의 인덱스 범위 - 20 몇개씩 스크롤 필요
        try:
            xpath = f'/html/body/div[2]/main/section/section/section/article/section[2]/section/div/div/div/div/ul/li[{i}]/section/div/a/h3'
            time.sleep(1)# 페이지 로드 대기

            title_element = driver.find_element(By.XPATH, xpath)
            title_text = title_element.text

            xpath = f'/html/body/div[2]/main/section/section/section/article/section[2]/section/div/div/div/div/ul/li[{i}]/section/div/a/p'
            time.sleep(1)# 페이지 로드 대기

            content_element = driver.find_element(By.XPATH, xpath)
            content_text = content_element.text

            xpath = f'/html/body/div[2]/main/section/section/section/article/section[2]/section/div/div/div/div/ul/li[{i}]/section/div/a'
            time.sleep(1)# 페이지 로드 대기

            link_element = driver.find_element(By.XPATH, xpath)
            link_text = link_element.get_attribute('href')

            data.loc[i - 1] = [title_text, content_text, link_text]  # 인덱스에 따라 저장

        except Exception as e:
            print(f"Error extracting title: {e}")
            #break  # 오류 발생 시 루프 종료

    # WebDriver 종료
    driver.quit()

    return data  # DataFrame 반환

