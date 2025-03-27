import React, { useEffect, useState, useRef } from 'react';

export default function Camera() {
    // Estados para controlar o componente da câmera
    const [connected, setConnected] = useState(false);
    const [detections, setDetections] = useState({
        broken_screen: false,
        broken_shell: false,
        saved_image: null
    });
    const [detectionHistory, setDetectionHistory] = useState([]);
    
    // Referências para o WebSocket e imagem
    const ws = useRef(null);
    const imageRef = useRef(null);

    useEffect(() => {
        // Inicializa a conexão WebSocket
        ws.current = new WebSocket('ws://localhost:8080/api/v1/camera/stream');

        // Manipulador de evento quando a conexão é estabelecida
        ws.current.onopen = () => {
            // Marca o estado como conectado
            setConnected(true);
            // Solicita o primeiro frame
            ws.current.send(JSON.stringify({ action: 'get_frame' }));
        };

        // Manipulador de evento para mensagens recebidas
        ws.current.onmessage = (event) => {
            const data = JSON.parse(event.data);
            
            // Verifica se há erro na mensagem
            if (data.error) {
                // Exibe o erro no console
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

        // Manipulador de erros no WebSocket
        ws.current.onerror = (error) => {
            console.error('WebSocket error:', error);
            setConnected(false);
        };

        // Manipulador quando a conexão é fechada
        ws.current.onclose = () => {
            setConnected(false);
        };

        // Função de limpeza quando o componente é desmontado
        return () => {
            if (ws.current) {
                ws.current.close();
            }
        };
    }, []);

    return (
        <div className="flex gap-4">
            {/* Área principal da câmera */}
            <div className='border-[#AE91E9] rounded-lg border-[2px] p-2 w-[640px]'>
                <h2 className="text-lg font-bold mb-2">Câmera em Tempo Real</h2>
                <div className='p-4'>
                    {!connected ? (
                        // Exibe mensagem quando não há conexão
                        <div className='bg-black rounded-lg p-16 m-2 flex items-center justify-center'>
                            <h1 className='text-white'>SEM SINAL</h1>
                        </div>
                    ) : (
                        // Exibe o stream da câmera quando conectado
                        <div className='relative'>
                            <img 
                                ref={imageRef}
                                className='rounded-lg w-full'
                                alt="Camera feed"
                            />
                            {/* Indicadores visuais para detecções */}
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

            {/* Área de histórico de detecções */}
            <div className='border-[#AE91E9] rounded-lg border-[2px] p-2 w-[300px]'>
                <h2 className="text-lg font-bold mb-2">Histórico de Detecções</h2>
                <div className="overflow-y-auto max-h-[600px]">
                    {detectionHistory.map((detection, index) => (
                        <div key={index} className="mb-4 p-2 border rounded">
                            <p className="text-sm mb-1">{detection.timestamp}</p>
                            <img 
                                src={`http://localhost:8080${detection.image}`}
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