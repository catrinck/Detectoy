import React, { useState, useEffect } from 'react'
import { Link, useNavigate, useLocation } from "react-router-dom";
import CardUser from '../components/CardUser';
import SideBar from '../components/SideBar';
import Busca from '../components/Busca';
import PopupCadastro from '../PopupCadastro';

export default function Users() {
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
            <div className='p-10 w-[80%] rounded-md bg-[#0E123F] h-[80%] flex justify-between gap-6 '>

                <div className='bg-white flex flex-col items-center justify-center rounded-md h-full w-full p-8'>
                    <header className='flex py-4 justify-between flex-row items-center w-full'>
                        <h1 className='text-[#0E123F] font-bold text-[28px]'>Usuários</h1>
                        <div className='flex flex-1 justify-end gap-8'>
                            <Busca/>
                            <button className="px-16 py-3 font-bold bg-[#AE91E9] text-white items-center justify-center rounded-full flex gap-2 h-[75%] mt-1" onClick={handleOpenPopup}>                         
                                <img src='AddUser.svg' alt='a'/>
                                Adicionar Usuario
                            </button>
                            {showPopup && <PopupCadastro onClose={handleClosePopup} />}

                            <div>
                                
                            </div>


                        </div>
                    </header>
                               {/* a ser ajustado */}
                    <div className='w-full mt-8 h-[500px]'>
                        {/* <div className=''> */}
                            <CardUser/>
                        </div>
                        {/* </div> */}
                    </div>
                </div>

                {/* <div className='p-2 '>= */}
                     <SideBar />
                {/* </div> */}

            </div>
    );
}

