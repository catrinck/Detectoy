import React, { useState, useEffect } from 'react'
import { Link, useNavigate, useLocation } from "react-router-dom";
import SideBar from './components/SideBar';





export default function Relatorio() {
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

    const item = {
        posto : 1,
        defeito : "secagem",
        data : "00/00/00",
        horario : "00:00"
    }

    return (
        

        <div className='h-[720px]'>

            <div className='p-10 m-20 rounded-md bg-[#0E123F] h-full flex flex-1'>

                <div className='bg-white  justify-center rounded-md h-full w-[81.75rem] p-8'>
                    <header className='flex flex-1'>
                        <h1 className='text-[#0E123F] font-bold text-[28px]'>Cadastrar Setores</h1>

                    </header>

                    <table className="w-full mt-2 border border-black rounded text-center">
                        <thead>
                            <tr className="text-white bg-[#AE91E9] text-sm">
                                <th className="p-2 border border-black">Posto</th>
                                <th className="p-2 border border-black">Defeito</th>
                                <th className="p-2 border border-black">Data</th>
                                <th className="p-2 border border-black">Horário</th>
                            </tr>
                        </thead>
                        <tbody>
                            {item.length > 0 ? (
                                item.map((item, index) => (
                                    <tr className="border-t border-black text-xs">
                                        <td className="p-2 border border-black">{item.posto}</td>
                                        <td className="p-2 border border-black">{item.defeito}</td>
                                        <td className="p-2 border border-black">{item.data}</td>
                                        <td className="p-2 border flex items-center">
                                        </td>
                                        <td className="p-2 border border-blackf">{item.horario}</td>
                                    </tr>
                                ))
                            ) : (
                                <tr>
                                    <td colSpan="4" className="text-center p-2">Nenhuma infração encontrada</td>
                                </tr>
                            )}
                        </tbody>
                    </table>

                </div>




                <div className='p-2 m-2 '>=
                    <SideBar />

                </div>



            </div>
        </div>
    );
}

