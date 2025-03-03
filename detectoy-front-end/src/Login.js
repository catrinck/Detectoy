import React, { useState } from 'react';  // ✅ Importa useState
import { Link } from "react-router-dom";
import "./Login.css";

const Login = () => {
    const [showPassword, setShowPassword] = useState(false);

    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    return (
        <div className="container">
            <form className="forms">
                <h1>Login</h1>
                
                <div className="input-box">
                    <input placeholder="Email" type="email" />
                </div>

                <div className="input-box">
                    <input 
                        placeholder="Senha" 
                        type={showPassword ? "text" : "password"}
                    />
                    <i 
                        className={`bi ${showPassword ? "bi-eye-slash" : "bi-eye"}`}
                        id="btn-senha" 
                        onClick={togglePasswordVisibility}
                        style={{ cursor: "pointer" }} 
                    ></i>
                </div>

                <div className="remember-forgot">
                    <label>
                        <input type="checkbox" />
                        Manter-me conectado
                    </label>
                    <a href="#">Esqueci minha senha</a>
                </div>

                <button type="submit" className="bg-blue-500 text-white px-6 py-2 rounded-full hover:bg-blue-600 transition">
                    Entrar
                </button>
            </form>
        </div>
    );
};

export default Login;
