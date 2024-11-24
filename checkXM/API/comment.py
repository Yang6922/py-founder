import requests
import random
import time
from requests.exceptions import RequestException


class DouyinComment:
    def __init__(self, sec_user_id, uifid , cursor=0, count = 20, ):
        self.sec_user_id = sec_user_id
        self.uifid = uifid
        # 分页游标，指示请求的评论起始位置（如 0、10、20 等）
        self.cursor = cursor
        # 每次请求的评论数量，这里是 20
        self.count = count
        self.base_url =  "https://www.douyin.com/aweme/v1/web/comment/list/"
        self.headers = {
            'Host': 'www.douyin.com',
            'Cookie': 'ttwid=1%7CKV1fFHifopYoxvnFYTfuyh5X9raTklwVKg7ay9aAPWw%7C1730287805%7Cbc2d8c1dff2f5a632e283c5f432fd068d11938e31faac5318a39dac826614286; ...',
            # 省略部分内容
            'uifid': self.uifid,
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': self.get_random_user_agent(),
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.douyin.com/user/MS4wLjABAAAAwHgIE1Q9ZfFmEN0DCBIAQmZFsTp767B3fVPw0tso6wGwllz-Tz2ASCyHa1kgZBy3?from_tab_name=main&modal_id=7329919390223256842',
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
            'device_platform': 'webapp',
            'aid': 6383,
            'channel': 'channel_pc_web',
            'aweme_id': None,
            'cursor': self.cursor,
            'count': self.count,
            'item_type': 0,
            'insert_ids': '',
            'whale_cut_token': '',
            'cut_version': 1,
            'rcFT': '',
            'update_version_code': 170400,
            'pc_client_type': 1,
            'pc_libra_divert': 'Windows',
            'version_code': 170400,
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': 1536,
            'screen_height': 864,
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Chrome',
            'browser_version': '130.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '130.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'cpu_core_num': 16,
            'device_memory': 8,
            'platform': 'PC',
            'downlink': 10,
            'effective_type': '4g',
            'round_trip_time': 100,
            'webid': '7431529453598393882',
            'uifid': self.uifid,
            'verifyFp': 'verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5',
            'fp': 'verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5',
            'msToken': 'xeOlXlqeqztzuKGUCG8KFk_OBDhB0VS3_1tNHxqcPL4p87WvtMfW48dfoepxVUAwyYi1uHCm9hSHoUQHQS52FUFxoWCAYR7QzttYMT73iEs9-k9T5ZViNlDUz0B5hkVlQM7njV-0zW3q-Mo0y8OlKNhxzA97LZtcQlXehh4F4A%3D%3D',
            'a_bogus': 'OvURktSLDdm5KdKGmCbVyV-U6WdlNP8yUBixRO3P9PFPYw0OESNpdaeIrxFChzR4oWpzhCVHpnt%2FYDncPTUTZHnpKmpvS%2F0Wg42998so8qqXGes%2FDqDdChzzLwBF0QJNlA9aiADRWsMN2fdR9qVFAQBay5zH5RjgSqpnpZb9GDCU3s6Tn924taGWg76%3D'
        }

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

    def fetch_posts(self,aweme_id):
        payload = {}
        params = self.params.copy()  # param
        params["aweme_id"] = aweme_id  # set aweme_id
        result = self.connect_to_endpoint(params=params, payload=payload)
        return result
        # self.analysis(result)

    def analysis(self, data):
        if data:
            top_comments = data['comments'][:3]
            for comment in top_comments:
                user = comment['user']
                print(f"用户: {user['nickname']}, 评论: {comment['text']}, 点赞数: {comment['digg_count']}")
        else:
            print("数据为空")


if __name__ == "__main__":
    sec_user_id = "MS4wLjABAAAAwHgIE1Q9ZfFmEN0DCBIAQmZFsTp767B3fVPw0tso6wGwllz-Tz2ASCyHa1kgZBy3"  # 替换为您的sec_user_id
    uifid = "63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112f485a28250abe3b6e3642aab0bec10ed25942c76caace5b473fcdf18abcf88f2b8bd2e00c967cdb6661eff0f30914db0b12f6a146d2adf5ca8e350e09ce8f6f3643f9523557b3cc69de0624275814dc58f41defc7663327a12249556594a014c18f4341345bd4066ae48b129f8622ac12d2323f19d1da993e482f0e5c103f8cd"
    aweme_id = "7333853807241088307"
    # aweme_id ="7322890094187138316"
    comment = DouyinComment(sec_user_id, uifid)
    comment.fetch_posts(aweme_id)

