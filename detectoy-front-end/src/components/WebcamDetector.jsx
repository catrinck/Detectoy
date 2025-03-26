import React, { useEffect, useState, useRef } from 'react';

export default function WebcamDetector() {
    const [isRunning, setIsRunning] = useState(false);
    const [detections, setDetections] = useState([]);
    const [currentFrame, setCurrentFrame] = useState(null);
    const [error, setError] = useState(null);
    const intervalRef = useRef(null);

    const startCamera = async () => {
        try {
            setError(null);
            const response = await fetch('http://localhost:8000/api/v1/webcam/start');
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Falha ao iniciar câmera');
            }
            setIsRunning(true);
            startFrameCapture();
        } catch (error) {
            console.error('Erro ao iniciar câmera:', error);
            setError(error.message);
            setIsRunning(false);
        }
    };

    const stopCamera = async () => {
        try {
            setError(null);
            const response = await fetch('http://localhost:8000/api/v1/webcam/stop');
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Falha ao parar câmera');
            }
            setIsRunning(false);
            if (intervalRef.current) {
                clearInterval(intervalRef.current);
            }
        } catch (error) {
            console.error('Erro ao parar câmera:', error);
            setError(error.message);
        }
    };

    const captureFrame = async () => {
        try {
            setError(null);
            const response = await fetch('http://localhost:8000/api/v1/webcam/frame');
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Falha ao capturar frame');
            }
            
            const data = await response.json();
            setCurrentFrame(`data:image/jpeg;base64,${data.frame}`);
            
            // Se houver detecção, adiciona ao histórico
            if (data.detections.saved_image) {
                setDetections(prev => [{
                    timestamp: new Date().toLocaleTimeString(),
                    image: data.detections.saved_image,
                    broken_screen: data.detections.broken_screen,
                    broken_shell: data.detections.broken_shell
                }, ...prev]);
            }
        } catch (error) {
            console.error('Erro ao capturar frame:', error);
            setError(error.message);
        }
    };

    const startFrameCapture = () => {
        // Captura um frame a cada 500ms
        intervalRef.current = setInterval(captureFrame, 500);
    };

    useEffect(() => {
        return () => {
            if (intervalRef.current) {
                clearInterval(intervalRef.current);
            }
            stopCamera();
        };
    }, []);

    return (
        <div className="flex gap-4">
            <div className='border-[#AE91E9] rounded-lg border-[2px] p-2 w-[640px]'>
                <h2 className="text-lg font-bold mb-2">Câmera em Tempo Real</h2>
                <div className='p-4'>
                    {error && (
                        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                            {error}
                        </div>
                    )}
                    {!isRunning ? (
                        <div className='bg-black rounded-lg p-16 m-2 flex items-center justify-center'>
                            <h1 className='text-white'>CÂMERA DESLIGADA</h1>
                        </div>
                    ) : (
                        <div className='relative'>
                            <img 
                                src={currentFrame}
                                className='rounded-lg w-full'
                                alt="Camera feed"
                            />
                        </div>
                    )}
                    <div className="mt-4 flex justify-center gap-4">
                        <button
                            onClick={startCamera}
                            disabled={isRunning}
                            className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 disabled:bg-gray-400"
                        >
                            Iniciar Câmera
                        </button>
                        <button
                            onClick={stopCamera}
                            disabled={!isRunning}
                            className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 disabled:bg-gray-400"
                        >
                            Parar Câmera
                        </button>
                    </div>
                </div>
            </div>

            <div className='border-[#AE91E9] rounded-lg border-[2px] p-2 w-[300px]'>
                <h2 className="text-lg font-bold mb-2">Histórico de Detecções</h2>
                <div className="overflow-y-auto max-h-[600px]">
                    {detections.map((detection, index) => (
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