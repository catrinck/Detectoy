import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./Home"
import CriarUsuario from "./CriarUsuario";
import GerenciarUsuarios from "./GerenciarUsuarios";
import EditarUsuario from "./EditarUsuario";


function App() {
  return (
      <Router>
          <Routes>
              <Route path="/" element={<Home />}/>
              <Route path="/criar-usuario" element={<CriarUsuario />} />
              <Route path="/usuarios" element={<GerenciarUsuarios />} />
              <Route path="/usuarios/:cpf_usuario" element={<EditarUsuario />} />
          </Routes>
      </Router>
  );
}

export default App;
