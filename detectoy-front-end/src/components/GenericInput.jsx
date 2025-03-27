export default function GenericInput({ campo, placeholder, value, onChange }) {
  const handleChange = (e) => {
    // Verifica se onChange é uma função
    if (typeof onChange === 'function') {
      // Como não sabemos se onChange espera um evento ou um valor,
      // passamos o valor diretamente
      onChange(e.target.value);
    }
  };

  return (
    <div className="m-5 text-[16px]">
      <label className="text-[#011128] block mb-2">{campo}</label>
      <input className="bg-[#EBEAED] rounded-lg p-2 w-full" 
        placeholder={placeholder}
        value={value} // Valor controlado
        onChange={handleChange} // Usa a função segura
      />
    </div>
  );
}