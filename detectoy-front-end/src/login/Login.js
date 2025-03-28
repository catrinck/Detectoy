import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Login.css";
import logo from "../image/logo010.svg"
import logo2 from "../image/logoEye.svg"


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
            const response = await axios.get("http://127.0.0.1:8080/api/v1/gerentes", loginData);

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
            <img className="absolute bottom-12 left-8" src={logo2} alt=""/>
            <div className="container">
            <img className="mx-auto mt-24 mb-28" src={logo} alt=""></img>
                <form className="forms" onSubmit={handleSubmit}>
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

                    <button type="submit" className="bg-[#AE91E9] text-white px-6 py-2 rounded-full hover:bg-[#836db0] transition mt-12">
                        Entrar
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Login;
