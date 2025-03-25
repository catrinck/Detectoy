import React, { useState } from "react";
import { Edit2Icon, EyeIcon, TrashIcon } from "lucide-react";
{/*import Delete from "./Delete";
import Edicao from "./Edicao";*/}

export default function CardSetor({
  camera,
  dataInst,
  nome,
  onShowEquipament,
  disabled,
  }) {

  const [visibleDelete, setVisibleDelete] = useState(false)
  const [visibleEdit, setVisibleEdit] = useState(false)



  return (
    <>
      <div className="overflow-hidden bg-[#F6F6F6] rounded-xl  h-28 shadow-md w-full flex">
        <div className="bg-[#AE91E9] shrink-0 w-4" />
        <div className="flex flex-row w-full p-2 relative">
          <div className="flex flex-col justify-between">

            <div className="gap-2 items-center">
              {/* Nome do equipamento */}
              <h2 className="font-semibold text-base">{nome}</h2>

              <p className="text-[#5C5C5C] font-light text-xs opacity-70">Câmera {camera}</p>

            </div>
           

            <div className="flex mb-2 flex-row gap-x-4 items-center">
              {/*Total de infrações do equipamento */}
              <p className="font-semibold whitespace-nowrap text-xs opacity-70">
                Total de Ocorrências: 120
              </p>

            </div>
          </div>

          <div className="right-1.5 top-1.5 absolute flex flex-col gap-1.5">

            {/* Botões de edição */}
            <button
              disabled={disabled}
              onClick={() => setVisibleEdit(true)}
              className="flex h-4 w-4 items-center justify-center opacity-60 border-black rounded-sm border p-[1px] hover:bg-yellow-300"
            >
              <Edit2Icon className="fill-black" />
            </button>

            {/* Botão de visualizar Equipamento */}
            <button
              onClick={onShowEquipament}
              disabled={disabled}
              className="flex h-4 w-4 items-center justify-center opacity-60 border-black rounded-sm border p-[1px] hover:bg-blue-300"
            >
              <EyeIcon className="fill-black text-white" />
            </button>

            {/* Botão de deletar Equipamento */}
            <button
              disabled={disabled}
              className="flex h-4 w-4 items-center justify-center opacity-60 border-black rounded-sm border p-[1px] hover:bg-red-300"
              onClick={() => setVisibleDelete(true)}
            >
              <TrashIcon className="fill-black" />
            </button>

          </div>
        </div>
      </div>


</>
  );
}