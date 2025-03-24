
export default function GenericInput({ campo, placeholder, value, onChange }) {
  return (
    <div className="m-5 text-[16px]">
      <label className="text-[#011128] block mb-2">{campo}</label>
      <input className="bg-[#EBEAED] rounded-lg p-2 w-full" 
        placeholder={placeholder}
        value={value} // Valor controlado
        onChange={(e) => onChange(e.target.value)} // Captura o valor do input
      />
    </div>
  );
}