import React, { useEffect, useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Edit2Icon, EyeIcon, TrashIcon } from "lucide-react";


const CardUser = ({ usuario, onShowEquipament, deleteUser }) => {
    const { cpf, nome, log, cameras, relatorios } = usuario;
    const role = log && cameras && relatorios ? "Administrador" : "Supervisor";

    return (
        <>
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


        </>
    );
};

export default GerenciarUsuarios;

