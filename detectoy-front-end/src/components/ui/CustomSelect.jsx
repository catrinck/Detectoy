const CustomSelect = ({ options, value, onChange }) => {
    return (
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="p-1 border rounded-lg text-black px-4 pr-8"
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    );
  };
  
  export default CustomSelect;