import base64
import urllib
import requests
import json_excel

API_KEY = " "
SECRET_KEY = " "

def main(path, pdf_file_num):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice?access_token=" + get_access_token()

    # pdf_file 可以通过 get_file_content_as_base64("C:\fakepath\2409_03027_1.pdf",True) 方法获取
    pdf_file = get_file_content_as_base64(path,True)
    payload = f'pdf_file={pdf_file}&pdf_file_num={pdf_file_num}&seal_tag=false'
    # payload = f'ofd_file={pdf_file}&seal_tag=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))

    response.encoding = "utf-8"
    return response.text
    # print(response.text)


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':

    path = r""

    main(path,1)

