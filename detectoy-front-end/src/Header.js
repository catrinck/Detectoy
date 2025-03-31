import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
    return (
        <header className="header">
            <div className="flex justify-left bg-blue-50">
                <div className="flex justify-center">
                    <Link
                        to="/"
                        className="bg-blue-50 text-black px-6 py-3 hover:bg-blue-600 hover:text-white transition"
                    >
                        Início
                    </Link>
                </div>
                <div className="flex justify-center">
                    <Link
                        to="/usuarios"
                        className="bg-blue-50 text-black px-6 py-3 hover:bg-blue-600 hover:text-white transition"
                    >
                        Gerenciar Usuários
                    </Link>
                </div>
                <div className="flex justify-center">
                    <Link
                        to="/criar-usuario"
                        className="bg-blue-50 text-black px-6 py-3 hover:bg-blue-600 hover:text-white transition"
                    >
                        Cadastrar Usuário
                    </Link>
                </div>
            </div>
        </header>
    );
};

export default Header;
