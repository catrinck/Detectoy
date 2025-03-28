import React, { useState, useEffect } from 'react'
import "./TelaInicial.css";
import { Link, useNavigate, useLocation } from "react-router-dom";
import GerarRelatorio from '../components/GerarRelatorio';
import HistoricoInfracoes from '../components/HistoricoInfracoes';
import InfracoesSetor from '../components/InfracoesSetor';
import axios from 'axios';
import Sidebar from '../components/SideBar';

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
    <div className="bg-[#D0D6E2] h-screen flex items-center justify-center w-screen">
      {/* <div className="Padding"> */}
        <div className="p-10 w-[80%] rounded-md bg-[#0E123F] h-[80%] flex justify-between gap-6 ">
          
          
        {/* </div> */}

        <div className="p-10 w-full overflow-y-auto bg-white rounded-md">

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
        {/* <div className="h-full"> */}
           <Sidebar/>
          {/* </div> */}

      </div>
    </div>
  );
}

