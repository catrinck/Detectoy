import React, { useState } from 'react';
import axios from "axios";
import './home-page/TelaInicial.css';

function PopupCadastro({ onClose }) {

    const [administradorChecked, setAdministradorChecked] = useState(false);
    const [supervisorChecked, setSupervisorChecked] = useState(false);

    return (
        <div className="popup-overlay">
            {/* Só mostra o formulário se o pop-up de sucesso NÃO estiver visível */}
            {!showSuccessPopup && (
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
                                id="supervisor" 
                                checked={supervisorChecked}
                                onChange={handleSupervisorChange} 
                            />
                            <label htmlFor="supervisor">Supervisor</label>
                        </div>
                        {errorMessage && <p className="error-message">{errorMessage}</p>}
                        <button type="submit" onClick={handleSubmit} className="btnCadastroUser">Cadastrar</button>
                    </form>
                    <button className="close-button" onClick={onClose}>Fechar</button>
                </div>
            )}

            {/* Pop-up de sucesso aparece e esconde o outro */}
            {showSuccessPopup && (
                <div className="success-popup">
                    <div className="success-content">
                        <h3>Usuário Cadastrado!</h3>
                        <button onClick={() => { setShowSuccessPopup(false); onClose(); }}>
                            Voltar à Usuários
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}

export default PopupCadastro;
