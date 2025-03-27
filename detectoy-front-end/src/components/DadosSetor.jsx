import React, { useState } from 'react'
import GenericInput from './GenericInput'

export default function DadosSetor() {
    const [nome, setNome] = useState("");
    const [error, setError] = useState("");
    const [camera, setCamera] = useState("");
    const [isSubmitting, setIsSubmitting] = useState(false);

    const handleNomeChange = (value) => {
        setNome(value);
    };

    const handleCameraChange = (value) => {
        setCamera(value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setError("");
        
        // Validação básica
        if (!nome.trim()) {
            setError("Nome do setor é obrigatório");
            return;
        }
        
        setIsSubmitting(true);
        
        // Aqui iria a lógica de criação do setor com chamada à API
        setTimeout(() => {
            setIsSubmitting(false);
            // Reset dos campos após o sucesso
            setNome("");
            setCamera("");
        }, 1000);
    }

    return (
        <div className='border-2 border-gray-400 rounded-xl w-full'>

            {/* Título do Formulário */}
            <h3 className='px-5 py-2 font-semibold text-white bg-[#AE91E9] rounded-t-xl'>
                Dados do Setor
            </h3>

            <form onSubmit={handleSubmit}>

                <div className='flex flex-1'>
                    <div className="">

                        <GenericInput className=""
                            campo="Nome do Setor"
                            value={nome}
                            onChange={handleNomeChange} />

                        <div className='flex items-end  '>
                            <GenericInput
                                campo="Câmeras"
                                value={camera}
                                onChange={handleCameraChange} />

                            <button 
                                type="button" 
                                className='rounded-lg border-2 border-grey p-2 h-10 mb-5'
                            >
                                Adicionar Câmera
                            </button>
                        </div>
                    </div>
                </div>

                <div className="flex justify-end px-5 pb-3">
                    <button 
                        type="submit" 
                        className='rounded-lg bg-[#AE91E9] text-white p-2 px-5'
                        disabled={isSubmitting}
                    >
                        {isSubmitting ? 'Salvando...' : 'Salvar Setor'}
                    </button>
                </div>

                {/* Mensagem de erro */}
                {error && <p className="text-red-500 mt-2 px-5 pb-3">{error}</p>}

            </form>
        </div>
    )
}
