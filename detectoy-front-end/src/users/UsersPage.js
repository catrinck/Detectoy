import React, { useState, useEffect } from 'react'
import "../home-page/TelaInicial.css";
import { Link, useNavigate, useLocation } from "react-router-dom";
import PopupCadastro from '../PopupCadastro';
import Busca from '../components/Busca';
import CardSetor from '../components/CardSetor';

export default function UserPage() {
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
        <div className="Container">
            <div className="Padding">
                <div className="ContainerUser flex flex-col items-end absolute top-[3vh] right-[3vh]">
                    <div className="bg-[#090A1C] rounded-lg shadow-md p-4 text-white w-[240px] h-[70px] flex items-center justify-center mb-12 mt-10">
                        Bem vindo, Nome Sobrenome
                    </div>
                    <div className="flex flex-col space-y-4">
                        <button
                            className={`w-[240px] py-2 px-4 font-bold rounded transition-all
                ${selectedButton === "tela-inicial"
                                    ? "bg-[#AE91E9] text-white"
                                    : "bg-white text-[#0E123F] hover:bg-[#AE91E9] hover:text-white"
                                }`}
                            onClick={() =>
                                navigate("/tela-inicial") //navega para dashboard
                            }
                        >
                            Dashboard
                        </button>
                        <button
                            className={`w-[240px] py-2 px-4 font-bold rounded transition-all
                ${selectedButton === "reports"
                                    ? "bg-[#AE91E9] text-white"
                                    : "bg-white text-[#0E123F] hover:bg-[#AE91E9] hover:text-white"
                                }`}
                            onClick={() =>
                                navigate("/reports") //navega para reports
                            }
                        >
                            Setores
                        </button>
                        <button
                            className={`w-[240px] py-2 px-4 font-bold rounded transition-all
                ${selectedButton === "users"
                                    ? "bg-[#AE91E9] text-white"
                                    : "bg-white text-[#0E123F] hover:bg-[#AE91E9] hover:text-white"
                                }`}
                            onClick={() =>
                                navigate("/users") //navega para users
                            }
                        >
                            Usuários
                        </button>
                    </div>
                </div>
                <div className="Padding2 gap-20">
                    Usuários
                    <div className='flex justify-end'>
                        {/* PESQUISA */}
                        <Busca />

                        <button className="btnAddUser" onClick={handleOpenPopup}>
                            Adicionar usuário
                            <i class="bi bi-person-add"></i>
                        </button>
                        {showPopup && <PopupCadastro onClose={handleClosePopup} />}
                        
                            
                    </div>

                    

                </div>
                <Link to="/Home">
                    <button className="hover:text-white absolute bottom-4 right-4 bg-white hover:bg-[#AE91E9] text-[#0E123F] font-bold py-2 px-4 rounded flex items-center gap-2">
                        Voltar
                    </button>
                </Link>
            </div>
        </div>
    );
}

