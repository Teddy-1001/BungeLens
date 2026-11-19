import Icon from "../components/Icon";

const Workspace = ({ lang = "en" }) => (
  <main className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
    <div className="flex flex-wrap items-end justify-between gap-4">
      <div>
        <p className="text-sm text-slate-500">Library / Constitution / Chapter Four</p>
        <h1 className="mt-2 text-3xl font-black text-slate-950">Constitution of Kenya, 2010</h1>
        <p className="mt-2 text-slate-600">Chapter Four - The Bill of Rights</p>
      </div>
      <span className="rounded-full bg-blue-100 px-3 py-1 text-xs font-bold text-blue-800">Enacted law</span>
    </div>

    <div className="mt-8 grid gap-5 lg:grid-cols-2">
      <article className="rounded-2xl border border-slate-200 bg-white p-6">
        <p className="text-xs font-bold tracking-wider text-slate-500">AUTHORITATIVE LEGAL TEXT</p>
        <h2 className="mt-4 text-2xl font-bold text-slate-950">Article 43 - Economic and social rights</h2>
        <p className="mt-5 leading-8 text-slate-700">
          Every person has the right to the highest attainable standard of health, accessible housing,
          adequate food and water, social security and education.
        </p>
      </article>
      <article className="rounded-2xl border border-blue-100 bg-blue-50 p-6">
        <div className="flex items-center gap-2 text-blue-800">
          <Icon name="sparkle" size={18} />
          <p className="text-xs font-bold tracking-wider">{lang === "en" ? "AI-GENERATED EXPLANATION" : "MAELEZO YA AI"}</p>
        </div>
        <h2 className="mt-4 text-2xl font-bold text-slate-950">
          {lang === "en" ? "What Article 43 means" : "Maana ya Ibara ya 43"}
        </h2>
        <p className="mt-5 leading-8 text-slate-700">
          Every person in Kenya is entitled to basic services needed for a dignified life,
          including healthcare, housing, food, clean water, social support and education.
        </p>
      </article>
    </div>
  </main>
);

export default Workspace;
