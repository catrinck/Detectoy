import React, { useState } from 'react'


export default function HistoricoInfracoes() {
    const item = {
        posto : 1,
        defeito : "secagem",
        data : "00/00/00",
        horario : "00:00"
    }
   
    return (
    
    <div className="text-black p-4 rounded-lg">
      <div className="flex justify-between items-center">
        <h2 className="text-lg font-bold text-darkBlue flex items-center gap-2">
        <img src="notifications-icon.svg" alt="historico" className="w-6 h-6"/> Histórico de Infrações
        </h2>

        
      </div>

      <table className="w-full mt-2 border border-black rounded text-center">
        <thead>
          <tr className="text-white bg-[#AE91E9] text-sm">
            <th className="p-2 border border-black">Posto</th>
            <th className="p-2 border border-black">Defeito</th>
            <th className="p-2 border border-black">Data</th>
            <th className="p-2 border border-black">Horário</th>
          </tr>
        </thead>
        <tbody>
          {item.length > 0 ? (
            item.map((item, index) => (
              <tr className="border-t border-black text-xs">
                <td className="p-2 border border-black">{item.posto}</td>
                <td className="p-2 border border-black">{item.defeito}</td>
                <td className="p-2 border border-black">{item.data}</td>
                <td className="p-2 border flex items-center">
                </td>
                <td className="p-2 border border-blackf">{item.horario}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4" className="text-center p-2">Nenhuma infração encontrada</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  )
}
