import asyncio
import websockets
import json
import cv2
import base64
import numpy as np

async def camera_stream():
    uri = "ws://localhost:8000/api/v1/camera/stream"
    
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                # Solicita um novo frame
                await websocket.send(json.dumps({"action": "get_frame"}))
                
                # Recebe resultados
                response = await websocket.recv()
                data = json.loads(response)
                
                if "error" in data:
                    print(f"Erro: {data['error']}")
                    break
                
                # Converte frame base64 para imagem
                img_bytes = base64.b64decode(data["frame"])
                nparr = np.frombuffer(img_bytes, np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                # Mostra resultados
                print(f"Tela quebrada: {data['broken_screen']}")
                print(f"Carcaça quebrada: {data['broken_shell']}")
                
                # Mostra frame
                cv2.imshow("Camera", frame)
                
                # Sai se pressionar 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    await websocket.send(json.dumps({"action": "stop"}))
                    break
                
        finally:
            cv2.destroyAllWindows()

if __name__ == "__main__":
    asyncio.run(camera_stream())