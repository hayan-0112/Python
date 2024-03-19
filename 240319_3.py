import asyncio
import random

async def show(x): #async : 비동기 함수(동시 실행 가능)
    x = random.sample([1,2,3,4,5], k=1)
    await asyncio.sleep(x[0])
    print(x)
count = 0
async def main():
    await asyncio.gather( #await : async 함수 안에서만 사용 가능
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
    )
asyncio.run(main())