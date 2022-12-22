from fastapi import FastAPI,Query,status
import uvicorn
from Schemas import TagBook,Publisher
from naiin import findbook

app = FastAPI()

@app.get('/',status_code=status.HTTP_202_ACCEPTED)
async def home(tagbook:TagBook,publisher:Publisher,_q: str = Query(enum=["True", "False"])):
    if tagbook == "Coming":
        tagbook = "coming_soon"
        if publisher == "Phoenix":
            publisher = "005459"
            result = findbook(type=tagbook,pub=publisher)
        elif publisher == "Animag":
            publisher = "006485"
            result = findbook(type=tagbook,pub=publisher)
        elif publisher == "Firstpage":
            publisher = "004827"
            result = findbook(type=tagbook,pub=publisher)
        elif publisher == "Phoenix,Animag,Firstpage":
            publisher = "006485,004827,005459"
            result = findbook(type=tagbook,pub=publisher)
    elif tagbook == "New Arrival":
        tagbook = "new_arrival"
        if publisher == "Phoenix":
            publisher = "005459"
            result = findbook(type=tagbook,pub=publisher)
        elif publisher == "Animag":
            publisher = "006485"
            result = findbook(type=tagbook,pub=publisher)
        elif publisher == "Firstpage":
            publisher = "004827"
            result = findbook(type=tagbook,pub=publisher)
        elif publisher == "Phoenix,Animag,Firstpage":
            publisher = "006485,004827,005459"
            result = findbook(type=tagbook,pub=publisher)
        
    target = ["แมงมุมแล้วไง","ห้องเรียนจารชน","แผนสมรสไม่สมเลิฟ","โกนหนวดไปทำงานแล้วกลับบ้านมาพบเธอ","ระยะห่างระหว่างเราใกล้กันไปมั้ย","คาเฟ่นี้มีนางฟ้ามาเสิร์ฟ",
    "ขาดคุณนางฟ้าข้างห้องไป","ประสบการณ์รักฉบับวุ่นวายฯ","แฟนรุ่นพี่แค้นนี้ต้องชำระ","Solo","ชีวิตรสโซดาของจิโตเสะคุง","แง้มหัวใจยัยน้องสาวจำเป็น","คุณแม่ที่มีสกิลพื้นฐานเป็นการฯ"]
    if _q == "True":
        try:
            for x in range(len(result)):
                split = result[x]["title"].split(" ")
                for y in target:
                    if y in split:
                        print(f"Find : {result[x].values()}")
        except:
            pass
    
    try:            
        return {f"Volume {len(result)}":result}
    except Exception:
        return {f"Volume {result}":result}

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True)