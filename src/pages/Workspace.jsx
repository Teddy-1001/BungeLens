import Icon from "../components/Icon";

const Workspace = ({ lang = "en" }) => (
  <main className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
    <div className="flex flex-wrap items-end justify-between gap-4">
      <div>
        <p className="text-sm text-slate-500">
          Library / Constitution / Chapter Four
        </p>
        <h1 className="mt-2 text-3xl font-black text-slate-950">
          Constitution of Kenya, 2010
        </h1>
        <p className="mt-2 text-slate-600">
          Chapter Four — The Bill of Rights
        </p>
      </div>

      <span className="rounded-full bg-blue-100 px-3 py-1 text-xs font-bold text-blue-800">
        Enacted law
      </span>
    </div>

    <div className="mt-8 grid gap-5 lg:grid-cols-[15rem_minmax(0,1fr)] xl:grid-cols-[15rem_minmax(0,1fr)_minmax(0,1fr)]">
      <aside className="hidden self-start rounded-2xl border border-slate-200 bg-white p-4 lg:sticky lg:top-24 lg:block lg:max-h-[calc(100vh-8rem)] lg:overflow-y-auto">
        <div className="mb-3 flex items-center justify-between px-2">
          <span className="text-xs font-bold uppercase tracking-wider text-slate-500">
            {lang === "en" ? "Contents" : "Yaliyomo"}
          </span>
          <Icon name="search" size={16} />
        </div>

        <nav
          aria-label={
            lang === "en" ? "Document chapters" : "Sura za hati"
          }
          className="space-y-1"
        >
          <button
            type="button"
            className="flex w-full flex-col rounded-lg px-3 py-2.5 text-left text-sm font-semibold text-slate-700 transition hover:bg-slate-50"
          >
            {lang === "en" ? "Chapter One" : "Sura ya Kwanza"}
            <span className="mt-1 text-xs font-normal text-slate-500">
              Sovereignty &amp; the Republic
            </span>
          </button>

          <button
            type="button"
            className="flex w-full flex-col rounded-lg px-3 py-2.5 text-left text-sm font-semibold text-slate-700 transition hover:bg-slate-50"
          >
            {lang === "en" ? "Chapter Two" : "Sura ya Pili"}
            <span className="mt-1 text-xs font-normal text-slate-500">
              The Republic
            </span>
          </button>

          <button
            type="button"
            aria-current="page"
            className="flex w-full flex-col rounded-lg bg-blue-50 px-3 py-2.5 text-left text-sm font-semibold text-blue-800"
          >
            {lang === "en" ? "Chapter Four" : "Sura ya Nne"}
            <span className="mt-1 text-xs font-normal text-blue-700">
              The Bill of Rights
            </span>
          </button>

          <button
            type="button"
            aria-current="location"
            className="ml-3 flex w-[calc(100%-0.75rem)] flex-col rounded-lg border-l-2 border-blue-600 bg-blue-50/60 px-3 py-2.5 text-left text-sm font-medium text-blue-800"
          >
            Article 43
            <span className="mt-1 text-xs font-normal text-slate-500">
              Economic &amp; social rights
            </span>
          </button>

          <button
            type="button"
            className="ml-3 flex w-[calc(100%-0.75rem)] flex-col rounded-lg px-3 py-2.5 text-left text-sm font-medium text-slate-600 transition hover:bg-slate-50"
          >
            Article 44
            <span className="mt-1 text-xs font-normal text-slate-500">
              Language and culture
            </span>
          </button>

          <button
            type="button"
            className="flex w-full flex-col rounded-lg px-3 py-2.5 text-left text-sm font-semibold text-slate-700 transition hover:bg-slate-50"
          >
            {lang === "en" ? "Chapter Five" : "Sura ya Tano"}
            <span className="mt-1 text-xs font-normal text-slate-500">
              Land and Environment
            </span>
          </button>
        </nav>
      </aside>

      <article className="min-w-0 rounded-2xl border border-slate-200 bg-white p-6">
        <p className="text-xs font-bold tracking-wider text-slate-500">
          AUTHORITATIVE LEGAL TEXT
        </p>
        <h2 className="mt-4 text-2xl font-bold text-slate-950">
          Article 43 — Economic and social rights
        </h2>
        <p className="mt-5 leading-8 text-slate-700">
          Every person has the right to the highest attainable standard of
          health, accessible housing, adequate food and water, social security
          and education.
        </p>
      </article>

      <article className="min-w-0 rounded-2xl border border-blue-100 bg-blue-50 p-6">
        <div className="flex items-center gap-2 text-blue-800">
          <Icon name="sparkle" size={18} />
          <p className="text-xs font-bold tracking-wider">
            {lang === "en"
              ? "AI-GENERATED EXPLANATION"
              : "MAELEZO YA AI"}
          </p>
        </div>
        <h2 className="mt-4 text-2xl font-bold text-slate-950">
          {lang === "en"
            ? "What Article 43 means"
            : "Maana ya Ibara ya 43"}
        </h2>
        <p className="mt-5 leading-8 text-slate-700">
          Every person in Kenya is entitled to basic services needed for a
          dignified life, including healthcare, housing, food, clean water,
          social support and education.
        </p>
      </article>
    </div>
  </main>
);

export default Workspace;