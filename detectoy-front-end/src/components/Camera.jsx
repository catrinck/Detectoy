import React, { useEffect, useState, useRef } from 'react';

export default function Camera() {
    const [connected, setConnected] = useState(false);
    const [detections, setDetections] = useState({
        broken_screen: false,
        broken_shell: false,
        saved_image: null
    });
    const [detectionHistory, setDetectionHistory] = useState([]);
    const ws = useRef(null);
    const imageRef = useRef(null);

    useEffect(() => {
        // Conecta ao WebSocket
        ws.current = new WebSocket('ws://localhost:8080/api/v1/camera/stream');

        ws.current.onopen = () => {
            console.log('Connected to camera stream');
            setConnected(true);
            ws.current.send(JSON.stringify({ action: 'get_frame' }));
        };

        ws.current.onmessage = (event) => {
            const data = JSON.parse(event.data);
            
            if (data.error) {
                console.error('Camera error:', data.error);
                return;
            }

            // Atualiza a imagem
            if (imageRef.current && data.frame) {
                imageRef.current.src = `data:image/jpeg;base64,${data.frame}`;
            }

            // Se houver uma nova detecção com imagem salva, adiciona ao histórico
            if (data.saved_image) {
                setDetectionHistory(prev => [...prev, {
                    timestamp: new Date().toLocaleTimeString(),
                    image: data.saved_image,
                    broken_screen: data.broken_screen,
                    broken_shell: data.broken_shell
                }]);
            }

            // Atualiza estado das detecções
            setDetections({
                broken_screen: data.broken_screen,
                broken_shell: data.broken_shell,
                saved_image: data.saved_image
            });

            // Solicita próximo frame
            ws.current.send(JSON.stringify({ action: 'get_frame' }));
        };

        ws.current.onerror = (error) => {
            console.error('WebSocket error:', error);
            setConnected(false);
        };

        ws.current.onclose = () => {
            console.log('Disconnected from camera stream');
            setConnected(false);
        };

        return () => {
            if (ws.current) {
                ws.current.close();
            }
        };
    }, []);

    return (
        <div className="flex gap-4">
            <div className='border-[#AE91E9] rounded-lg border-[2px] p-2 w-[640px]'>
                <h2 className="text-lg font-bold mb-2">Câmera em Tempo Real</h2>
                <div className='p-4'>
                    {!connected ? (
                        <div className='bg-black rounded-lg p-16 m-2 flex items-center justify-center'>
                            <h1 className='text-white'>SEM SINAL</h1>
                        </div>
                    ) : (
                        <div className='relative'>
                            <img 
                                ref={imageRef}
                                className='rounded-lg w-full'
                                alt="Camera feed"
                            />
                            <div className='absolute top-2 right-2 flex gap-2'>
                                {detections.broken_screen && (
                                    <span className='bg-red-500 text-white px-2 py-1 rounded-md text-sm'>
                                        Tela Quebrada
                                    </span>
                                )}
                                {detections.broken_shell && (
                                    <span className='bg-red-500 text-white px-2 py-1 rounded-md text-sm'>
                                        Carcaça Quebrada
                                    </span>
                                )}
                            </div>
                        </div>
                    )}
                </div>
            </div>

            <div className='border-[#AE91E9] rounded-lg border-[2px] p-2 w-[300px]'>
                <h2 className="text-lg font-bold mb-2">Histórico de Detecções</h2>
                <div className="overflow-y-auto max-h-[600px]">
                    {detectionHistory.map((detection, index) => (
                        <div key={index} className="mb-4 p-2 border rounded">
                            <p className="text-sm mb-1">{detection.timestamp}</p>
                            <img 
                                src={`http://localhost:8000${detection.image}`}
                                alt="Detection"
                                className="w-full rounded"
                            />
                            <div className="mt-1 text-sm">
                                {detection.broken_screen && <span className="text-red-500 mr-2">Tela Quebrada</span>}
                                {detection.broken_shell && <span className="text-red-500">Carcaça Quebrada</span>}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}