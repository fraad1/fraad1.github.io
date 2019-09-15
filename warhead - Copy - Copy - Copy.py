from threading import Thread
import requests


def letsDoThis():
    burp0_url = "https://onlineplus.mofidonline.com:443/Customer/SendOrder"
    burp0_cookies = {"UserHasReadedHelp": "true", "_ga": "GA1.2.434933171.1567762252", "ASP.NET_SessionId": "qro03juxvfm1bat31cndya2t", "TS019a1d16": "01bc767316a90881747fccd306b1dcc881d6201adb5e57bdf7441b03439eb7f99917f2b63131946b9297b1b28a66b1ac48da41473b73bdf0ab05c9dd50b37a576de48d21022da9b1b8383d71e467706ea2ae2dedb115356f9ac01f76b4783ce7c019da72f0", "TS019a1d16_26": "01c0f187045a37822c2ce7a12ac06f4e0aac621e4b0b1a0524351de9a3d0c7f235b0f4155db3a663943f783874502b7243b08339a0ac4ad65d3210745b21f20a0f6dde6666", "crisp-client%2Fsession%2Fe95056ad-2681-452d-976d-0c2a304165c9": "session_be54fd1d-4743-4df3-b076-d0b025afdc55", "crisp-client%2Fsocket%2Fe95056ad-2681-452d-976d-0c2a304165c9": "0", ".ASPXAUTH": "45CEED7CF2F3D171859425145C08C765B3D7286C5371F23CE23FE6B00395A89F4BB547E70875BDE0450CFDD11A8C5BDC81665BD4E6DC774809921FF8DB9091D0164215E5C63D5D18BFA0B700AFF1B200EEAB905B34D3FE13BC49562C7E92EC2209FB58AB72B5C7805806754F4B4E00F1B387E1943CB6C2E00EB59F8E8ADC27DC", "Token": "a6f4b52d-b62d-4ce8-a216-8250a6f6f3d5", "_gid": "GA1.2.984534467.1568432473", "LS6_https_1603_943_TadbirConnection": "1568432756272|C|LS6__onlineplus_mofidonline_com_943_TadbirConnection|onlineplus.mofidonline.com", "LS6_https_1603_https%3A%2F%2Fpushv7.etadbir.com%2F": "|943_TadbirConnection|", "LS6_https_1603_TadbirConnection": "|943|"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Content-Type": "application/json", "Connection": "close", "Referer": "https://onlineplus.mofidonline.com/Home/Default/page-1"}
    burp0_json={"CautionAgreementSelected": False, "FinancialProviderId": 1, "isin": "IRO3GEMZ0001", "IsSymbolCautionAgreement": False, "IsSymbolSepahAgreement": False, "maxShow": 0, "minimumQuantity": "", "orderCount": 650, "orderId": 0, "orderPrice": 9601, "orderSide": 65, "orderValidity": 74, "orderValiditydate": None, "SepahAgreementSelected": False}
    a = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    print(a.text)


def runInParallel():
    for _ in range(10):
        Thread(target = letsDoThis).start()


runInParallel()


