import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Login.css";

const Login = () => {
    const [cpf, setCpf] = useState("");
    const [senha, setSenha] = useState("");
    const [showPassword, setShowPassword] = useState(false);
    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate(); // Hook para redirecionamento

    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    const handleCpfChange = (e) => {
        setCpf(e.target.value);
    };

    const handleSenhaChange = (e) => {
        setSenha(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault(); // Evita recarregar a página
        setError("");
        setIsLoading(true);

        const loginData = {
            email: cpf, // Usando cpf como email por enquanto
            senha: senha
        };

        try {
            // URL corrigida para apontar para a porta 8080 e caminho correto da API
            const response = await axios.post("http://localhost:8080/api/v1/login/gerentes/", loginData);

            if (response.status === 200) {
                // Se o login for bem-sucedido, salva o token JWT
                localStorage.setItem("token", response.data.access_token);
                localStorage.setItem("userData", JSON.stringify(response.data.user_data));
                navigate("/tela-inicial"); // Redireciona para a tela inicial
            }
        } catch (error) {
            // Se a requisição falhar, define uma mensagem de erro
            if (error.response) {
                if (error.response.status === 400 || error.response.status === 401) {
                    setError("CPF ou senha incorretos. Tente novamente.");
                } else if (error.response.status === 500) {
                    setError("Erro no servidor. Verifique se o servidor backend está em execução.");
                } else {
                    setError(`Erro no servidor (${error.response.status}). Tente mais tarde.`);
                }
            } else if (error.request) {
                setError("Não foi possível conectar ao servidor. Verifique sua conexão.");
            } else {
                setError("Erro ao processar a requisição. Tente novamente.");
            }
        } finally {
            setIsLoading(false);
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
                            placeholder="CPF ou Email" 
                            type="text" 
                            value={cpf}
                            onChange={handleCpfChange}
                            disabled={isLoading}
                        />
                    </div>

                    <div className="input-box">
                        <input
                            placeholder="Senha"
                            type={showPassword ? "text" : "password"}
                            value={senha}
                            onChange={handleSenhaChange}
                            disabled={isLoading}
                        />
                        <i
                            className={`bi ${showPassword ? "bi-eye-slash" : "bi-eye"}`}
                            id="btn-senha"
                            onClick={togglePasswordVisibility}
                            style={{ cursor: "pointer" }}
                        ></i>
                    </div>

                    <button 
                        type="submit" 
                        className="bg-blue-500 text-white px-6 py-2 rounded-full hover:bg-blue-600 transition"
                        disabled={isLoading}
                    >
                        {isLoading ? "Entrando..." : "Entrar"}
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Login;
