import React from 'react'
import CustomSelect from './ui/CustomSelect'

export default function InfracoesSetor() {
    const setor = {
        time:1,
        name:"",
        infractions:1
    }
        
    
    return (
    <div className="text-black p-4 rounded-lg">
    <div className="flex justify-between items-center">
      <h2 className="text-lg font-bold mb-4 text-darkBlue flex items-center gap-2">
        <img src='./equipament-icon.svg' className="w-6 h-6" alt="Setor"/> Infrações por Setor
      </h2>
      <CustomSelect
        
        options={[
          { value: "monthly", label: "Mensal" },
          { value: "annual", label: "Anual" },
        ]}
      />
    </div>
    <div className="grid grid-cols-4 gap-3 border border-black rounded-lg p-4">
      {Array.isArray(setor) && setor.length > 0 ? (
        setor.map((setor, index) => (
          <div key={index} className="relative bg-gray-100 rounded-lg shadow-lg p-2 h-15 flex items-center space-x-3">
            <div className="absolute left-0 top-0 h-full w-5 bg-blue-600 rounded-l-lg"></div>
            <div className="pl-3">
              <h3 className="text-md font-medium text-xs whitespace-nowrap">{setor.name}</h3>
              <p className="text-sm font-bold">{setor.infractions}</p>
            </div>
          </div>
        ))
      ) : (
        <p>Sem dados para exibir</p>
      )}
    </div>
  </div>
  )
}
