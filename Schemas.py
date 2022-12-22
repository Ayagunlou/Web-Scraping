from enum import Enum

class TagBook(str,Enum):
    coming = "Coming"
    new = "New Arrival"

class Publisher(str,Enum):
    phoenix = "Phoenix"
    animag = "Animag"
    firstpage = "Firstpage"
    all = f"{phoenix},{animag},{firstpage}"


# def convert(data) -> dict:
#         return {
#             "title":data["title"],
#             "link":data["link"],
#             "status":data["status"]
#         }
# def dataList(users) -> list:
#         return [convert(user) for user in users]
