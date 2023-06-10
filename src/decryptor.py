from urllib.request import urlopen, Request

def get_final_link(url):
    if not url.startswith("http") or not url.startswith("http"):
        url = "https://" + url
    
    httprequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    with urlopen(httprequest) as response:
        return response.url
