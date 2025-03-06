import React, { useState, useEffect} from 'react'
import "./TelaInicial.css";
import { Link, useNavigate, useLocation} from "react-router-dom";

export default function ReportsPage() {
    const [selectedButton, setSelectedButton] = useState(null);
    const navigate = useNavigate();
    const location = useLocation();

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
                            Relatórios
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
                <div className="Padding2">
                    Dashboard
                    <form class="max-w-md mx-auto mt-2">
                        <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only">Buscar</label>
                        <div class="relative">
                            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                <svg class="w-4 h-4 text-[#0E123F]-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                                </svg>
                            </div>
                            <input type="search" id="default-search"
                                class="block w-[350px] p-3 ps-10 text-sm text-[#0E123F] border border-[#0E123F] 
                    rounded-[26px] bg-[#0E123F]-50 focus:ring-white focus:border-white placeholder:text-[#0E123F] placeholder:font-normal"
                                placeholder="Buscar" required />
                        </div>
                    </form>
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

