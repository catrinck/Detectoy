import React, { useState, useEffect } from 'react'
import "./TelaInicial.css";
import { Link, useNavigate, useLocation } from "react-router-dom";
import GerarRelatorio from './components/GerarRelatorio';
import HistoricoInfracoes from './components/HistoricoInfracoes';
import InfracoesSetor from './components/InfracoesSetor';


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

        <div className="flex-1 p-10 overflow-y-auto bg-white rounded-md mr-[16.5rem] mt-[2rem] mb-[2rem] ml-[2rem]">

          <h2 className="text-2xl font-bold mb-6">Dashboard & Relatórios</h2>

          <div className="grid grid-cols-2 gap-3">
            <div className="space-y-2">
              {/* Infrações por Setor */}
              <InfracoesSetor />

              {/* Gerar Relatório */}
              <GerarRelatorio />
            </div>

            {/* Histórico de Infrações */}
            <HistoricoInfracoes />
          </div>
        </div>

        
      </div>
    </div>
  );
}

