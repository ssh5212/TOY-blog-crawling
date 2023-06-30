import requests
from bs4 import BeautifulSoup as bs
from datetime import date, timedelta

page = requests.get("https://angelplayer.tistory.com/")
soup = bs(page.text, "html.parser")

# print(soup)

today = date.today()
yesterday = date.today() - timedelta(1)



today_month = int(today.strftime('%m')) # 오늘 달 정보
today_day = int(today.strftime('%d')) # 오늘 일 정보

# today_month = 6 # 오늘 달 정보
# today_day = 27 # 오늘 일 정보

# print(today_month)
# print(today_day)


yesterday_month = int(yesterday.strftime('%m')) # 어제 달 정보
yesterday_day = int(yesterday.strftime('%d')) # 어제 일 정보

count = 0 # 어제 오늘 쓴 포스트의 개수

time_elements = soup.select('span.txt_bar')
# print(time_elements)
for index, element in enumerate(time_elements, 1):
	text = element.text
	
	# 월 구하기
	lastidx = text.find('.')
	text = text[lastidx + 1:]
	month = int(text[1:lastidx - 2])
	print("month :", month)

	# 일 구하기
	lastidx=text.find('.')
	day = int(text[lastidx + 2:-7])
	print("day :", day)

	if ((month == yesterday_month and day == yesterday_day) or (month == today_month and day == today_day)):
		count += 1
		continue
	else:
		break


if (count != 0):
	title_elements = soup.select('h3.tit_post')
	h_elements = soup.find_all("div", class_="index-list-content")

	# print(title_elements)

	for index, element in enumerate(title_elements, 1):
		# <h3 class="tit_post">[SSAFY] Start Camp에서 SSAFY MeetUp까지! 1학기 총정리!</h3>
		# print(element)

		text = element.text
		print(text)

		link_data = h_elements[index - 1].select_one("div.index-list-content a")
		if link_data:
			href = "angelplayer.tistory.com" + link_data["href"]
			print(href)



		if (count == index):
			break

else:
	print("내 그랄줄 알았다!")







# h_elements = soup.find_all("div", class_="index-list-content")
# data = h_elements[1].select_one("div.index-list-content a")
# if data:
# 	href = data["href"]
# 	print(href)

# for index, element in enumerate(h_elements, 1):
# 	data = element.select_one("div.index-list-content a")
# 	if data:
# 		href = data["href"]
# 		print(href)

# print(title_elements)


# 	text = element.text
# 	print(text)
