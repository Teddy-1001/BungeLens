import { useState } from "react";
import Icon from "../components/Icon";
const Home = ({ navigate, lang = "en" }) => {
    const [query, setQuery] = useState("");

    const features =
        lang === "en"
            ? [
                ["book", "Know Your Constitution", "Understand your rights, freedoms and responsibilities in clear, everyday language.", "workspace"],
                ["file", "Understand Parliamentary Bills", "Discover proposed laws and what their possible implications could be for you.", "tracker"],
                ["sparkle", "Ask BungeLens", "Ask questions and receive AI-powered explanations backed by original sources.", "chat"],
            ]
            : [
                ["book", "Ijue Katiba Yako", "Elewa haki, uhuru na wajibu wako kwa lugha rahisi ya kila siku.", "workspace"],
                ["file", "Elewa Miswada ya Bunge", "Gundua sheria zinazopendekezwa na athari zake zinazowezekana kwako.", "tracker"],
                ["sparkle", "Uliza BungeLens", "Uliza maswali upate maelezo yanayosaidiwa na AI na vyanzo halisi.", "chat"],
            ];

    const submitSearch = (event) => {
        event.preventDefault();
        if (query.trim()) {
            navigate("library");
        }
    };

    return (
        <>
            <main className="overflow-hidden">
                <section className="relative isolate overflow-hidden border-b border-slate-200/70 bg-slate-50">
                    {/* Background accents */}
                    <div
                        aria-hidden="true"
                        className="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_78%_25%,rgba(37,99,235,0.14),transparent_32%),linear-gradient(135deg,#f8fafc_0%,#eff6ff_55%,#f8fafc_100%)]"
                    />
                    <div
                        aria-hidden="true"
                        className="pointer-events-none absolute -right-24 -top-28 -z-10 size-80 rounded-full border border-blue-200/40"
                    />

                    <div className="mx-auto flex max-w-7xl flex-col items-center px-4 py-20 text-center sm:px-6 sm:py-24 lg:px-8 lg:py-28">
                        <span className="inline-flex items-center gap-2 rounded-full border border-blue-200/70 bg-white/75 px-4 py-2 text-sm font-semibold text-blue-800 shadow-sm shadow-blue-950/5">
                            <span className="size-2 rounded-full bg-green-600 ring-4 ring-green-100" />
                            {lang === "en"
                                ? "Civic knowledge for every Kenyan"
                                : "Elimu ya uraia kwa kila Mkenya"}
                        </span>

                        <h1 className="mt-7 max-w-4xl text-4xl font-black leading-[1.08] tracking-tight text-slate-950 sm:text-5xl lg:text-7xl">
                            {lang === "en" ? "Understand the laws that " : "Elewa sheria "}
                            <span className="text-blue-700">
                                {lang === "en"
                                    ? "shape your life."
                                    : "zinazoathiri maisha yako."}
                            </span>
                        </h1>

                        <p className="mt-6 max-w-2xl text-base leading-7 text-slate-600 sm:text-lg sm:leading-8">
                            {lang === "en"
                                ? "Explore Kenya’s Constitution and parliamentary bills in simple, understandable language."
                                : "Chunguza Katiba ya Kenya na miswada ya Bunge kwa lugha rahisi na inayoeleweka."}
                        </p>

                        <form
                            onSubmit={submitSearch}
                            role="search"
                            className="mt-9 flex w-full max-w-2xl items-center gap-2 rounded-2xl border border-slate-200 bg-white p-2 shadow-xl shadow-slate-900/[0.06] transition focus-within:border-blue-300 focus-within:ring-4 focus-within:ring-blue-100"
                        >
                            <span className="ml-2 shrink-0 text-slate-400">
                                <Icon name="search" size={20} />
                            </span>

                            <input
                                value={query}
                                onChange={(event) => setQuery(event.target.value)}
                                aria-label={lang === "en" ? "Search documents" : "Tafuta nyaraka"}
                                placeholder={
                                    lang === "en"
                                        ? "Search the Constitution, bills or legal topics..."
                                        : "Tafuta Katiba, miswada au mada za kisheria..."
                                }
                                className="min-w-0 flex-1 border-0 bg-transparent px-2 py-3 text-sm text-slate-900 outline-none placeholder:text-slate-400 sm:text-base"
                            />

                            <button
                                type="submit"
                                aria-label={lang === "en" ? "Search" : "Tafuta"}
                                className="grid size-11 shrink-0 place-items-center rounded-xl bg-blue-700 text-white transition hover:bg-blue-800 focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-blue-200"
                            >
                                <Icon name="arrow" size={19} />
                            </button>
                        </form>

                        <div className="mt-6 flex flex-wrap items-center justify-center gap-x-6 gap-y-3 text-sm font-medium text-slate-600">
                            <span className="inline-flex items-center gap-2">
                                <Icon name="shield" size={16} />
                                {lang === "en" ? "Source-backed" : "Yenye vyanzo"}
                            </span>

                            <span className="inline-flex items-center gap-2">
                                <Icon name="check" size={16} />
                                {lang === "en" ? "Plain language" : "Lugha rahisi"}
                            </span>

                            <span className="inline-flex items-center gap-2">
                                <span className="size-2 rounded-full bg-green-600" />
                                English & Kiswahili
                            </span>
                        </div>
                    </div>
                </section>

               <section className="relative mx-auto max-w-7xl px-4 py-20 sm:px-6 sm:py-24 lg:px-8">
  <div
    aria-hidden="true"
    className="pointer-events-none absolute left-1/2 top-16 -z-10 h-56 w-[min(90%,48rem)] -translate-x-1/2 rounded-full bg-blue-100/50 blur-3xl"
  />

  <div className="mx-auto max-w-2xl text-center">
    <span className="inline-flex items-center gap-2 rounded-full border border-blue-100 bg-blue-50/80 px-3 py-1.5 text-xs font-bold uppercase tracking-[0.16em] text-blue-800">
      <span className="size-1.5 rounded-full bg-blue-600" />
      {lang === "en" ? "Knowledge is power" : "Maarifa ni nguvu"}
    </span>

    <h2 className="mt-5 text-3xl font-black tracking-tight text-slate-950 sm:text-4xl lg:text-5xl">
      {lang === "en"
        ? "Law, made easier to understand"
        : "Sheria, kwa lugha inayoeleweka"}
    </h2>

    <p className="mx-auto mt-4 max-w-xl text-base leading-7 text-slate-600 sm:text-lg">
      {lang === "en"
        ? "Explore, understand and engage with the laws that shape our nation."
        : "Chunguza, elewa na shiriki katika sheria zinazounda taifa letu."}
    </p>
  </div>

  <div className="mt-12 grid gap-5 md:grid-cols-3">
    {features.map(([icon, title, text, destination], index) => (
      <button
        key={title}
        type="button"
        onClick={() => navigate(destination)}
        className="group relative flex h-full flex-col overflow-hidden rounded-2xl border border-slate-200/80 bg-white p-6 text-left shadow-sm transition duration-300 hover:-translate-y-1 hover:border-blue-200 hover:shadow-xl hover:shadow-slate-900/[0.07] focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-blue-200"
      >
        <span
          aria-hidden="true"
          className="absolute right-0 top-0 h-28 w-28 -translate-y-1/2 translate-x-1/2 rounded-full bg-blue-50 opacity-0 transition duration-300 group-hover:opacity-100"
        />

        <span className="relative grid size-12 place-items-center rounded-xl bg-blue-50 text-blue-700 transition duration-300 group-hover:bg-blue-700 group-hover:text-white">
          <Icon name={icon} size={24} />
        </span>

        <h3 className="relative mt-5 text-xl font-bold text-slate-950">
          {title}
        </h3>

        <p className="relative mt-3 flex-1 leading-7 text-slate-600">
          {text}
        </p>

        <span className="relative mt-6 inline-flex items-center gap-2 text-sm font-bold text-blue-700">
          {lang === "en" ? "Learn more" : "Jifunze zaidi"}
          <span className="transition-transform duration-200 group-hover:translate-x-1">
            <Icon name="arrow" size={16} />
          </span>
        </span>
      </button>
    ))}
  </div>
</section>

                <section className="border-y border-slate-200/80 bg-white">
  <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
    <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
      <div>
        <span className="inline-flex items-center gap-2 rounded-full bg-blue-50 px-3 py-1.5 text-xs font-bold uppercase tracking-[0.16em] text-blue-800">
          <span className="size-1.5 rounded-full bg-blue-600" />
          {lang === "en" ? "Featured documents" : "Nyaraka maalum"}
        </span>

        <h2 className="mt-4 text-3xl font-black tracking-tight text-slate-950 sm:text-4xl">
          {lang === "en"
            ? "Start with what matters"
            : "Anza na yaliyo muhimu"}
        </h2>
      </div>

      <button
        type="button"
        onClick={() => navigate("library")}
        className="group inline-flex w-fit items-center gap-2 text-sm font-bold text-blue-700 transition hover:text-blue-900 focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-blue-200 sm:mb-1"
      >
        {lang === "en" ? "View all documents" : "Tazama nyaraka zote"}
        <span className="transition-transform group-hover:translate-x-1">
          <Icon name="arrow" size={17} />
        </span>
      </button>
    </div>

    <div className="mt-9 grid gap-5 lg:grid-cols-[1.2fr_0.8fr]">
      <button
        type="button"
        onClick={() => navigate("workspace")}
        className="group flex flex-col gap-6 rounded-2xl border border-slate-200 bg-slate-50 p-5 text-left transition duration-300 hover:border-blue-200 hover:shadow-xl hover:shadow-slate-900/[0.06] focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-blue-200 sm:flex-row sm:items-center"
      >
        <div className="grid aspect-[4/5] w-full shrink-0 place-items-center overflow-hidden rounded-xl bg-gradient-to-br from-blue-950 via-blue-900 to-slate-900 p-6 text-center text-white shadow-inner sm:w-44">
          <div>
            <Icon name="scale" size={36} />
            <p className="mt-4 text-sm font-bold leading-5 tracking-wide">
              THE CONSTITUTION
              <br />
              OF KENYA
            </p>
            <p className="mt-2 text-xs font-semibold tracking-[0.2em] text-blue-200">
              2010
            </p>
          </div>
        </div>

        <div className="flex flex-1 flex-col justify-center">
          <span className="w-fit rounded-full bg-emerald-100 px-2.5 py-1 text-[11px] font-bold uppercase tracking-wider text-emerald-800">
            {lang === "en" ? "Enacted law" : "Sheria iliyopitishwa"}
          </span>

          <h3 className="mt-3 text-xl font-bold text-slate-950">
            Constitution of Kenya, 2010
          </h3>

          <p className="mt-3 leading-7 text-slate-600">
            {lang === "en"
              ? "The supreme law of the Republic, setting out the rights, duties and structure of government."
              : "Sheria kuu ya Jamhuri inayoeleza haki, wajibu na muundo wa serikali."}
          </p>

          <span className="mt-5 inline-flex items-center gap-2 text-sm font-bold text-blue-700">
            {lang === "en"
              ? "Read the simplified Constitution"
              : "Soma Katiba iliyorahisishwa"}
            <span className="transition-transform group-hover:translate-x-1">
              <Icon name="arrow" size={16} />
            </span>
          </span>
        </div>
      </button>

      <div className="grid gap-3">
        {[
          {
            title: "The Finance Bill, 2024",
            meta: "National Assembly Bill No. 30",
            destination: "tracker",
            status: lang === "en" ? "Proposal" : "Pendekezo",
            tone: "bg-amber-100 text-amber-800",
          },
          {
            title: "The Digital Health Act, 2023",
            meta: "Act No. 15 of 2023",
            destination: "impact",
            status: lang === "en" ? "Enacted law" : "Sheria iliyopitishwa",
            tone: "bg-emerald-100 text-emerald-800",
          },
          {
            title: "The Public Participation Bill, 2023",
            meta: "Senate Bill No. 4",
            destination: "tracker",
            status: lang === "en" ? "In committee" : "Kamati",
            tone: "bg-indigo-100 text-indigo-800",
          },
        ].map(({ title, meta, destination, status, tone }) => (
          <button
            key={title}
            type="button"
            onClick={() => navigate(destination)}
            className="group flex items-center gap-4 rounded-xl border border-slate-200 bg-white p-4 text-left transition duration-200 hover:border-blue-200 hover:bg-blue-50/50 focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-blue-200"
          >
            <span className="grid size-11 shrink-0 place-items-center rounded-lg bg-slate-100 text-slate-700 transition group-hover:bg-blue-100 group-hover:text-blue-800">
              <Icon name="file" size={20} />
            </span>

            <span className="min-w-0 flex-1">
              <strong className="block truncate text-sm text-slate-950">
                {title}
              </strong>
              <span className="mt-1 block truncate text-xs text-slate-500">
                {meta}
              </span>
            </span>

            <span
              className={`hidden shrink-0 rounded-full px-2 py-1 text-[10px] font-bold uppercase tracking-wide sm:inline-flex ${tone}`}
            >
              {status}
            </span>

            <span className="shrink-0 text-slate-400 transition group-hover:translate-x-0.5 group-hover:text-blue-700">
              <Icon name="arrow" size={16} />
            </span>
          </button>
        ))}
      </div>
    </div>
  </div>
</section>

                <section className="bg-slate-950">
                    <div className="mx-auto flex max-w-7xl flex-col items-start justify-between gap-8 px-4 py-12 sm:px-6 md:flex-row md:items-center lg:px-8">
                        <div>
                            <p className="text-xs font-bold uppercase tracking-[0.18em] text-blue-300">Ask. Understand. Participate.</p>
                            <h2 className="mt-3 text-3xl font-black tracking-tight text-white">
                                {lang === "en" ? "Have a question about Kenyan law?" : "Una swali kuhusu sheria ya Kenya?"}
                            </h2>
                        </div>
                        <button
                            onClick={() => navigate("chat")}
                            className="flex shrink-0 items-center gap-2 rounded-xl bg-white px-5 py-3 text-sm font-bold text-blue-900 transition hover:bg-blue-50"
                        >
                            <Icon name="sparkle" size={18} />
                            {lang === "en" ? "Ask BungeLens" : "Uliza BungeLens"}
                        </button>
                    </div>
                </section>
            </main>

        </>
    );
};

export default Home;
