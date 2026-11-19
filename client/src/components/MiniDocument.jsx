// MiniDocument.jsx
import Icon from "./Icon";
import Badge from "./Badge";

const MiniDocument = ({ title, meta, status, tone = "green", onClick }) => {
  return (
    <button className="mini-document" onClick={onClick}>
      <span className="mini-document-icon">
        <Icon name="file" size={20} />
      </span>

      <span className="mini-document-content">
        <strong>{title}</strong>
        <span>{meta}</span>
      </span>

      <Badge tone={tone}>{status}</Badge>
    </button>
  );
};

export default MiniDocument;