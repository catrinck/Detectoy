const CustomSelect = ({ options, value, onChange }) => {
  const handleChange = (e) => {
    if (typeof onChange === 'function') {
      onChange(e.target.value);
    }
  };

  return (
    <select
      value={value}
      onChange={handleChange}
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