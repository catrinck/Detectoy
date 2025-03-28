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
import ProtectedRoute from "./ProtectedRoute";
import CameraStream from './components/CameraStream';

function App() {
    return (
        <Router>
            <Routes>
                {/* página de login sem proteção */}
                <Route path="/login" element={<Login />} />

                <Route element={<ProtectedRoute/>}>
                    <Route path="/" element={<Login />} />
                    <Route path="/criar-usuario" element={<CriarUsuario />} />
                    <Route path="/usuarios" element={<GerenciarUsuarios />} />
                    <Route path="/usuarios/:cpf_usuario" element={<EditarUsuario />} />
                    <Route path="/tela-inicial" element={<TelaInicial />} />
                    <Route path="/Home" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/users" element={<UsersPage />} />
                    <Route path="/reports" element={<ReportsPage />} />
                    <Route path="/popup-cadastro" element={<PopupCadastro />} />
                    <Route path="/CadastrarSetor" element={<CadastrarSetor />}></Route>
                    <Route path="/camera-stream" element={<CameraStream />} />
                </Route>
            </Routes> 
        </Router>
    );
}

export default App;
