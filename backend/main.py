import random

async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    print("Requested:", scope["path"])
    n = random.randint(1, 10000)

    ans = f"rand num: {n}"
    
    await send({
        'type': 'http.response.body',
        'body': bytearray(ans, encoding="utf-8"),
    })