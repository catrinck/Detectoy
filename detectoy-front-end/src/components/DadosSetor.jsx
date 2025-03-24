import React, { useState } from 'react'
import GenericInput from './GenericInput'
import Camera from './Camera';


export default function DadosSetor() {
    const [nome, setNome] = useState("");
    const [error, setError] = useState("");
    const [camera, setCamera] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault()
        setError("")
        console.log("peru")
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
                            onChange={setNome} />

                        <div className='flex items-end  '>
                            <GenericInput
                                campo="Câmeras"
                                value={camera}
                                onChange={setCamera} />

                            <button className='rounded-lg border-2 border-grey p-2 h-10 mb-5'>Adicionar Câmera</button>
                        </div>
                    </div>
                   

                </div>


                {/* Mensagem de erro */}
                {error && <p className="text-red-500 mt-2">{error}</p>}

            </form>
        </div>
    )
}
