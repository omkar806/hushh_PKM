import asyncio
import websockets
import json
from fastapi import WebSocket

# WebSocket.send_json()
# WebSocket.receive_json()

async def receive_data(access_token: str, brand_name: str = None):
    if access_token is None:
        return "Access token not provided"
    
    uri = "wss://hushh-hushh-valet-chat.hf.space/websockets/ws"
    
    try:
        async with websockets.connect(uri) as websocket:
            print("WebSocket connection established")

            # Now that the connection is established, you can send data
            data = {'access_token':access_token , 'brand_name':brand_name}
            text = json.dumps(data, separators=(",",":"), ensure_ascii=False)

            if brand_name is not None:
                await websocket.send(text)
                print("Data sent:", brand_name)
            
            while True:
                # Receive data from the websocket server
                data = await websocket.recv()
                print("Received:", data)

    except websockets.WebSocketException as e:
        print(f"WebSocket connection failed: {e}")

# Example usage
# asyncio.get_event_loop().run_until_complete(receive_data("your_access_token", "your_brand_name"))
