import asyncio
import websockets
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def connect_websocket():
    uri = "ws://localhost:8000/api/v1/camera/stream"
    retry_count = 0
    max_retries = 3
    
    while retry_count < max_retries:
        try:
            async with websockets.connect(uri) as websocket:
                logger.info("Connected to camera stream")
                
                # Request 10 frames
                for i in range(10):
                    await websocket.send(json.dumps({"action": "get_frame"}))
                    response = await websocket.recv()
                    data = json.loads(response)
                    
                    if data.get("status") == "error":
                        logger.error(f"Frame error: {data['error']}")
                        continue
                        
                    logger.info(f"Frame {i+1}: Detected {data['detected_classes']}")
                    await asyncio.sleep(0.1)
                
                # Clean exit
                await websocket.send(json.dumps({"action": "stop"}))
                return
                
        except Exception as e:
            retry_count += 1
            logger.error(f"Connection attempt {retry_count} failed: {str(e)}")
            await asyncio.sleep(1)
    
    logger.error("Failed to connect after maximum retries")

if __name__ == "__main__":
    asyncio.run(connect_websocket())