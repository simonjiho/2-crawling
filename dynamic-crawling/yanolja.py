from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
import re
import time

# Selenium 드라이버 설정 (Chrome 사용)
#driver = 

# Yanolja 리뷰 페이지로 이동
url = 'https://www.yanolja.com/reviews/domestic/3015391'
######## your code here ########
# driver

# 페이지 로딩을 위해 대기
time.sleep(3)

# 스크롤 설정: 페이지 하단까지 스크롤을 내리기
scroll_count = 10  # 스크롤 횟수 설정
for _ in range(scroll_count):
    ######## your code here ########
    time.sleep(1)  # 스크롤 이후 대기

# 웹페이지 소스 가져오기
page_source = driver.page_source
# BeautifulSoup를 사용하여 HTML 파싱
soup = BeautifulSoup(page_source, 'html.parser')

# 리뷰 텍스트 추출
################################
# reviews_class = 
################################
reviews = []

# 각 리뷰 텍스트 정리 후 추가
for review, reviewer in zip(reviews_class, reviewers_class) :
    cleaned_text = review.get_text(strip=True).replace('\r', '').replace('\n', '')
    reviews.append(f"{reviewer} : {cleaned_text}")


# 별점 추출
ratings = []
################################
# rating_containers = 
################################

# 각 리뷰별로 별점 계산
for container in rating_containers:
    ################################
    ######## your code here ########
    ################################
    
    ratings.append(rating)

# 별점과 리뷰를 결합하여 리스트 생성
data = list(zip(ratings, reviews))

# DataFrame으로 변환
df_reviews = pd.DataFrame(data, columns=['Rating', 'Review'])

# 평균 별점 계산
# average_rating = 


# 불용어 리스트 (한국어)
korean_stopwords = set(['이', '그', '저', '것', '들', '다', '을', '를', '에', '의', '가', '이', '는', '해', '한', '하', '하고', '에서', '에게', '과', '와', '너무', '잘', '또','좀', '호텔', '아주', '진짜', '정말'])

# 모든 리뷰를 하나의 문자열로 결합
# all_reviews_text = 

# 단어 추출 (특수문자 제거)
# words = 

# 불용어 제거
# filtered_words = 

# 단어 빈도 계산
word_counts = Counter(filtered_words)

# 자주 등장하는 상위 15개 단어 추출
common_words = word_counts.most_common(15)

# 분석 결과 요약
summary_df = pd.DataFrame({
    'Average Rating': [average_rating],
    'Common Words': [', '.join([f"{word}({count})" for word, count in common_words])]
})

# 최종 DataFrame 결합
final_df = pd.concat([df_reviews, summary_df], ignore_index=True)

# Excel 파일로 저장
######## your code here ######### 드라이버 종료
# 드라이버 종료
driver.quit()