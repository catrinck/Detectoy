import React, { useEffect, useState } from "react";
import axios from "axios";
import Header from "./Header";
import {useNavigate} from "react-router-dom";

const GerenciarUsuarios = () => {
    const [usuarios, setUsuarios] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get("http://127.0.0.1:8000/api/usuarios/");
                setUsuarios(response.data);
            } catch (error) {
                console.error("Erro ao buscar produtos:", error);
            }
        };
        fetchProducts();
    }, []);


    const navigate = useNavigate();

    const editUsuario = (usuario_cpf) => {
        navigate(`/usuarios/${usuario_cpf}`);
    };

    const deleteProduct = async (usuario_cpf) => {
        try {
            await axios.delete(`http://127.0.0.1:8000/api/products/${usuario_cpf}`);
            alert(`Produto deletado com sucesso!`);
            setUsuarios(usuarios.filter((usuario) => usuario.cpf !== usuario_cpf));
        } catch (error) {
            console.error("Erro ao deletar produto:", error);
            alert("Falha ao deletar produto. Tente novamente.");
        }
    };

    return (
        <div>
            <Header />
            <div className="min-h-screen flex flex-col items-center gap-y-8 bg-blue-50">
                <h1 className="text-3xl font-bold my-6">Usuarios</h1>
                {usuarios.length > 0 ? (
                    <div className="min-w-635px">
                        {usuarios.map((usuario, index) => (
                            <div
                                className="grid items-start bg-gray-50 p-6 rounded-lg shadow-lg mb-3 grid-cols-3 grid-rows3 hover:bg-white hover:scale-105 transition duration-300 ease-in-out"
                                key={index}>
                                <div className="text-2xl font-bold mb-0 col-span-2 pr-30">
                                    {usuario.nome}
                                </div>
                                <div className="col-start-3 flex flex-row justify-end">
                                    <div
                                        className="bg-blue-500 text-white text-center px-3 py-1 rounded-lg hover:bg-blue-600 transition col-start-3 mx-1"
                                        onClick={() => editUsuario(usuario.cpf)}
                                    >
                                        Editar
                                    </div>
                                    <div
                                        className="bg-red-500 text-white text-center px-3 py-1 rounded-lg hover:bg-red-600 transition mx-1"
                                        onClick={() => deleteProduct(usuario.cpf)}
                                    >
                                        Excluir
                                    </div>
                                </div>
                                <div className="text-xl mb-1 col-span-2">
                                    <b>CPF: </b>{usuario.cpf}
                                </div>
                                <div className="text-xl mb-1 col-span-1">
                                    <b>Acesso às câmeras: </b>{usuario.cameras ? ("Sim") : ("Não")}
                                </div>
                                <div className="text-xl mb-1 col-span-2">
                                    <b>E-mail: </b>{usuario.email}
                                </div>
                                <div className="text-xl mb-1 col-span-1">
                                    <b>Acesso aos relatorios: </b>{usuario.relatorios ? ("Sim") : ("Não")}
                                </div>
                            </div>
                        ))
                        }
                        <div
                            className="justify-center w-fit bg-blue-500 text-white text-center px-3 py-1 rounded-lg hover:bg-blue-600 transition mx-1">
                            Cadastrar novo usuário
                        </div>
                    </div>

                ) : (
                    <div className="flex flex-col items-center">
                        <p className="text-center text-gray-500">Nenhum usuário cadastrado.</p>
                        <p><a href="/criar-usuario" className="text-center text-sky-500">Cadastrar um usuário</a></p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default GerenciarUsuarios;
