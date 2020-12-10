import requests
import randomheaders
import bs4

"""The post request to add an item to basket has been nearly completed. The response
kepps throwing a 500 which I assume has to do with the form data
Need to then do the one for check basket next. Also need to move eveyrhting into sessions when all working. 
Using proxies right now to test multiple times"""

def main(url):
    # Add to Basket

    with requests.Session() as s:
        proxy = {"http": "http://20982c0c036b4a639067f3dc6634056b:@proxy.crawlera.com:8010/",}
        res = s.get(url, headers=randomheaders.LoadHeader())
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        #form
        elem = soup.select('button[class="product-details__cta js-product-cta '
                            'button button--big button--rectangle button--transactional"]')[0]
        sku = elem['data-sku']
        token = elem['data-csrftoken']
        print(int(sku), token)

        data = {'sku': sku,
                'CSRFToken': token,
                'qty': 1,
                'url': '/api/cart/add',
                'action': 'add'}

        res = s.post(url, data=data)
        print(res.status_code, res.url)
        # soup = bs4.BeautifulSoup(res.text, 'lxml')
        # success = soup.select('div[class="minicart__link--count js-minicart-totalCount "]')[0].text
        # print(success)



# <div class="minicart__link--count js-minicart-totalCount ">
# 1</div>

# sku: 700170360933900
# CSRFToken: 9c3692f5-d6b3-4f5c-abd3-088c53d67672
# qty: 1
# url: /api/cart/add
# action: add



main("https://www.aldi.co.uk/hatchimals-hatchibuddies/p/700170360933900")



# sku = soup.select('div[class="product-details__code"]')[0].text.strip()
# sku = [s for s in sku.split() if s.isdigit()]
# sku = "".join(sku)

# basket: {lineItems: [{id: "700170360933900", quantity: 1, unitPrice: 8.99, category: "toys"}]}
# client: {expectedSiteConfigVersion: "3/1"}
# experiment: {id: "tvt2", group: "treatment"}
# visitor: {sessionId: "4ce161e4-3991-11eb-8bed-4dfc2829c21d", id: "4ce161e4-3991-11eb-8bed-4dfc2829c21d"}