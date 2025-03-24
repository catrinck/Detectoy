// PopupCadastro.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function PopupSetor({ onClose }) {

const navigate = useNavigate();

    return (
        <div className="popup-overlay">
            <div className="popup-content">

                <button className="close-button" onClick={onClose}>Fechar</button>
                <div className='rounded-full bg-[#3CAE49] items-center justify-center mt-8 '>
                    <img src="check-icon-white.svg" className='h-32 h-32' alt='ok' />
                </div>
                <h1 className='mt-16 text-[50px]'>Setor Cadastrado!</h1>
            
                <button className="px-16 py-3 font-bold bg-[#AE91E9] text-white items-center justify-center rounded-full " 
                            onClick={() =>
                                navigate("/reports") //navega para users
                              }>Voltar</button>
            
            </div>          

        </div>
    );
}

export default PopupSetor;