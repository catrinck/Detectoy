import React, {useState} from "react";
import axios from "axios";
import Header from "../Header";


const CriarUsuario = () => {
    const [usuario, setUsuario] = useState({
        cpf: "",
        nome: "",
        email: "",
        senha: "",
        log: false,
        cameras: false,
        relatorios: false,

    });

    const handleChange = (e) => {
        const { name, type, checked, value } = e.target;

        // Check if the input is a checkbox
        const newValue = type === "checkbox" ? checked : value;

        setUsuario((prevUsuario) => ({
            ...prevUsuario,
            [name]: newValue,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://localhost:8080/api/v1/gerentes/", usuario);
            alert(response.status + " - Usuário criado: " + usuario.nome);
        } catch (error) {
            alert("Erro ao criar o usuário: " + error.message);
        }
    };

    return (
        <div>
            <Header/>
            <div className="min-h-screen flex items-center justify-center bg-blue-50">
                <div className="bg-white p-8 rounded-lg shadow-lg max-w-md w-full">
                    <h1 className="text-2xl font-bold mb-6">Criar novo usuário</h1>
                    <form onSubmit={handleSubmit} className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium">CPF:</label>
                            <input
                                type="text"
                                name="cpf"
                                value={usuario.cpf}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border rounded-lg"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium">Nome:</label>
                            <input
                                type="text"
                                name="nome"
                                value={usuario.nome}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border rounded-lg"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium">E-mail:</label>
                            <input
                                type="email"
                                name="email"
                                value={usuario.email}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border rounded-lg"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium">Senha:</label>
                            <input
                                type="password"
                                name="senha"
                                value={usuario.senha}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border rounded-lg"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium">Terá acesso aos comandos das câmeras?</label>
                            <input
                                type="checkbox"
                                name="cameras"
                                checked={usuario.cameras}
                                onChange={handleChange}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium">Terá acesso aos logs?</label>
                            <input
                                type="checkbox"
                                name="log"
                                checked={usuario.log}
                                onChange={handleChange}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium">Terá acesso aos comandos dos
                                relatórios?</label>
                            <input
                                type="checkbox"
                                name="relatorios"
                                checked={usuario.relatorios}
                                onChange={handleChange}
                            />
                        </div>
                        <button
                            type="submit"
                            onClick={handleSubmit}
                            className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
                        >
                            Criar Usuário
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default CriarUsuario;
