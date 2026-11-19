import {
  ArrowRight,
  BookOpen,
  Check,
  Clock,
  FileText,
  Search,
  Send,
  ShieldCheck,
  Scale,
  Sparkles,
  Upload,
} from "lucide-react";

const icons = {
  arrow: ArrowRight,
  book: BookOpen,
  check: Check,
  clock: Clock,
  file: FileText,
  search: Search,
  send: Send,
  shield: ShieldCheck,
  scale: Scale,
  sparkle: Sparkles,
  upload: Upload,
};

const Icon = ({ name, size = 20 }) => {
  const IconComponent = icons[name];

  if (!IconComponent) return null;

  return <IconComponent size={size} aria-hidden="true" />;
};

export default Icon;