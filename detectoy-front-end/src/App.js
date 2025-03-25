import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./Home"
import CriarUsuario from "./users/CriarUsuario";
import GerenciarUsuarios from "./users/GerenciarUsuarios";
import EditarUsuario from "./users/EditarUsuario";
import TelaInicial from "./home-page/TelaInicial";
import Login from "./login/Login";
import UsersPage from "./users/UsersPage";
import ReportsPage from "./ReportsPage";
import PopupCadastro from "./PopupCadastro";
import CadastrarSetor from "./CadastrarSetor";


function App() {
  return (
      <Router>
          <Routes>
              <Route path="/" element={<Home />}/>
              <Route path="/criar-usuario" element={<CriarUsuario />} />
              <Route path="/usuarios" element={<GerenciarUsuarios />} />
              <Route path="/usuarios/:cpf_usuario" element={<EditarUsuario />} />
              <Route path="/tela-inicial" element={<TelaInicial />} />
              <Route path="/Home" element ={<Home />} />
              <Route path="/login" element ={<Login />} />
              <Route path="/users" element ={<UsersPage />} />
              <Route path="/reports" element ={<ReportsPage />} />
              <Route path="/popup-cadastro" element ={<PopupCadastro />} />
              <Route path="/CadastrarSetor" element={<CadastrarSetor/>}></Route>
          </Routes>
      </Router>
  );
}

export default App;
