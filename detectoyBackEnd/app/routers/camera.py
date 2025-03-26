from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json
import logging
from ..services.camera_service import camera_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1")  # Add prefix here

@router.websocket("/camera/stream")
async def camera_stream(websocket: WebSocket):
    await websocket.accept()
    logger.info("New WebSocket connection established")
    
    try:
        camera_service.start_camera()
        
        while True:
            try:
                data = await websocket.receive_text()
                command = json.loads(data)
                
                if command["action"] == "get_frame":
                    frame = camera_service.get_frame()
                    results = camera_service.process_frame(frame)
                    
                    if results["status"] == "error":
                        logger.error(f"Error processing frame: {results['error']}")
                        await websocket.send_json({
                            "status": "error",
                            "error": results["error"]
                        })
                        continue
                    
                    await websocket.send_json(results)
                elif command["action"] == "stop":
                    break
                    
            except WebSocketDisconnect:
                logger.info("Client disconnected")
                break
            except Exception as e:
                logger.error(f"Error in WebSocket loop: {str(e)}")
                await websocket.send_json({
                    "status": "error",
                    "error": str(e)
                })
                break
                
    except Exception as e:
        logger.error(f"Fatal error in camera stream: {str(e)}")
        try:
            await websocket.send_json({
                "status": "error",
                "error": "Fatal error: " + str(e)
            })
        except:
            pass
    finally:
        camera_service.stop_camera()
        try:
            await websocket.close()
        except:
            pass
        logger.info("Camera stream closed")