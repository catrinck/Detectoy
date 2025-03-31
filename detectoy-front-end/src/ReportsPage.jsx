import React, { useState, useEffect } from 'react'
import { Link, useNavigate, useLocation } from "react-router-dom";
import PopupCadastro from './PopupCadastro';
import Busca from './components/Busca';
import CardSetor from './components/CardSetor';
import SideBar from './components/SideBar';

export default function ReportsPage() {
    const [selectedButton, setSelectedButton] = useState(null);
    const navigate = useNavigate();
    const location = useLocation();
    const [showPopup, setShowPopup] = useState(false);

    useEffect(() => {
        const path = location.pathname;
        if (path === "/tela-inicial") {
            setSelectedButton("tela-inicial");
        } else if (path === "/reports") {
            setSelectedButton("reports");
        } else if (path === "/users") {
            setSelectedButton("users");
        } else {
            setSelectedButton(null);
        }
    }, [location]);

    const handleOpenPopup = () => {
        setShowPopup(true);
    };
    const handleClosePopup = () => {
        setShowPopup(false);
    };


    return (
        <div className='h-screen bg-[#D0D6E2] flex items-center justify-center w-screen'>
            <div className='p-10 w-[80%] rounded-md bg-[#0E123F] h-[80%] flex justify-between gap-6'>

                <div className='bg-white flex flex-col items-center justify-center rounded-md h-full w-full p-8'>
                    <header className='flex flex-1 justify-between flex-row items-center w-full'>
                        <h1 className='text-[#0E123F] font-bold text-[28px]'>Painel de Setores</h1>
                        <div className='flex flex-1 justify-end gap-8'>
                            <Busca/>
                            <button className="px-16 py-3 font-bold bg-[#AE91E9] text-white items-center justify-center rounded-full " 
                            onClick={() =>
                                navigate("/CadastrarSetor") //navega para users
                              }>Adicionar Setor</button>
                        </div>
                    </header>
                               {/* a ser ajustado */}
                    <div className='flex-1 mt-4 w-full '>
                        <div className='item-start grid grid-cols-4 gap-4 overflow-scroll h-[500px] '>
                            <CardSetor/>
                        </div>
                    </div>
                </div>

                {/* <div className='p-2 '> */}

                    <SideBar />

                {/* </div> */}

            </div>
        </div>
    );
}

