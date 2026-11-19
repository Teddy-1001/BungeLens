// Button.jsx
import Icon from "./Icon";

const Button = ({ children, icon, variant = "primary", onClick }) => {
  return (
    <button className={`button button-${variant}`} onClick={onClick}>
      {icon && <Icon name={icon} size={18} />}
      <span>{children}</span>
    </button>
  );
};

export default Button;