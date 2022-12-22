from bs4 import BeautifulSoup
import requests

def findbook(type,pub):
    # coming = "coming_soon"
    # new = "new_arrival"
    # book_find = "006485,004827,005459"
    # phoenix = "005459"
    # animag = "006485"
    # firstpage = "004827"

    url = f"https://www.naiin.com/category?type_book={type}&product_type_id=1&p={pub}"
    page = requests.get(url).text
    doc = BeautifulSoup(page,"html.parser")

    div = doc.find(class_ ="product-list mt15 mb15 view-block grid")
    try:
        items = div.find_all(class_ = "itemname")
    except Exception: 
        return None

    items3 = div.find_all(class_ = "btn-addtocart-ylw-small")

    list1 =[]
    list1_link =[]
    list3 = [] 

    for item in items:
        list1.append(item.string)
        list1_link.append(item["href"])

    for i in items3:
        list3.append(i.string)

    result = []
    for x,y,z in zip(list1,list1_link,list3):
        books = {
            "title":str(x),
            "link":str(y),
            "status":str(z)
        }
        result.append(books)

    return result
