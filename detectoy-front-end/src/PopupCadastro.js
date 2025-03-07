// PopupCadastro.js
import React, { useState } from 'react';
import './TelaInicial.css';

function PopupCadastro({ onClose }) {

    const [administradorChecked, setAdministradorChecked] = useState(false);
    const [supervisorChecked, setSupervisorChecked] = useState(false);

    return (
        <div className="popup-overlay">
            <div className="popup-content">
                <h2>Adicionar usuário</h2>
                <form>
                    <input type="text" placeholder="Nome" className="cadastro-input" />
                    <input type="email" placeholder="Email" className="cadastro-input" />
                    <input type="password" placeholder="Senha" className="cadastro-input" />
                    <div className="checkboxPermissions">
                        <input
                            type="checkbox"
                            id="administrador"
                            checked={administradorChecked}
                            onChange={() => {
                                setAdministradorChecked(true);
                                setSupervisorChecked(false);
                            }}
                        />
                        <label htmlFor="administrador">Administrador</label>
                        <input
                            type="checkbox"
                            id="supervisor" checked={supervisorChecked}
                            onChange={() => {
                                setSupervisorChecked(true);
                                setAdministradorChecked(false);
                            }} />
                            
                        <label htmlFor="supervisor">Supervisor</label>
                    </div>
                    <button type="submit" className="btnCadastroUser">Cadastrar</button>
                </form>
                <button className="close-button" onClick={onClose}>Fechar</button>
            </div>
        </div>
    );
}

export default PopupCadastro;