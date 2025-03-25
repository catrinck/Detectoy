import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Login.css";

const Login = () => {
    const [cpf, setCpf] = useState("");
    const [senha, setSenha] = useState("");
    const [showPassword, setShowPassword] = useState(false);
    const [error, setError] = useState("");
    const navigate = useNavigate(); // Hook para redirecionamento

    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    const handleSubmit = async (e) => {
        e.preventDefault(); // Evita recarregar a página

        const loginData = {
            cpf: cpf,
            senha: senha
        };

        try {
            const response = await axios.post("http://localhost:8000/api/login/gerentes/", loginData);

            if (response.status === 200) {
                // Se o login for bem-sucedido, pode salvar um token JWT se houver
                localStorage.setItem("token", response.data.token);
                navigate("/tela-inicial"); // Redireciona para a tela inicial
            }
        } catch (error) {
            // Se a requisição falhar, define uma mensagem de erro
            if (error.response) {
                if (error.response.status === 400 || error.response.status === 401) {
                    setError("CPF ou senha incorretos. Tente novamente.");
                } else {
                    setError("Erro no servidor. Tente mais tarde.");
                }
            } else {
                setError("Erro ao conectar com o servidor.");
            }
        }
    };

    return (
        <div className="login-page">
            <div className="container">
                <form className="forms" onSubmit={handleSubmit}>
                    <h1>Login</h1>

                    {error && <p className="error">{error}</p>} {/* Exibe erro */}

                    <div className="input-box">
                        <input 
                            placeholder="CPF" 
                            type="text" 
                            value={cpf}
                            onChange={(e) => setCpf(e.target.value)}
                        />
                    </div>

                    <div className="input-box">
                        <input
                            placeholder="Senha"
                            type={showPassword ? "text" : "password"}
                            value={senha}
                            onChange={(e) => setSenha(e.target.value)}
                        />
                        <i
                            className={`bi ${showPassword ? "bi-eye-slash" : "bi-eye"}`}
                            id="btn-senha"
                            onClick={togglePasswordVisibility}
                            style={{ cursor: "pointer" }}
                        ></i>
                    </div>

                    <button type="submit" className="bg-blue-500 text-white px-6 py-2 rounded-full hover:bg-blue-600 transition">
                        Entrar
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Login;
