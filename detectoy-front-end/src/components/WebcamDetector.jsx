import React, { useEffect, useState, useRef } from 'react';

export default function WebcamDetector() {
    // Estados para controlar o componente da câmera
    const [detections, setDetections] = useState({
        broken_screen: false,
        broken_shell: false,
        result_image: null
    });
    const [detectionHistory, setDetectionHistory] = useState([]);
    
    // Referências para o WebSocket e vídeo
    const ws = useRef(null);
    const videoRef = useRef(null);

    useEffect(() => {
        // Inicializa a conexão WebSocket para detecções
        ws.current = new WebSocket('ws://127.0.0.1:8080/ws/detections');

        // Manipulador de evento quando a conexão é estabelecida
        ws.current.onopen = () => {
            // Conexão estabelecida - pronto para receber dados
        };

        // Manipulador de evento para mensagens recebidas
        ws.current.onmessage = (event) => {
            const data = JSON.parse(event.data);
            
            // Atualiza o estado das detecções
            setDetections({
                broken_screen: data.broken_screen,
                broken_shell: data.broken_shell,
                result_image: data.result_image
            });

            // Se houver uma nova detecção com imagem salva, adiciona ao histórico
            if (data.result_image) {
                setDetectionHistory(prev => [...prev, {
                    timestamp: new Date().toLocaleTimeString(),
                    image: data.result_image,
                    broken_screen: data.broken_screen,
                    broken_shell: data.broken_shell
                }]);
            }
        };

        // Manipulador de erros no WebSocket
        ws.current.onerror = (error) => {
            console.error('Erro no WebSocket:', error);
        };

        // Manipulador quando a conexão é fechada
        ws.current.onclose = () => {
            // Conexão WebSocket fechada
        };

        // Inicia o stream da câmera
        if (videoRef.current) {
            videoRef.current.src = 'http://127.0.0.1:8080/api/v1/webcam/stream';
        }

        // Função de limpeza quando o componente é desmontado
        return () => {
            if (ws.current) {
                ws.current.close();
            }
            if (videoRef.current) {
                videoRef.current.src = '';
            }
        };
    }, []);

    return (
        <div className="flex gap-4">
            {/* Área principal da câmera */}
            <div className='border-[#AE91E9] rounded-lg border-[2px] p-2 w-[640px]'>
                <h2 className="text-lg font-bold mb-2">Detecção em Tempo Real</h2>
                <div className='p-4'>
                    <div className='relative'>
                        <video
                            ref={videoRef}
                            autoPlay
                            playsInline
                            className='rounded-lg w-full'
                            style={{ maxHeight: '480px', objectFit: 'contain' }}
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
                                src={`http://127.0.0.1:8080${detection.image}`}
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