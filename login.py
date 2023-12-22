"""
run
执行一次扫码登录流程
"""
import utils
import time
import show_img
from PIL import Image


def get_cookie() -> dict:
    """
    扫码登录流程
    :return: None
    """
    config = utils.load_json_file(path="./config/config.json")
    # url_get_qrcode: 访问申请二维码，获取qrcode_key和二维码地址url_qrcode
    url_get_qrcode = config['url']['url_get_qrcode']
    # url_check_scan: 访问获取登录状态
    url_check_scan = config['url']['url_check_scan']

    headers = config['headers']
    # 保存二维码图片，并获取对应的qrcode_key
    qrcode_key = utils.save_img(url=url_get_qrcode, headers=headers, img_location=config['qrcode_location'])
    img = Image.open(config['qrcode_location'])
    # 二维码图片以字符串形式输出到控制台
    show_img.print_qrcode(img=img)

    print("请扫码")
    while True:
        # 获取登录状态
        result_check_scan = utils.check_scan(url=url_check_scan, qrcode_key=qrcode_key, headers=headers)
        data_result = result_check_scan['data']
        """
        code
        0:    扫码登录成功
        86038:二维码已失效
        86090:二维码已扫码未确认
        86101:未扫码
        """
        result_code = data_result['code']
        if result_code == 86101:
            time.sleep(2)
        elif result_code == 86090:
            time.sleep(2)
        elif result_code == 86038:
            print(data_result['message'], "重新获取中")
            qrcode_key = utils.save_img(url=url_get_qrcode, headers=headers, img_location=config['qrcode_location'])
            time.sleep(1)
        elif result_code == 0:
            print("登录成功，获取cookie中")
            return result_check_scan['response'].cookies.get_dict()
        else:
            print("未知扫码状况")
