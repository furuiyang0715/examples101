import json
import requests
from lxml import html

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}


def download_picture(url):
    pic_name = url.split("/")[-1]
    content = requests.get(url, headers=headers).content
    with open("/Users/furuiyang/Desktop/zhihu/{}".format(pic_name), "wb") as f:
        f.write(content)


def crawl(offset):
    url = 'https://www.zhihu.com/api/v4/questions/363414427/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics' \
          '&offset={}&limit=20&sort_by=updated'.format(offset)
    r = requests.get(url, verify=False, headers=headers)
    content = r.content.decode("utf-8")
    ret = json.loads(content)
    answers = ret.get("data")
    for answer in answers:
        content = answer.get("content")
        doc = html.fromstring(content)
        imgs = doc.xpath("//img/@src")
        imgs = [img for img in imgs if img.startswith("http")]
        if not imgs:
            continue
        for img in imgs:
            download_picture(img)


def main():
    # 根据页面问题的个数进行调整
    for i in range(0, 4):
        crawl(i*20)


def t_test():
    url = 'https://pic1.zhimg.com/50/v2-6903b90b39babdfd4bfe1bb602ddd791_hd.jpg'
    resp = requests.get(url)
    content = resp.content
    with open('temp.jpg', "wb") as f:
        f.write(content)


if __name__ == "__main__":
    main()

    # t_test()
