import Icon from "../components/Icon";

const documents = [
  ["Constitution of Kenya, 2010", "Constitution", "Enacted law"],
  ["The Finance Bill, 2024", "Bills", "Proposal"],
  ["The Digital Health Act, 2023", "Acts", "Enacted law"],
  ["The Public Participation Bill, 2023", "Bills", "In committee"],
];

const Library = ({ lang = "en" }) => (
  <main className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
    <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
      <div>
        <p className="text-xs font-bold uppercase tracking-[0.18em] text-blue-700">
          {lang === "en" ? "Legal library" : "Maktaba ya sheria"}
        </p>
        <h1 className="mt-3 text-4xl font-black text-slate-950">
          {lang === "en" ? "Explore Legal Documents" : "Chunguza Nyaraka za Kisheria"}
        </h1>
      </div>
      <button className="flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-bold text-slate-700">
        <Icon name="upload" size={18} /> Upload PDF
      </button>
    </div>

    <div className="mt-8 grid gap-5 md:grid-cols-2">
      {documents.map(([title, category, status]) => (
        <article key={title} className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <div className="flex items-start justify-between gap-4">
            <span className="grid size-12 place-items-center rounded-xl bg-blue-50 text-blue-700">
              <Icon name="file" size={24} />
            </span>
            <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-bold text-slate-600">{status}</span>
          </div>
          <p className="mt-5 text-xs font-bold uppercase tracking-wider text-blue-700">{category}</p>
          <h2 className="mt-2 text-xl font-bold text-slate-950">{title}</h2>
        </article>
      ))}
    </div>
  </main>
);

export default Library;
