import React from 'react'
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { jwtDecode } from "jwt-decode";

export default function SideBar() {
    const [selectedButton, setSelectedButton] = useState(null);
    const navigate = useNavigate();
    const location = useLocation();
    const [userName, setUserName] = useState("Usuário");


    useEffect(() => {
        // Pega o token do localStorage
        const token = localStorage.getItem("token");

        if (token) {
            try {
                // Decodifica o token para obter o nome do usuário
                const decodedToken = jwtDecode(token);
                setUserName(decodedToken.nome || "Usuário");
            } catch (error) {
                console.error("Erro ao decodificar token:", error);
            }
        }
    }, []);

    const handleLogout = () => {
        localStorage.removeItem("token"); // Remove o token JWT
        navigate("/"); // Redireciona para a página de login
    };

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
        <div className="flex flex-col space-y-4 ">
            
            <div className="bg-[#090A1C] rounded-lg shadow-md p-4 text-white w-[240px] h-[70px] flex items-center justify-center mb-12 mt-10">
                Bem vindo,&nbsp;
                <div className="font-bold">
                    {userName}
                </div>
            </div>

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

            <button
                className={`w-[240px] py-2 px-4 font-bold rounded transition-all
                ${selectedButton === "Relatorio"
                        ? "bg-[#AE91E9] text-white"
                        : "bg-white text-[#0E123F] hover:bg-[#AE91E9] hover:text-white"
                    }`}
                onClick={() =>
                    navigate("/Relatorio") //navega para users
                }
            >
                Relatório
            </button>

            <Link to="/Login">
                <button className="hover:text-white bg-white hover:bg-[#AE91E9] text-[#0E123F] font-bold py-2 px-4 rounded flex items-center gap-2 "
                    onClick={handleLogout}>
                    Logout
                </button>
            </Link>

        </div>


    )
}
