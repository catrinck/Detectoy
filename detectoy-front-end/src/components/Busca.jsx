import React, { useState } from 'react'

export default function Busca() {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  return (
    <div>
        <form className="min-w-md mt-2">
                        <label htmlFor="default-search" className="mb-2 text-sm font-medium text-gray-900 sr-only">Buscar</label>
                        <div className="relative">
                            <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                <svg className="w-4 h-4 text-[#0E123F]-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                    <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                                </svg>
                            </div>
                            <input 
                                type="search" 
                                id="default-search"
                                className="block w-[350px] p-3 ps-10 text-sm text-[#0E123F] border border-[#0E123F] 
                    rounded-[26px] bg-[#0E123F]-50 focus:ring-white focus:border-white placeholder:text-[#0E123F] placeholder:font-normal"
                                placeholder="Buscar" 
                                value={searchTerm}
                                onChange={handleSearchChange}
                                required 
                            />
                        </div>
                    </form>
      
    </div>
  )
}
