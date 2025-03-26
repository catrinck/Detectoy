import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Edit2Icon, EyeIcon, TrashIcon } from "lucide-react";


const CardUser = ({ usuario, onShowEquipament, deleteUser }) => {
    const { cpf, nome, log, cameras, relatorios } = usuario;
    const role = log && cameras && relatorios ? "Administrador" : "Supervisor";

    return (
        <div className="overflow-hidden bg-[#F6F6F6] rounded-xl h-28 shadow-md w-full flex">
            <div className="bg-[#AE91E9] shrink-0 w-4" />
            <div className="flex flex-row w-full p-2 relative">
                <div className="flex flex-col justify-between mt-2">
                    <h2 className="font-semibold text-base">{nome}</h2>
                    <p className="text-[#5C5C5C] font-bold ml-2">Permissões: {role}</p>
                </div>
                <div className="right-1.5 top-1.5 absolute flex flex-col gap-1.5 mt-4">
                    <button
                        className="flex h-4 w-4 items-center justify-center opacity-60 border-black rounded-sm border p-[1px] hover:bg-yellow-300"
                        onClick={() => onShowEquipament(cpf)}
                    >
                        <Edit2Icon className="fill-black" />
                    </button>
                    <button
                        className="flex h-4 w-4 items-center justify-center opacity-60 border-black rounded-sm border p-[1px] hover:bg-red-300"
                        onClick={() => deleteUser(cpf)}
                    >
                        <TrashIcon className="fill-black" />
                    </button>
                </div>
            </div>
        </div>
    );
};

const GerenciarUsuarios = () => {
    const [usuarios, setUsuarios] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchUsuarios = async () => {
            try {
                const response = await axios.get("http://127.0.0.1:8000/api/funcionarios/");
                setUsuarios(response.data);
            } catch (error) {
                console.error("Erro ao buscar usuários:", error);
            }
        };
        fetchUsuarios();
    }, []);

    const editUsuario = (cpf) => {
        navigate(`/usuarios/${cpf}`);
    };

    const deleteUser = async (cpf) => {
        try {
            await axios.delete(`http://127.0.0.1:8000/api/funcionarios/${cpf}`);
            setUsuarios(usuarios.filter((usuario) => usuario.cpf !== cpf));
        } catch (error) {
            console.error("Erro ao deletar usuário:", error);
            alert("Falha ao deletar usuário. Tente novamente.");
        }
    };

    return (
        <div className="">
            {usuarios.length > 0 ? (
                <div className="min-w-635px item-start grid grid-cols-3 gap-4 overflow-auto h-[500px] ">
                    {usuarios.map((usuario) => (

                        <>
                            <CardUser
                                key={usuario.cpf}
                                usuario={usuario}
                                onShowEquipament={editUsuario}
                                deleteUser={deleteUser}

                            />
                           
                        </>
                    ))}
                </div>
            ) : (
                <p className="text-center text-gray-500">Nenhum usuário cadastrado.</p>
            )}
        </div>
    );
};

export default GerenciarUsuarios;
