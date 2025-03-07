import React, { useState, useEffect } from "react";
import "./TelaInicial.css";
import { Link, useNavigate, useLocation } from "react-router-dom";

export default function TelaInicial() {
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
    <div className="Container bg-[#E5E7EB] min-h-screen flex justify-between">
      
      {/* Conteúdo Principal */}
      <div className="flex-1 p-10">
        <h2 className="text-2xl font-bold mb-6">Dashboard & Relatórios</h2>

        {/* Infrações por Setor */}
        <div className="mb-8">
          <h3 className="text-lg font-semibold mb-4 bg-[#0E123F] text-white rounded w-[400px] h-[50px] flex items-center justify-center text-white">Infrações por Setor</h3>
          <div className="grid grid-cols-3 gap-6">
            {Array(6)
              .fill("")
              .map((_, index) => (
                <div key={index} className="bg-white p-4 rounded-lg shadow-md text-center">
                  <p>Nome Setor</p>
                  <p className="text-2xl font-bold">50</p>
                </div>
              ))}
          </div>
        </div>

        {/* Gerar Relatório */}
        <div className="mb-8">
          <h3 className="text-lg font-semibold mb-4 bg-[#0E123F] text-white rounded w-[400px] h-[50px] flex items-center justify-center text-white">Gerar Relatório</h3>
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2">
              <input type="checkbox" id="setor" />
              <label htmlFor="setor">Por Setor</label>
            </div>
            <div className="flex items-center gap-2">
              <input type="checkbox" id="defeito" />
              <label htmlFor="defeito">Por Defeito</label>
            </div>
            <div className="flex items-center gap-2">
              <input type="checkbox" id="tempo" />
              <label htmlFor="tempo">Por Tempo</label>
            </div>
            <button className="bg-[#AE91E9] text-white py-2 px-4 rounded">
              Gerar
            </button>
          </div>
        </div>

        {/* Histórico de Infrações */}
        <div>
          <h3 className="text-lg font-semibold mb-4 bg-[#0E123F] text-white rounded w-[400px] h-[50px] flex items-center justify-center text-white ">Histórico de Infrações</h3>
          <div className="bg-white p-4 rounded-lg shadow-md">
            <table className="w-full">
              <thead>
                <tr>
                  <th className="text-left">Posto</th>
                  <th className="text-left">Defeito</th>
                  <th className="text-left">Data</th>
                  <th className="text-left">Horário</th>
                </tr>
              </thead>
              <tbody>
                {Array(10)
                  .fill("")
                  .map((_, index) => (
                    <tr key={index} className="border-b">
                      <td>#001</td>
                      <td>Máquina de Soldagem</td>
                      <td>16/03/25</td>
                      <td>8:03 H</td>
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* Painel Lateral Direito (Quadrado Roxo) */}
      <div className="w-[400px] h-[900px] bg-[#0E123F] p-8 text-white rounded-lg flex flex-col justify-between items-center">
        <div className="text-center mb-10 bg-[#0E123F">
          <div className="bg-[#090A1C] rounded-lg p-4">
            Bem vindo, <strong>Nome Sobrenome</strong>
          </div>
        </div>
        <nav className="flex flex-col space-y-4 w-full">
          <button
            className={`w-full py-2 px-4 rounded ${selectedButton === "tela-inicial" ? "bg-[#AE91E9] text-[white]" : "hover:bg-[#AE91E9] hover:text-[white]"}`}
            onClick={() => navigate("/tela-inicial")}
          >
            Dashboard & Relatórios
          </button>
          <button
            className={`w-full py-2 px-4 rounded bg-[white] text-[#0E123F] ${selectedButton === "users" ? "bg-bg-[white] text-[#0E123F]" : "hover:bg-[#AE91E9] hover:text-[white]"}`}
            onClick={() => navigate("/users")}
          >
            Usuários
          </button>
        </nav>

        <Link to="/Home">
          <button className="bg-white hover:bg-[#0E123F] hover:text-white text-[#0E123F] font-bold py-2 px-4 rounded w-full bottom-4">
            Voltar
          </button>
        </Link>
      </div>
    </div>
  );
}
