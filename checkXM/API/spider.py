import requests
import random
import time
from requests.exceptions import RequestException
import datetime

from API.comment import DouyinComment
from API.excel import MovieDataExcel


class DouyinSpider:
    ############################
    # 0,1710302400000,1709528400000,1709287218000,1709020801000,1708772400000,1708606801000,1708425831000,1708246800000,1708142400000,1707994086000,1707893947000
    # 1707753672000,1707627601000,1707453024000,1707201010000,1706930958000,1706666340000,1706355000000,1705888800000,1705374011000
    def __init__(self, sec_user_id, uifid, count=18):
        self.sec_user_id = sec_user_id
        self.uifid = uifid
        #self.cursors = [0]
        self.cursors = [0, 1710302400000, 1709528400000, 1709287218000, 1709020801000, 1708772400000, 1708606801000,
                        1708425831000, 1708246800000, 1708142400000, 1707994086000, 1707893947000, 1707753672000,
                        1707627601000, 1707453024000, 1707201010000, 1706930958000, 1706666340000, 1706355000000,
                        1705888800000, 1705374011000]
        self.count = count
        self.base_url = "https://www.douyin.com/aweme/v1/web/aweme/post/"
        self.headers = {
            'Host': 'www.douyin.com',
            'Cookie': 'ttwid=1%7CKV1fFHifopYoxvnFYTfuyh5X9raTklwVKg7ay9aAPWw%7C1730287805%7Cbc2d8c1dff2f5a632e283c5f432fd068d11938e31faac5318a39dac826614286; UIFID_TEMP=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d1122189c816f1a8afdbfcce3019e48ff107f25ae055b17205681c4d0697592cb98c572da47acbe0c611d165e163b613ecba; s_v_web_id=verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5; hevc_supported=true; dy_swidth=1536; dy_sheight=864; FORCE_LOGIN=%7B%22isForcePopClose%22%3A1%2C%22videoConsumedRemainSeconds%22%3A180%7D; fpk1=U2FsdGVkX1+3JK51xSSDpeK5s7asYeyZF7reCA+oraUSydh9wUsFEDqXCjwvuGxcMp0QOALwnxis89brHpI7ng==; fpk2=7675d59b5e84e0a878ee6f0a97f9056f; passport_csrf_token=9f15399129b85c0ed48e8e879c87526a; passport_csrf_token_default=9f15399129b85c0ed48e8e879c87526a; bd_ticket_guard_client_web_domain=2; UIFID=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112f485a28250abe3b6e3642aab0bec10ed25942c76caace5b473fcdf18abcf88f2b8bd2e00c967cdb6661eff0f30914db0b12f6a146d2adf5ca8e350e09ce8f6f3643f9523557b3cc69de0624275814dc58f41defc7663327a12249556594a014c18f4341345bd4066ae48b129f8622ac12d2323f19d1da993e482f0e5c103f8cd; passport_assist_user=CjzabjIXKUpirMADwElVFw4QooKom0NFPp5KczMdZC34Gq4vf95vsFGYMhy5Kh7o7SFcUc5OOJRcbXbiSqcaSgo8fcGQF6f1P0_eaS5_1SuYJk0aeyUebqGfFtJnii5NHaCZjHyIapnvo796HlLimPWBLIhJ9-PJrpH1Uw6KEKyQ4A0Yia_WVCABIgED1EIebA%3D%3D; n_mh=k0ZDMEx4Mj4G_Ef1j7IuX3CdzihZ3eDtIXPi4A5GPNk; sso_uid_tt=c50396f34c6b30c8f3fe4503bf05c0c4; sso_uid_tt_ss=c50396f34c6b30c8f3fe4503bf05c0c4; toutiao_sso_user=ef55db02b32e8e69cd98795df95f93c3; toutiao_sso_user_ss=ef55db02b32e8e69cd98795df95f93c3; sid_ucp_sso_v1=1.0.0-KGVjODg5OWZmZTE5ZjQ1ZjUxYzVlYzFiODhiMTAzMmFlMWFlNTBlMDIKHwignryw5wIQ4bGIuQYY7zEgDDDFj4nWBTgGQPQHSAYaAmxmIiBlZjU1ZGIwMmIzMmU4ZTY5Y2Q5ODc5NWRmOTVmOTNjMw; ssid_ucp_sso_v1=1.0.0-KGVjODg5OWZmZTE5ZjQ1ZjUxYzVlYzFiODhiMTAzMmFlMWFlNTBlMDIKHwignryw5wIQ4bGIuQYY7zEgDDDFj4nWBTgGQPQHSAYaAmxmIiBlZjU1ZGIwMmIzMmU4ZTY5Y2Q5ODc5NWRmOTVmOTNjMw; login_time=1730287844724; passport_auth_status=7c54df04feebcd9646de4a41e6365d7f%2C; passport_auth_status_ss=7c54df04feebcd9646de4a41e6365d7f%2C; uid_tt=54993fb8d64563b1f0d12322aea4c5be; uid_tt_ss=54993fb8d64563b1f0d12322aea4c5be; sid_tt=cf0cb56cc1a5a13e1776ea078be48aab; sessionid=cf0cb56cc1a5a13e1776ea078be48aab; sessionid_ss=cf0cb56cc1a5a13e1776ea078be48aab; is_staff_user=false; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=0f526cbe559bb7eb2631f177fdc0ec95; __security_server_data_status=1; sid_guard=cf0cb56cc1a5a13e1776ea078be48aab%7C1730287855%7C5183989%7CSun%2C+29-Dec-2024+11%3A30%3A44+GMT; sid_ucp_v1=1.0.0-KDA0MjhjMDRiMDU4ZGExOWUwMGQzOTA0NTM0MTAzZjMyZjAxYjhmMDMKGQignryw5wIQ77GIuQYY7zEgDDgGQPQHSAQaAmxmIiBjZjBjYjU2Y2MxYTVhMTNlMTc3NmVhMDc4YmU0OGFhYg; ssid_ucp_v1=1.0.0-KDA0MjhjMDRiMDU4ZGExOWUwMGQzOTA0NTM0MTAzZjMyZjAxYjhmMDMKGQignryw5wIQ77GIuQYY7zEgDDgGQPQHSAQaAmxmIiBjZjBjYjU2Y2MxYTVhMTNlMTc3NmVhMDc4YmU0OGFhYg; publish_badge_show_info=%220%2C0%2C0%2C1730287857737%22; h265ErrorNum=-1; store-region=cn-hb; store-region-src=uid; xgplayer_user_id=257565671676; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.743%7D; SEARCH_RESULT_LIST_TYPE=%22single%22; pwa2=%220%7C0%7C3%7C0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; WallpaperGuide=%7B%22showTime%22%3A1730287874046%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A53%2C%22cursor2%22%3A16%2C%22hoverTime%22%3A1730301787305%7D; strategyABtestKey=%221730513612.769%22; csrf_session_id=a30f1cb500e93642d0c6109b37a87f08; biz_trace_id=c0fdceb0; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA3DgglHnUfteMFNj7ZPn5ZzQ5wu_fNMuNBBC1ThLcoHQ%2F1730563200000%2F0%2F0%2F1730517237194%22; __ac_nonce=06725a9db00fc80a5b4a7; __ac_signature=_02B4Z6wo00f01IqdEywAAIDAvbnXct2je8SKvReAAEWHQsggRKoPn6gIBxpAGQx5CcWrUExz2qGeJJzBPlXWQ8Olbk95T3CNHkvxs6gjkpu2CAdTyQMIzLPdKhCYA6XJvk0bSPqAQO4UfTM502; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA3DgglHnUfteMFNj7ZPn5ZzQ5wu_fNMuNBBC1ThLcoHQ%2F1730563200000%2F0%2F1730521566851%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT1pUNWJnMFVXb014cm91Y01mOGRRZEJGM3ZzZStoT3lrTlNZUDdGWU1HYlp3MDRLZEthOWY4NTMrNG14dUt1eGIyN0FQK3BkdDFJR3g5ZDVkQ2VHekE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; odin_tt=865ceb6ba7f9e7a95ca7bedf115a1a02a2a5214bcf5c55ad11b10c8a029aa06072ba3086b81602dd3a5f43e1bfc904b2; download_guide=%223%2F20241031%2F1%22; passport_fe_beating_status=false; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22',
            'uifid': self.uifid,
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.douyin.com/user/MS4wLjABAAAAwHgIE1Q9ZfFmEN0DCBIAQmZFsTp767B3fVPw0tso6wGwllz-Tz2ASCyHa1kgZBy3',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'priority': 'u=1, i',
            'pragma': 'no-cache',
            'cache-control': 'no-cache'
        }
        self.proxies = {
            "http": None,
            "https": None
        }
        self.params = {
            "device_platform": "webapp",
            "aid": 6383,
            "channel": "channel_pc_web",
            "sec_user_id": self.sec_user_id,
            "max_cursor": None,
            "locate_query": "false",
            "show_live_replay_strategy": 1,
            "need_time_list": 1,
            "time_list_query": 0,
            "whale_cut_token": "",
            "cut_version": 1,
            "count": self.count,
            "publish_video_strategy_type": 2,
            "from_user_page": 1,
            "update_version_code": 170400,
            "pc_client_type": 1,
            "pc_libra_divert": "Windows",
            "version_code": 290100,
            "version_name": "29.1.0",
            "cookie_enabled": "true",
            "screen_width": 1536,
            "screen_height": 864,
            "browser_language": "zh-CN",
            "browser_platform": "Win32",
            "browser_name": "Chrome",
            "browser_version": "130.0.0.0",
            "browser_online": "true",
            "engine_name": "Blink",
            "engine_version": "130.0.0.0",
            "os_name": "Windows",
            "os_version": "10",
            "cpu_core_num": 16,
            "device_memory": 8,
            "platform": "PC",
            "downlink": 10,
            "effective_type": "4g",
            "round_trip_time": 100,
            "webid": 7431529453598393882,
            "uifid": self.uifid,
            "verifyFp": "verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5",
            "fp": "verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5",
            "msToken": "TaWGsAgrAmBH97MTKcJ_OZB9mBmD69esoOjlmYyi0kGFNyB5a2MmfA77cpv1uRBgnrmqDWP8NswfBNvTFmtmoK9now7eDHot4FwOD3LaoXG6vHtIDBb59Fu3CKvB0tHuQcGI-JmBfZpONixUOnBqMCtZYoiVYGAddzoAsa7piZw==",
            "a_bogus": "Qv4Rgt6LQo8jCd/t8Kjny35UT8LArs8yJ-ioRx3PHNKdYweaDbPPdNGDnozK4DmlLRpkhq1Hdnt/YEVcFtXwZ99kLmkfuki6x029960o8qq6TUG/grmdC8uFLwsKUQvNl5CaiID5IsMnIVnRnqVqAQMaC5z9QRDgSNpVp2t9aDS83BLTnn2RenTAW1E="
        }
        self.comment = DouyinComment(sec_user_id, uifid)
        self.movie_excel = MovieDataExcel()

    def get_random_user_agent(self):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        ]
        return random.choice(user_agents)

    def connect_to_endpoint(self, params, payload):

        response = requests.get(self.base_url, params=params, data=payload, headers=self.headers, proxies=self.proxies)
        if response.status_code != 200:
            raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
        return response.json()

    def fetch_posts(self):
        payload = {}
        for cursor in self.cursors:
            params = self.params.copy()  # 复制模板
            params["max_cursor"] = cursor  # 设置 max_cursor
            result = self.connect_to_endpoint(params=params, payload=payload)
            self.analysis(result)
            # 随机等待
            time.sleep(random.uniform(1, 3))  # 等待1到3秒

    def analysis(self, data):

        if data:
            # 提取信息
            status_code = data['status_code']
            min_cursor = data['min_cursor']
            max_cursor = data['max_cursor']
            has_more = data['has_more']
            aweme_list = data['aweme_list']

            # 打印提取的信息
            print(f"Status Code: {status_code}")
            print(f"Min Cursor: {min_cursor}")
            print(f"Max Cursor: {max_cursor}")
            print(f"Has More: {has_more}")

            # 遍历并打印 aweme_list 中的每个元素
            index = 0
            for aweme in aweme_list:
                index += 1
                aweme_id = aweme['aweme_id']
                desc = aweme['desc']
                create_time = aweme['create_time']
                local_time = datetime.datetime.fromtimestamp(create_time)
                log_format = "%Y-%m-%d %H:%M:%S"
                create_date = local_time.strftime(log_format)

                # 获取 video
                video = aweme.get("video", {})
                duration = video.get("duration")
                total_seconds = round(duration / 1000)
                minutes = total_seconds // 60
                seconds = total_seconds % 60
                video_duration = f"{minutes:02}:{seconds:02}"
                # 检查 url_list 是否为空
                video_url = None
                url_list = video.get("play_addr", {}).get("url_list", [])
                if url_list:
                    video_url = url_list[0]  # 将第一个 URL 赋值给 video_url
                else:
                    print("url_list 为空，无法获取第一个元素。")

                # 获取 statistics
                statistics = aweme.get("statistics", {})
                collect_count = statistics.get("collect_count")
                comment_count = statistics.get("comment_count")
                digg_count = statistics.get("digg_count")
                share_count = statistics.get("share_count")

                # 获取评论
                comment_list = self.comment.fetch_posts(aweme_id)


                print(f"\nAweme ID: {aweme_id}")
                print(f"Description: {desc}")
                print(f"Create Time: {create_date}")
                print(f"视频时长:{video_duration}")
                print(f"视频链接:{video_url}")
                print(f"点赞数: {digg_count}")
                print(f"评论数: {comment_count}")
                print(f"收藏数: {collect_count}")
                print(f"转发数: {share_count}")
                if comment_list:
                    comments = comment_list.get('comments', [])
                    if comments:
                        # 对 comments 进行排序，取点赞数最高的前 3 条
                        top_comments = sorted(comments, key=lambda x: x['digg_count'], reverse=True)[:3]
                        for comment in top_comments:
                            user = comment['user']
                            print(f"用户: {user['nickname']}, 评论: {comment['text']}, 点赞数: {comment['digg_count']}")

                    self.movie_excel.insert_data(desc, create_date, video_duration, video_url, digg_count,comment_count, collect_count, share_count, top_comments)
                else:
                    print("评论数据为空")
                time.sleep(1)  # 每次请求之间等待1秒

            print(f"Total: {index}")
        else:
            print("数据为空")


if __name__ == "__main__":
    sec_user_id = "MS4wLjABAAAAwHgIE1Q9ZfFmEN0DCBIAQmZFsTp767B3fVPw0tso6wGwllz-Tz2ASCyHa1kgZBy3"  # 替换为您的sec_user_id
    uifid = "63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112f485a28250abe3b6e3642aab0bec10ed25942c76caace5b473fcdf18abcf88f2b8bd2e00c967cdb6661eff0f30914db0b12f6a146d2adf5ca8e350e09ce8f6f3643f9523557b3cc69de0624275814dc58f41defc7663327a12249556594a014c18f4341345bd4066ae48b129f8622ac12d2323f19d1da993e482f0e5c103f8cd"
    spider = DouyinSpider(sec_user_id, uifid)
    spider.fetch_posts()
