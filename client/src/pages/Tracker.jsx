import Icon from "../components/Icon";

const stages = ["Introduced", "First Reading", "Committee Stage", "Second Reading", "Third Reading", "Passed", "Assent"];

const Tracker = ({ lang = "en" }) => (
  <main className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
    <p className="text-xs font-bold uppercase tracking-[0.18em] text-blue-700">
      {lang === "en" ? "Legislative tracker" : "Kifuatiliaji cha miswada"}
    </p>
    <h1 className="mt-3 text-4xl font-black text-slate-950">
      {lang === "en" ? "Follow bills through Parliament" : "Fuatilia miswada Bungeni"}
    </h1>

    <section className="mt-8 rounded-2xl border border-slate-200 bg-white p-6">
      <p className="text-xs font-bold text-blue-700">PROPOSED LEGISLATION</p>
      <h2 className="mt-2 text-2xl font-bold text-slate-950">The Public Participation Bill, 2023</h2>
      <p className="mt-1 text-slate-500">Senate Bill No. 4 of 2023</p>

      <div className="mt-8 grid gap-3 sm:grid-cols-4">
        {stages.map((stage, index) => (
          <div key={stage} className={`rounded-xl border p-4 ${index === 2 ? "border-blue-300 bg-blue-50" : "border-slate-200"}`}>
            <span className="grid size-8 place-items-center rounded-full bg-slate-100 text-sm font-bold text-slate-700">
              {index < 2 ? <Icon name="check" size={16} /> : index + 1}
            </span>
            <p className="mt-3 text-sm font-bold text-slate-800">{stage}</p>
          </div>
        ))}
      </div>
    </section>
  </main>
);

export default Tracker;
