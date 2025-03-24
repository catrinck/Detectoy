import React from 'react'

export default function GerarRelatorio() {
    
    const handleSubmit = (e) =>  {
        e.preventDefault()
        console.log("bobao")
    }

    return (
    <div className="text-black p-4 rounded-lg">
    <div className="flex justify-between items-center">
      <h2 className="text-lg font-bold mb-4 text-darkBlue flex items-center gap-2">
        <img src='./relatorio-icon.svg' className="w-6 h-6" alt="Setor"/> Gerar Relatório
      </h2>
      
    </div>
    <div className='border border-black rounded-lg p-4'>
        <div className='flex item-center '>
            <form onSubmit={handleSubmit} className='flex flex-col gap-2'>
                <div className='flex item-center gap-2'>
                <input type='checkbox'></input>
                <label>
                    Por Setor
                </label>
                </div>
                <div className='flex gap-2'>
                <input type='checkbox'></input>
                <label>
                    Por Defeito
                </label>
                </div><div className='flex gap-2'>
                <input type='checkbox'></input>
                <label>
                    Por Tempo
                </label>
                </div>
            </form>
        </div>
        <div className='flex justify-end mt-2'>
            <button type='submit' onClick={handleSubmit} className='bg-[#AE91E9] text-white rounded-full py-1 px-8'>Gerar</button>
        </div>
    </div>
    </div>
  
  )
  
}
