from fastapi import FastAPI, Query, status
import uvicorn
from Schemas import TagBook, Publisher
from naiin import findbook

app = FastAPI()


@app.get('/', status_code=status.HTTP_202_ACCEPTED)
async def home(tagbook: TagBook, publisher: Publisher, _q: str = Query(enum=["True", "False"])):
    publisher.phoenix._value_ = "005459"
    publisher.animag._value_ = "006485"
    publisher.firstpage._value_ = "004827"
    publisher.all._value_ = f"{publisher.phoenix._value_},{publisher.animag._value_},{publisher.firstpage._value_}"

    result = findbook(type=tagbook._name_, pub=publisher._value_)
    if result == None:
        return result

    target = ["แมงมุมแล้วไง", "ห้องเรียนจารชน", "แผนสมรสไม่สมเลิฟ", "โกนหนวดไปทำงานแล้วกลับบ้านมาพบเธอ", "ระยะห่างระหว่างเราใกล้กันไปมั้ย", "คาเฟ่นี้มีนางฟ้ามาเสิร์ฟ",
              "ขาดคุณนางฟ้าข้างห้องไป", "ประสบการณ์รักฉบับวุ่นวาย", "แฟนรุ่นพี่แค้นนี้ต้องชำระ", "Solo", "ชีวิตรสโซดาของจิโตเสะคุง", "แง้มหัวใจยัยน้องสาวจำเป็น", "คุณแม่ที่มีสกิลพื้นฐานเป็นการ"]
    if _q == "True":
        for x in range(len(result)):
            split = result[x]["title"]
            for y in target:
                if y in split:
                    print(f"Find : {result[x].values()}")

    return {f"Volume {len(result)}": result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
