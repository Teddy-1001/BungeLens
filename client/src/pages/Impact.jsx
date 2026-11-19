import { useState } from "react";
import Icon from "../components/Icon";

const audiences = ["Workers", "Students", "Small businesses", "Farmers", "General citizens"];

const Impact = ({ lang = "en" }) => {
  const [audience, setAudience] = useState("Small businesses");

  return (
    <main className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
      <p className="text-xs font-bold uppercase tracking-[0.18em] text-blue-700">
        {lang === "en" ? "Citizen impact explorer" : "Uchambuzi wa athari kwa wananchi"}
      </p>
      <h1 className="mt-3 text-4xl font-black text-slate-950">
        {lang === "en" ? "How could this bill affect you?" : "Muswada huu unaweza kukuathirije?"}
      </h1>

      <div className="mt-8 flex flex-wrap gap-3">
        {audiences.map((item) => (
          <button
            key={item}
            onClick={() => setAudience(item)}
            className={`flex items-center gap-2 rounded-xl border px-4 py-3 text-sm font-bold ${
              audience === item ? "border-blue-300 bg-blue-50 text-blue-800" : "border-slate-200 bg-white text-slate-700"
            }`}
          >
            <Icon name="users" size={18} /> {item}
          </button>
        ))}
      </div>

      <div className="mt-8 grid gap-5 md:grid-cols-2">
        <article className="rounded-2xl border border-blue-200 bg-white p-6">
          <h2 className="text-xl font-bold text-slate-950">Potential benefits for {audience}</h2>
          <p className="mt-3 leading-7 text-slate-600">Expanded electronic systems could make filing more predictable and reduce paperwork.</p>
        </article>
        <article className="rounded-2xl border border-slate-200 bg-white p-6">
          <h2 className="text-xl font-bold text-slate-950">Potential concerns</h2>
          <p className="mt-3 leading-7 text-slate-600">New reporting requirements may increase compliance costs and require updated systems.</p>
        </article>
      </div>
    </main>
  );
};

export default Impact;
