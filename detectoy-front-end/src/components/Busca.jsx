import React from 'react'

export default function Busca() {
  return (
    <div>
        <form class="min-w-md mt-2">
                        <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only">Buscar</label>
                        <div class="relative">
                            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                <svg class="w-4 h-4 text-[#0E123F]-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                                </svg>
                            </div>
                            <input type="search" id="default-search"
                                class="block w-[350px] p-3 ps-10 text-sm text-[#0E123F] border border-[#0E123F] 
                    rounded-[26px] bg-[#0E123F]-50 focus:ring-white focus:border-white placeholder:text-[#0E123F] placeholder:font-normal"
                                placeholder="Buscar" required />
                        </div>
                    </form>
      
    </div>
  )
}
