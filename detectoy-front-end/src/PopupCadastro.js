// PopupCadastro.js
import React, { useState } from 'react';
import axios from "axios";
import './home-page/TelaInicial.css';

function PopupCadastro({ onClose }) {

    const [administradorChecked, setAdministradorChecked] = useState(false);
    const [supervisorChecked, setSupervisorChecked] = useState(false);

    const [usuario, setUsuario] = useState({
        cpf: "",
        nome: "",
        email: "",
        senha: "",
        log: false,
        cameras: false,
        relatorios: false,

    });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setUsuario((prevState) => ({
            ...prevState,
            [name]: value,
        }));
    };

    const handleAdministradorChange = () => {
        setAdministradorChecked(true);
        setSupervisorChecked(false);
        setUsuario({
            ...usuario,
            log: true,
            cameras: true,
            relatorios: true,
        });
    };

    const handleSupervisorChange = () => {
        setSupervisorChecked(true);
        setAdministradorChecked(false);
        setUsuario({
            ...usuario,
            log: false,
            cameras: false,
            relatorios: false,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:8000/api/funcionarios/", usuario);
            alert(response.status + " - Usuário criado: " + usuario.nome);
        } catch (error) {
            alert("Erro ao criar o usuário: " + error.message);
        }
    };

    return (
        <div className="popup-overlay">
            <div className="popup-content">
                <h2>Adicionar usuário</h2>
                <form>
                    <input
                        type="text"
                        placeholder="Nome"
                        name="nome"
                        value={usuario.nome}
                        onChange={handleInputChange}
                        className="cadastro-input"
                    />
                    <input
                        type="text"
                        placeholder="CPF"
                        name="cpf"
                        value={usuario.cpf}
                        onChange={handleInputChange}
                        className="cadastro-input"
                    />
                    <input
                        type="email"
                        placeholder="Email"
                        name="email"
                        value={usuario.email}
                        onChange={handleInputChange}
                        className="cadastro-input"
                    />
                    <input
                        type="password"
                        placeholder="Senha"
                        name="senha"
                        value={usuario.senha}
                        onChange={handleInputChange}
                        className="cadastro-input"
                    />
                    <div className="checkboxPermissions">
                        <input
                            type="checkbox"
                            id="administrador"
                            checked={administradorChecked}
                            onChange={handleAdministradorChange}
                        />
                        <label htmlFor="administrador">Administrador</label>
                        <input
                            type="checkbox"
                            id="supervisor" checked={supervisorChecked}
                            onChange={handleSupervisorChange} 
                        />
                            
                        <label htmlFor="supervisor">Supervisor</label>
                    </div>
                    <button type="submit" onClick={handleSubmit} className="btnCadastroUser">Cadastrar</button>
                </form>
                <button className="close-button" onClick={onClose}>Fechar</button>
            </div>
        </div>
    );
}

export default PopupCadastro;