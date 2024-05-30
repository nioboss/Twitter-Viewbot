# Nhận Code Tool Theo Yêu Cầu - Zalo: 0896502726 - Tele: @nio2k9

# script programmed and published by: @HaAnhTuan
# increase Twitter post views with unlimited cookies
# - used only for learning, not recommended to increase large numbers, account may be locked by twitter because of its policy
# - I have not tested to see if it still works because I coded this script last year
from datetime           import datetime
from pystyle            import *    
from urllib3.exceptions import InsecureRequestWarning
from http               import cookiejar
import asyncio
import httpx
import os
import time
import threading
import requests
import random
class chancookie(cookiejar.CookiePolicy):
    # Nhận Code Tool Theo Yêu Cầu - Zalo: 0896502726 - Tele: @nio2k9
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape  = True
    rfc2965   = hide_cookie2 = False
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
r = requests.Session()
r .cookies.set_policy(chancookie())
def rpsm_loop():
    # Nhận Code Tool Theo Yêu Cầu - Zalo: 0896502726 - Tele: @nio2k9
    global ycs, rps, rpm
    while True:
        bandau = ycs
        time.sleep(1.5)
        rps = round((ycs - bandau) / 1.5, 1)
        rpm = round(rps * 60, 1)
def title_loop():
    # Nhận Code Tool Theo Yêu Cầu - Zalo: 0896502726 - Tele: @nio2k9
    global rps, rpm, thanhcongs, thatbais, ycs
    while True:
        os.system(f'title Twitter Viewbot by @__nioAI ^I Success: {thanhcongs} I Fails: {thatbais} I Rpm: {rpm}' if os.name == 'nt' else '')
        now = datetime.now().strftime("%H:%M:%S")
        print(Colorate.Horizontal(Colors.blue_to_white, f"[{now}] {thanhcongs} {thatbais}"))
        time.sleep(2)
def send_request(session):
    # Nhận Code Tool Theo Yêu Cầu - Zalo: 0896502726 - Tele: @nio2k9
    while True:
        cookie = random.choice(cookies)
        global ycs, _lock, thanhcongs, thatbais
        csrfToken = cookie.split('ct0=')[1].split(';')[0]
        author_id = cookie.split('twid=u%3D')[1].split(';')[0]
        tweet_uid = tweet_url.split('/')[-1]
        chay      = session.post('https://twitter.com/i/api/1.1/jot/client_event.json', headers={'authority': 'twitter.com', 'accept': '*/*', 'accept-language': 'vi,en-GB;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://twitter.com', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'x-csrf-token': csrfToken, 'x-twitter-active-user': 'yes', 'x-twitter-auth-type': 'OAuth2Session', 'x-twitter-client-language': 'vi', 'referer': tweet_url, 'cookie': cookie}, data={'debug': 'true', 'log': '[{"_category_":"client_event","format_version":2,"triggered_on":1699964598313,"items":[{"item_type":0,"id":"'+tweet_uid+'","position":0,"sort_index":"7500454969542471449","suggestion_details":{"controller_data":"DAACDAABDAABCgABAAAAAAAAAAAKAAkVwK3azZpAAAAAAAA=","suggestion_type":"RankedOrganicTweet"},"percent_screen_height_100k":46267,"author_id":"'+author_id+'","is_viewer_follows_tweet_author":false,"is_tweet_author_follows_viewer":false,"is_viewer_super_following_tweet_author":false,"is_viewer_super_followed_by_tweet_author":false,"is_tweet_author_super_followable":false,"engagement_metrics":{"reply_count":0,"retweet_count":0,"favorite_count":1,"quote_count":0}}],"event_namespace":{"page":"tweet","component":"stream","action":"results","client":"m5"},"client_event_sequence_start_timestamp":1699964595212,"client_event_sequence_number":6,"client_app_id":"3033300"}]'})
        ycs += 1
        if (chay == ''):
            _lock.acquire()
            _lock.release()
            thanhcongs += 1
        else:
            if cookies == []:
                input('Danh sách cookie chạy được view đã hết, hãy thêm mới cookie và khởi động lại tool')
                exit()
            if (_lock.locked()):
                _lock.release()
            thatbais += 1
            cookies  .remove(cookie)
def view_loop(cookies, min): # this is instead of opening cmd and running =))
    # Nhận Code Tool Theo Yêu Cầu - Zalo: 0896502726 - Tele: @nio2k9
    dsluong = []
    for _ in range(min):
        thread = threading.Thread(target=run_thread, args=(cookies,))
        dsluong.append(thread)
        thread.start()
    for thread in dsluong:
        thread.join()
def run_thread(cookies):
    # Nhận Code Tool Theo Yêu Cầu - Zalo: 0896502726 - Tele: @nio2k9
    with httpx.Client(http2 = True) as session:
        list_task = [send_request(session) for i in range(500000)]
        asyncio.run(asyncio.gather(*list_task))
async def main():
    # Nhận Code Tool Theo Yêu Cầu - Zalo: 0896502726 - Tele: @nio2k9
    global tweet_url, ycs, _lock, thanhcongs, thatbais, rpm, rps, cookies
    os.system("cls" if (os.name == "nt") else "clear"); os.system("title Twitter Viewbot by @nio2k9" if (os.name == "nt") else "")
    tweet_url = str(Write.Input("? - post link >  ", Colors.red_to_purple, interval=0))
    os.system("cls" if (os.name == "nt") else "clear")
    _lock      = threading.Lock()
    ycs        = 0
    thanhcongs = 0
    thatbais   = 0
    rpm        = 0
    rps        = 0
    threading.Thread(target=rpsm_loop).start()
    threading.Thread(target=title_loop).start()
    with open('cookies.txt', 'r') as f:
        cookies = f.read().strip().splitlines()
    min = 100000
    view_loop(cookies, 100000)

# RUN TOOLS
if (__name__ == "__main__"):
    # Nhận Code Tool Theo Yêu Cầu - Zalo: 0896502726 - Tele: @nio2k9
    asyncio.run(main())
    # mình còn 1 source chạy max speed tốc độ x50 lần phiên bản này ngôn ngữ khác ae cần thì ib mình nhé
