import React, { useState, useEffect } from 'react'
import { Link, useNavigate, useLocation } from "react-router-dom";
import Busca from './components/Busca';
import CardSetor from './components/CardSetor';
import SideBar from './components/SideBar';
import DadosSetor from './components/DadosSetor';
import Camera from './components/Camera';
import PopupSetor from './components/PopUpSetor';



export default function CadastrarSetor({ handleSubmit }) {
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

                <div className='bg-white rounded-md h-full w-[81.75rem] p-12'>
                    <header className='flex flex-1'>
                        <h1 className='text-[#0E123F] font-bold text-[28px]'>Cadastrar Setores</h1>

                    </header>

                    <div className='flex-1 mt-4 '>
                        <div className=' item-start '>
                            <div className='flex '>
                                <DadosSetor></DadosSetor>
                                <Camera />
                            </div>
                            <div className="flex justify-end gap-2 mt-[4rem]">
                                <button
                                    type="button"
                                    onClick={() => navigate("/reports")}
                                    className="bg-gray-400 text-white px-4 py-2 rounded-lg hover:bg-gray-500">
                                    Cancelar
                                </button>

                                <button
                                    type="submit"
                                    onClick={handleOpenPopup}
                                    className="bg-[#AE91E9] text-white px-4 py-2 rounded-lg hover:bg-[#1D1D1D]">
                                    Prosseguir
                                </button>
                                {showPopup && <PopupSetor onClose={handleClosePopup} />}

                            </div>

                        </div>
                    </div>

                </div>

                <div className='p-2 '>

                    <SideBar />

                </div>

            </div>
        </div>
    );
}

