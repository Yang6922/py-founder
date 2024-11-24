import urllib

import requests
import random
from requests.exceptions import RequestException


class DouyinSearch:
    def __init__(self,from_user,keyword):
        self.base_url = "https://www.douyin.com/aweme/v1/web/home/search/item/"
        self.from_user = from_user
        self.keyword = keyword
        self.headers = {
            'Host': 'www.douyin.com',
            'Cookie': 'ttwid=1%7CKV1fFHifopYoxvnFYTfuyh5X9raTklwVKg7ay9aAPWw%7C1730287805%7Cbc2d8c1dff2f5a632e283c5f432fd068d11938e31faac5318a39dac826614286; UIFID_TEMP=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d1122189c816f1a8afdbfcce3019e48ff107f25ae055b17205681c4d0697592cb98c572da47acbe0c611d165e163b613ecba; s_v_web_id=verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5; hevc_supported=true; dy_swidth=1536; dy_sheight=864; FORCE_LOGIN=%7B%22isForcePopClose%22%3A1%2C%22videoConsumedRemainSeconds%22%3A180%7D; fpk1=U2FsdGVkX1+3JK51xSSDpeK5s7asYeyZF7reCA+oraUSydh9wUsFEDqXCjwvuGxcMp0QOALwnxis89brHpI7ng==; fpk2=7675d59b5e84e0a878ee6f0a97f9056f; passport_csrf_token=9f15399129b85c0ed48e8e879c87526a; passport_csrf_token_default=9f15399129b85c0ed48e8e879c87526a; bd_ticket_guard_client_web_domain=2; UIFID=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112f485a28250abe3b6e3642aab0bec10ed25942c76caace5b473fcdf18abcf88f2b8bd2e00c967cdb6661eff0f30914db0b12f6a146d2adf5ca8e350e09ce8f6f3643f9523557b3cc69de0624275814dc58f41defc7663327a12249556594a014c18f4341345bd4066ae48b129f8622ac12d2323f19d1da993e482f0e5c103f8cd; passport_assist_user=CjzabjIXKUpirMADwElVFw4QooKom0NFPp5KczMdZC34Gq4vf95vsFGYMhy5Kh7o7SFcUc5OOJRcbXbiSqcaSgo8fcGQF6f1P0_eaS5_1SuYJk0aeyUebqGfFtJnii5NHaCZjHyIapnvo796HlLimPWBLIhJ9-PJrpH1Uw6KEKyQ4A0Yia_WVCABIgED1EIebA%3D%3D; n_mh=k0ZDMEx4Mj4G_Ef1j7IuX3CdzihZ3eDtIXPi4A5GPNk; sso_uid_tt=c50396f34c6b30c8f3fe4503bf05c0c4; sso_uid_tt_ss=c50396f34c6b30c8f3fe4503bf05c0c4; toutiao_sso_user=ef55db02b32e8e69cd98795df95f93c3; toutiao_sso_user_ss=ef55db02b32e8e69cd98795df95f93c3; sid_ucp_sso_v1=1.0.0-KGVjODg5OWZmZTE5ZjQ1ZjUxYzVlYzFiODhiMTAzMmFlMWFlNTBlMDIKHwignryw5wIQ4bGIuQYY7zEgDDDFj4nWBTgGQPQHSAYaAmxmIiBlZjU1ZGIwMmIzMmU4ZTY5Y2Q5ODc5NWRmOTVmOTNjMw; ssid_ucp_sso_v1=1.0.0-KGVjODg5OWZmZTE5ZjQ1ZjUxYzVlYzFiODhiMTAzMmFlMWFlNTBlMDIKHwignryw5wIQ4bGIuQYY7zEgDDDFj4nWBTgGQPQHSAYaAmxmIiBlZjU1ZGIwMmIzMmU4ZTY5Y2Q5ODc5NWRmOTVmOTNjMw; login_time=1730287844724; passport_auth_status=7c54df04feebcd9646de4a41e6365d7f%2C; passport_auth_status_ss=7c54df04feebcd9646de4a41e6365d7f%2C; uid_tt=54993fb8d64563b1f0d12322aea4c5be; uid_tt_ss=54993fb8d64563b1f0d12322aea4c5be; sid_tt=cf0cb56cc1a5a13e1776ea078be48aab; sessionid=cf0cb56cc1a5a13e1776ea078be48aab; sessionid_ss=cf0cb56cc1a5a13e1776ea078be48aab; is_staff_user=false; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=0f526cbe559bb7eb2631f177fdc0ec95; __security_server_data_status=1; sid_guard=cf0cb56cc1a5a13e1776ea078be48aab%7C1730287855%7C5183989%7CSun%2C+29-Dec-2024+11%3A30%3A44+GMT; sid_ucp_v1=1.0.0-KDA0MjhjMDRiMDU4ZGExOWUwMGQzOTA0NTM0MTAzZjMyZjAxYjhmMDMKGQignryw5wIQ77GIuQYY7zEgDDgGQPQHSAQaAmxmIiBjZjBjYjU2Y2MxYTVhMTNlMTc3NmVhMDc4YmU0OGFhYg; ssid_ucp_v1=1.0.0-KDA0MjhjMDRiMDU4ZGExOWUwMGQzOTA0NTM0MTAzZjMyZjAxYjhmMDMKGQignryw5wIQ77GIuQYY7zEgDDgGQPQHSAQaAmxmIiBjZjBjYjU2Y2MxYTVhMTNlMTc3NmVhMDc4YmU0OGFhYg; publish_badge_show_info=%220%2C0%2C0%2C1730287857737%22; h265ErrorNum=-1; store-region=cn-hb; store-region-src=uid; xgplayer_user_id=257565671676; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.743%7D; download_guide=%223%2F20241031%2F0%22; SEARCH_RESULT_LIST_TYPE=%22single%22; pwa2=%220%7C0%7C3%7C0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; WallpaperGuide=%7B%22showTime%22%3A1730287874046%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A53%2C%22cursor2%22%3A16%2C%22hoverTime%22%3A1730301787305%7D; strategyABtestKey=%221730513612.769%22; csrf_session_id=a30f1cb500e93642d0c6109b37a87f08; biz_trace_id=c0fdceb0; __ac_nonce=0672592ef00572131475; __ac_signature=_02B4Z6wo00f01e8PcmQAAIDB2Cu2OLaT36XvL3bAABzo6vX6iIYJGzotcSoPVyUnGShmGBslx6eZsrLe3EH48na1-XQW.wfK3ru69NItSpTGkDHrdEm5GH1TYAUepfaICkWDfyg7y1NFWco9b3; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA3DgglHnUfteMFNj7ZPn5ZzQ5wu_fNMuNBBC1ThLcoHQ%2F1730563200000%2F0%2F0%2F1730516637194%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA3DgglHnUfteMFNj7ZPn5ZzQ5wu_fNMuNBBC1ThLcoHQ%2F1730563200000%2F0%2F0%2F1730517237194%22; passport_fe_beating_status=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT1pUNWJnMFVXb014cm91Y01mOGRRZEJGM3ZzZStoT3lrTlNZUDdGWU1HYlp3MDRLZEthOWY4NTMrNG14dUt1eGIyN0FQK3BkdDFJR3g5ZDVkQ2VHekE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; odin_tt=71618db9862d9a52319554d79d8bd044b830f9b0c390dafb8b30fa69313b7d95677d5624c1aeaed3dd0c13cd585db00f; IsDouyinActive=true',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': self.get_random_user_agent(),
            'accept': '*/*',
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
            "aid": "6383",
            "channel": "channel_pc_web",
            "search_channel": "aweme_personal_home_video",
            "search_source": "normal_search",
            "search_scene": "douyin_search",
            "sort_type": "0",
            "publish_time": "0",
            "is_filter_search": "0",
            "query_correct_type": "1",
            "keyword": self.keyword,
            "enable_history": "1",
            "search_id": "",
            "offset": "0",
            "count": "10",
            "from_user": self.from_user,
            "pc_client_type": "1",
            "pc_libra_divert": "Windows",
            "version_code": "170400",
            "version_name": "17.4.0",
            "cookie_enabled": "true",
            "screen_width": "1536",
            "screen_height": "864",
            "browser_language": "zh-CN",
            "browser_platform": "Win32",
            "browser_name": "Chrome",
            "browser_version": "130.0.0.0",
            "browser_online": "true",
            "engine_name": "Blink",
            "engine_version": "130.0.0.0",
            "os_name": "Windows",
            "os_version": "10",
            "cpu_core_num": "16",
            "device_memory": "8",
            "platform": "PC",
            "downlink": "10",
            "effective_type": "4g",
            "round_trip_time": "100",
            "webid": "7431529453598393882",
            "msToken": "wzdpjqkHoGFnxCPTLs0_bTvjsv1c1n3MTryM0a2BetyC1-uBJ-bznGggGj0s1XGyw-kSKQ2K1lMl6ZmjrmAqEX60_nS60n6hsHosBrdwju99M7q01S_O5jb6C8g99NWDcIU3lHLbEjIyRnUbdlSaaNRecSOtZUzpVlXhEIfHqg==",
            "a_bogus": "Yfs5kwXjE2/nadFb8KDj73NUSSVMrTWyzMTQRjxTCNK6YwUapRNFdaajaxqH6erzDRpkhCZ7RfzMTxVcFTUwZeapzmkkugX6o02c9gXL8qNgTUT/EHDOC0TzFwse0YJNeQCliAh5lsMrInnRVNVpAQ/GS5F9QRfgWqpAp/GyjDS03TgTVnAJtag1",
            "verifyFp": "verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5",
            "fp": "verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5"
        }

    def get_random_user_agent(self):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        ]
        return random.choice(user_agents)

    def fetch_posts(self):
        payload = {}
        try:
            response = requests.get(self.base_url, params=self.params, data=payload, headers=self.headers,proxies=self.proxies)
            # 打印最终的URL
            # print(response.url)
            response.raise_for_status()  # 检查请求是否成功
            return response.json()
        except RequestException as e:
            print(f"请求错误: {e}")
            return None

    def analysis(self):
        data = self.fetch_posts()
        if data:
            # 提取信息
            extra = data['extra']
            global_doodle_config = data['global_doodle_config']
            has_more = data['has_more']
            status_code = data['status_code']
            aweme_list = data['aweme_list']

            # 打印提取的信息
            print(f"Extra: {extra}")
            print(f"Global Doodle Config: {global_doodle_config}")
            print(f"Has More: {has_more}")
            print(f"Status Code: {status_code}")

            # 遍历并打印 aweme_list 中的每个元素
            index = 0
            for aweme in aweme_list:
                index += 1
                item = aweme.get("item", {})
                aweme_id = item.get("aweme_id")  # 获取 aweme_id
                item_caption = item.get("caption")  # 获取 caption

                # 获取 statistics
                statistics = item.get("statistics", {})
                admire_count = statistics.get("admire_count")
                collect_count = statistics.get("collect_count")
                comment_count = statistics.get("comment_count")
                digg_count = statistics.get("digg_count")
                download_count = statistics.get("download_count")
                play_count = statistics.get("play_count")
                share_count = statistics.get("share_count")

                type = aweme['type']
                print(f"\n item: {item}")
                print(f"aweme_id: {aweme_id}")
                print(f"caption: {item_caption}")
                print(f"点赞数: {digg_count}")
                print(f"评论数: {comment_count}")
                print(f"收藏数: {collect_count}")
                print(f"分享数: {share_count}")
                print(f"type: {type}")
            print(f"Total: {index}")
        else:
            print("数据为空")

if __name__ == "__main__":
    from_user = "4215980653034563"
    keyword = "大家各练各的，真是谁都没耽误"
    search = DouyinSearch(from_user,keyword)
    search.analysis()
