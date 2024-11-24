# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import urllib

import requests

from API.spider import DouyinSpider


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    import datetime

    # 时间戳（以秒为单位）
    timestamp = 1705026000

    # 转换为 UTC 时间
    utc_time = datetime.datetime.utcfromtimestamp(timestamp)

    # 转换为本地时间（如果需要）
    local_time = datetime.datetime.fromtimestamp(timestamp)

    # 格式化为日志格式
    log_format = "%Y-%m-%d %H:%M:%S"
    formatted_utc_time = utc_time.strftime(log_format)
    formatted_local_time = local_time.strftime(log_format)

    print(f"UTC 时间: {formatted_utc_time}")
    print(f"本地时间: {formatted_local_time}")

    keyword = "大家各练各的，真是谁都没耽误"
    encoded_keyword = urllib.parse.quote(keyword, encoding='utf-8')
    print("real_keyword:    %E5%A4%A7%E5%AE%B6%E5%90%84%E7%BB%83%E5%90%84%E7%9A%84%EF%BC%8C%E7%9C%9F%E6%98%AF%E8%B0%81%E9%83%BD%E6%B2%A1%E8%80%BD%E8%AF%AF")
    print(f"encoded_keyword: {encoded_keyword}")


def load_DouYin_data():
    url = "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAATAf7yHksdW6CBPSjl9CW8k3c_x_drbwg0CVLTowlwzE&max_cursor=0&locate_item_id=7412589007651048745&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=2&publish_video_strategy_type=2&from_user_page=0&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=130.0.0.0&browser_online=true&engine_name=Blink&engine_version=130.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7431529453598393882&uifid=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112f485a28250abe3b6e3642aab0bec10ed25942c76caace5b473fcdf18abcf88f2b8bd2e00c967cdb6661eff0f30914db0b12f6a146d2adf5ca8e350e09ce8f6f3643f9523557b3cc69de0624275814dc58f41defc7663327a12249556594a014c18f4341345bd4066ae48b129f8622ac12d2323f19d1da993e482f0e5c103f8cd&verifyFp=verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5&fp=verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5&msToken=VQvnqAjMrz3lTcZuNnlXXLBpqTJuj7WOw-dbM2_0P-YvJFtEPER7U-6J3xcesl_9yebVIPCnl6l8t5roLuEmgobNC9qYEkZPVg3jDGBm2V-sIPCSzmf4tt9rkgnwHj0GaeqrwXBzjgY_-Zjwb01c-L6Bwke63-2qIvhsW3Pf&a_bogus=Ef4RhHWyQZ5nOdMS8cbVyRKlFSy%2FNsuycMi%2FRxNP7xz9bwzOPYNFdPSSGxwFs7Jro8pzh9I7mnelbDdcFtUiZHrkwmpfSk7Wgs%2Fc988L2qq6Gts%2FEHmKChuzqwsC0YkNaA9aiAgRAsMr2VnRVr5ZABMa95zH5cfgSrp9p%2Fb9bDS0pPgT9n27eniWCX6%3D"

    payload = {}
    headers = {
        'Host': 'www.douyin.com',
        'Cookie': 'ttwid=1%7CKV1fFHifopYoxvnFYTfuyh5X9raTklwVKg7ay9aAPWw%7C1730287805%7Cbc2d8c1dff2f5a632e283c5f432fd068d11938e31faac5318a39dac826614286; UIFID_TEMP=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d1122189c816f1a8afdbfcce3019e48ff107f25ae055b17205681c4d0697592cb98c572da47acbe0c611d165e163b613ecba; s_v_web_id=verify_m2vsoqat_vhdxwbqw_hpAE_4Ftt_Af1N_ssnNcxj7ADO5; hevc_supported=true; dy_swidth=1536; dy_sheight=864; FORCE_LOGIN=%7B%22isForcePopClose%22%3A1%2C%22videoConsumedRemainSeconds%22%3A180%7D; fpk1=U2FsdGVkX1+3JK51xSSDpeK5s7asYeyZF7reCA+oraUSydh9wUsFEDqXCjwvuGxcMp0QOALwnxis89brHpI7ng==; fpk2=7675d59b5e84e0a878ee6f0a97f9056f; passport_csrf_token=9f15399129b85c0ed48e8e879c87526a; passport_csrf_token_default=9f15399129b85c0ed48e8e879c87526a; bd_ticket_guard_client_web_domain=2; UIFID=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112f485a28250abe3b6e3642aab0bec10ed25942c76caace5b473fcdf18abcf88f2b8bd2e00c967cdb6661eff0f30914db0b12f6a146d2adf5ca8e350e09ce8f6f3643f9523557b3cc69de0624275814dc58f41defc7663327a12249556594a014c18f4341345bd4066ae48b129f8622ac12d2323f19d1da993e482f0e5c103f8cd; passport_assist_user=CjzabjIXKUpirMADwElVFw4QooKom0NFPp5KczMdZC34Gq4vf95vsFGYMhy5Kh7o7SFcUc5OOJRcbXbiSqcaSgo8fcGQF6f1P0_eaS5_1SuYJk0aeyUebqGfFtJnii5NHaCZjHyIapnvo796HlLimPWBLIhJ9-PJrpH1Uw6KEKyQ4A0Yia_WVCABIgED1EIebA%3D%3D; n_mh=k0ZDMEx4Mj4G_Ef1j7IuX3CdzihZ3eDtIXPi4A5GPNk; sso_uid_tt=c50396f34c6b30c8f3fe4503bf05c0c4; sso_uid_tt_ss=c50396f34c6b30c8f3fe4503bf05c0c4; toutiao_sso_user=ef55db02b32e8e69cd98795df95f93c3; toutiao_sso_user_ss=ef55db02b32e8e69cd98795df95f93c3; sid_ucp_sso_v1=1.0.0-KGVjODg5OWZmZTE5ZjQ1ZjUxYzVlYzFiODhiMTAzMmFlMWFlNTBlMDIKHwignryw5wIQ4bGIuQYY7zEgDDDFj4nWBTgGQPQHSAYaAmxmIiBlZjU1ZGIwMmIzMmU4ZTY5Y2Q5ODc5NWRmOTVmOTNjMw; ssid_ucp_sso_v1=1.0.0-KGVjODg5OWZmZTE5ZjQ1ZjUxYzVlYzFiODhiMTAzMmFlMWFlNTBlMDIKHwignryw5wIQ4bGIuQYY7zEgDDDFj4nWBTgGQPQHSAYaAmxmIiBlZjU1ZGIwMmIzMmU4ZTY5Y2Q5ODc5NWRmOTVmOTNjMw; login_time=1730287844724; passport_auth_status=7c54df04feebcd9646de4a41e6365d7f%2C; passport_auth_status_ss=7c54df04feebcd9646de4a41e6365d7f%2C; uid_tt=54993fb8d64563b1f0d12322aea4c5be; uid_tt_ss=54993fb8d64563b1f0d12322aea4c5be; sid_tt=cf0cb56cc1a5a13e1776ea078be48aab; sessionid=cf0cb56cc1a5a13e1776ea078be48aab; sessionid_ss=cf0cb56cc1a5a13e1776ea078be48aab; is_staff_user=false; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=0f526cbe559bb7eb2631f177fdc0ec95; __security_server_data_status=1; sid_guard=cf0cb56cc1a5a13e1776ea078be48aab%7C1730287855%7C5183989%7CSun%2C+29-Dec-2024+11%3A30%3A44+GMT; sid_ucp_v1=1.0.0-KDA0MjhjMDRiMDU4ZGExOWUwMGQzOTA0NTM0MTAzZjMyZjAxYjhmMDMKGQignryw5wIQ77GIuQYY7zEgDDgGQPQHSAQaAmxmIiBjZjBjYjU2Y2MxYTVhMTNlMTc3NmVhMDc4YmU0OGFhYg; ssid_ucp_v1=1.0.0-KDA0MjhjMDRiMDU4ZGExOWUwMGQzOTA0NTM0MTAzZjMyZjAxYjhmMDMKGQignryw5wIQ77GIuQYY7zEgDDgGQPQHSAQaAmxmIiBjZjBjYjU2Y2MxYTVhMTNlMTc3NmVhMDc4YmU0OGFhYg; publish_badge_show_info=%220%2C0%2C0%2C1730287857737%22; h265ErrorNum=-1; store-region=cn-hb; store-region-src=uid; xgplayer_user_id=257565671676; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.743%7D; strategyABtestKey=%221730342934.842%22; download_guide=%223%2F20241031%2F0%22; SEARCH_RESULT_LIST_TYPE=%22single%22; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; csrf_session_id=a30f1cb500e93642d0c6109b37a87f08; webcast_leading_last_show_time=1730350565054; webcast_leading_total_show_times=1; pwa2=%220%7C0%7C3%7C0%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA3DgglHnUfteMFNj7ZPn5ZzQ5wu_fNMuNBBC1ThLcoHQ%2F1730390400000%2F0%2F1730372208744%2F0%22; WallpaperGuide=%7B%22showTime%22%3A1730287874046%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A35%2C%22cursor2%22%3A10%2C%22hoverTime%22%3A1730301787305%7D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_nonce=067236bc300088dd0ba6b; __ac_signature=_02B4Z6wo00f01WPgqLAAAIDBVMRs75dEdFVjwKwAAD.fSaLRWO65YPjgwLeDmLygj-vkug92kgogdaI05ljrG2VzVR7tf-.c5HLWuVaNhfoZHOjj4ntOrpgNmU6tqlnhDg-6g0wRCd7goGNFf5; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A200%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA3DgglHnUfteMFNj7ZPn5ZzQ5wu_fNMuNBBC1ThLcoHQ%2F1730390400000%2F0%2F1730374597192%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT1pUNWJnMFVXb014cm91Y01mOGRRZEJGM3ZzZStoT3lrTlNZUDdGWU1HYlp3MDRLZEthOWY4NTMrNG14dUt1eGIyN0FQK3BkdDFJR3g5ZDVkQ2VHekE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; odin_tt=b0ac6cda7ad8f80f22ab192ec5213df6aea7f8dd6f32748c568b378ee9b5b221228676e26f82d1a114dd80868bdefc1d; IsDouyinActive=true; xg_device_score=7.90435294117647',
        'uifid': '63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112f485a28250abe3b6e3642aab0bec10ed25942c76caace5b473fcdf18abcf88f2b8bd2e00c967cdb6661eff0f30914db0b12f6a146d2adf5ca8e350e09ce8f6f3643f9523557b3cc69de0624275814dc58f41defc7663327a12249556594a014c18f4341345bd4066ae48b129f8622ac12d2323f19d1da993e482f0e5c103f8cd',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.douyin.com/?recommend=1',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'priority': 'u=1, i',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'Postman-Token': '38e43abf-ba41-42f5-a403-7f5874d68b24'
    }

    response = requests.request("GET", url, headers=headers,proxies={"http": None, "https": None} ,data=payload)

    print(response.text)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sec_user_id = "MS4wLjABAAAAwHgIE1Q9ZfFmEN0DCBIAQmZFsTp767B3fVPw0tso6wGwllz-Tz2ASCyHa1kgZBy3"  # 替换为您的sec_user_id
    uifid = "63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112f485a28250abe3b6e3642aab0bec10ed25942c76caace5b473fcdf18abcf88f2b8bd2e00c967cdb6661eff0f30914db0b12f6a146d2adf5ca8e350e09ce8f6f3643f9523557b3cc69de0624275814dc58f41defc7663327a12249556594a014c18f4341345bd4066ae48b129f8622ac12d2323f19d1da993e482f0e5c103f8cd"
    spider = DouyinSpider(sec_user_id, uifid)
    spider.fetch_posts()
    load_DouYin_data()
    requests.post()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
