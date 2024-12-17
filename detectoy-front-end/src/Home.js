import React from "react";
import { Link } from "react-router-dom";
import Header from "./Header";

const Home = () => {
    return (
        <div>
            <Header />
            <div className="h-screen flex flex-col justify-center items-center gap-y-8 bg-blue-50">
                <h1 className="text-4xl font-bold mb-3">Boas-vindas ao Sistema</h1>
                <div>
                    <Link
                        to="/usuarios"
                        className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600 transition"
                    >
                        Gerenciar usuários
                    </Link>
                </div>
                <div>
                    <Link
                        to="/criar-usuario"
                        className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600 transition"
                    >
                        Criar um novo usuário
                    </Link>
                </div>

            </div>
        </div>

    );
};

export default Home;
