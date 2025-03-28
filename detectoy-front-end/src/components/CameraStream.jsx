import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import SideBar from './SideBar';

export default function CameraStream() {
    const [isStreaming, setIsStreaming] = useState(false);
    const [error, setError] = useState(null);
    const [capturedFrame, setCapturedFrame] = useState(null);
    const streamRef = useRef(null);

    const startStream = async () => {
        try {
            // Usar porta 8080 conforme configurado no .env
            await axios.get('http://localhost:8080/api/v1/webcam/start');
            setIsStreaming(true);
            
            if (setIsStreaming(true)) {  
                streamRef.current.src = 'http://localhost:8080/api/v1/webcam/stream';
                streamRef.current.onerror = () => {
                    setError('Erro ao carregar stream da câmera');
                    setIsStreaming(false);
                };
            }
        } catch (error) {
            if (error.code === 'ERR_NETWORK') {
                setError('Erro de conexão: Verifique se o servidor está rodando');
            } else {
                setError('Erro ao iniciar câmera: ' + (error.response?.data?.detail || error.message));
            }
            console.error(error);
            setIsStreaming(false);
        }
    };

    const stopStream = async () => {
        try {
            await axios.get('http://localhost:8080/api/v1/webcam/stop');
            setIsStreaming(false);
            if (streamRef.current) {
                streamRef.current.src = '';
            }
        } catch (error) {
            setError('Erro ao parar câmera: ' + (error.response?.data?.detail || error.message));
            console.error(error);
        }
    };

    const captureFrame = async () => {
        try {
            const response = await axios.get('http://localhost:8080/api/v1/webcam/frame');
            const data = response.data;
            if (data.result_image) {
                setCapturedFrame(data);
            }
        } catch (error) {
            setError('Erro ao capturar frame: ' + (error.response?.data?.detail || error.message));
            console.error(error);
        }
    };

    useEffect(() => {
        return () => {
            if (isStreaming) {
                stopStream();
            }
        };
    }, []);

    return (
        <div className='h-screen bg-[#D0D6E2] flex items-center justify-center w-screen'>
            <div className='p-10 w-[80%] rounded-md bg-[#0E123F] h-[80%] flex justify-between gap-6'>
                <div className='bg-white flex flex-col rounded-md h-full w-full p-8'>
                    <h1 className='text-2xl font-bold mb-4'>Stream da Câmera</h1>
                    
                    <div className='flex flex-col gap-4'>
                        <div className='relative bg-black rounded-lg overflow-hidden' style={{height: '480px'}}>
                            {!isStreaming ? (
                                <div className='absolute inset-0 flex items-center justify-center text-white'>
                                    CÂMERA DESLIGADA
                                </div>
                            ) : (
                                <img
                                    ref={streamRef}
                                    className='w-full h-full object-contain'
                                    alt="Camera stream"
                                    onError={() => {
                                        setError('Erro ao carregar imagem');
                                        setIsStreaming(false);
                                    }}
                                />
                            )}
                        </div>

                        <div className='flex gap-4 justify-center'>
                            <button
                                onClick={startStream}
                                disabled={isStreaming}
                                className='bg-green-500 text-white px-4 py-2 rounded disabled:bg-gray-400'
                            >
                                Iniciar Stream
                            </button>
                            <button
                                onClick={stopStream}
                                disabled={!isStreaming}
                                className='bg-red-500 text-white px-4 py-2 rounded disabled:bg-gray-400'
                            >
                                Parar Stream
                            </button>
                            <button
                                onClick={captureFrame}
                                disabled={!isStreaming}
                                className='bg-blue-500 text-white px-4 py-2 rounded disabled:bg-gray-400'
                            >
                                Capturar Frame
                            </button>
                        </div>

                        {error && (
                            <div className='text-red-500 text-center'>
                                {error}
                            </div>
                        )}

                        {capturedFrame && (
                            <div className='mt-4'>
                                <h2 className='text-xl font-bold mb-2'>Frame Capturado:</h2>
                                <img
                                    src={`data:image/jpeg;base64,${capturedFrame.result_image}`}
                                    alt="Captured frame"
                                    className='max-w-full rounded-lg'
                                />
                                {capturedFrame.broken_screen && 
                                    <div className='mt-2 text-red-500'>Tela Quebrada Detectada</div>
                                }
                                {capturedFrame.broken_shell && 
                                    <div className='mt-2 text-red-500'>Carcaça Quebrada Detectada</div>
                                }
                            </div>
                        )}
                    </div>
                </div>
                <SideBar />
            </div>
        </div>
    );
}
