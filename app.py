from flask import Flask, render_template
app = Flask(__name__)
from flask import redirect
import requests
from bs4 import BeautifulSoup as bs
from datetime import date, timedelta

result_data = {}
bs_result = True


@app.route('/redirect_url/<dynamic_value>')
def redirect_url(dynamic_value):
    print("redirect")
    redirect_url = f'https://angelplayer.tistory.com/{dynamic_value}'
    return redirect(redirect_url)

def bs4():
    print("IM bs INNNNNOR")
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
                href = link_data["href"]
                print(href)

                result_data[index] = {'title' : text, "url": href}


            if (count == index):
                break

    else:
        print("쓴 글이 없다")
        global bs_result
        bs_result = False

@app.route('/')
def home():
    print("start")

    bs4()

    global bs_result
    if (bs_result == False):
        return render_template("fail.html")
    else:
        return render_template("index.html", 
                result_data = result_data)

if __name__ == '__main__':
    app.run(debug=True)