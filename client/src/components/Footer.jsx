import { LogOut } from "lucide-react";
import Icon from "./Icon";

const Footer = ({ lang, navigate }) => {
  const isEnglish = lang === "en";

  const platformLinks = [
    {
      label: isEnglish ? "Constitution" : "Katiba",
      destination: "workspace",
    },
    {
      label: isEnglish ? "Parliamentary Bills" : "Miswada ya Bunge",
      destination: "tracker",
    },
    {
      label: isEnglish ? "Ask BungeLens" : "Uliza BungeLens",
      destination: "chat",
    },
  ];

  const companyLinks = [
    { label: isEnglish ? "About" : "Kuhusu nasi", destination: "about" },
    { label: isEnglish ? "Contact" : "Wasiliana nasi", destination: "contact" },
    { label: isEnglish ? "Privacy" : "Faragha", destination: "privacy" },
  ];

  return (
    <footer className="border-t border-slate-200 bg-slate-950 text-slate-300">
      <div className="mx-auto grid max-w-7xl gap-10 px-4 py-12 sm:px-6 md:grid-cols-2 lg:grid-cols-[1.4fr_0.8fr_0.8fr_1.2fr] lg:gap-12 lg:px-8 lg:py-16">
        <div>
          <LogOut
            onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
          />
          <p className="mt-4 max-w-sm text-sm leading-6 text-slate-400">
            {isEnglish
              ? "Making Kenya’s laws clearer, one document at a time."
              : "Kufanya sheria za Kenya zieleweke, hati moja baada ya nyingine."}
          </p>
        </div>

        <nav aria-label={isEnglish ? "Platform" : "Jukwaa"}>
          <h2 className="text-sm font-bold text-white">
            {isEnglish ? "Platform" : "Jukwaa"}
          </h2>
          <ul className="mt-4 space-y-3">
            {platformLinks.map(({ label, destination }) => (
              <li key={destination}>
                <button
                  type="button"
                  onClick={() => navigate(destination)}
                  className="text-left text-sm text-slate-400 transition hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-400"
                >
                  {label}
                </button>
              </li>
            ))}
          </ul>
        </nav>

        <nav aria-label={isEnglish ? "Company" : "Kuhusu nasi"}>
          <h2 className="text-sm font-bold text-white">
            {isEnglish ? "Company" : "Kuhusu nasi"}
          </h2>
          <ul className="mt-4 space-y-3">
            {companyLinks.map(({ label, destination }) => (
              <li key={destination}>
                <button
                  type="button"
                  onClick={() => navigate(destination)}
                  className="text-left text-sm text-slate-400 transition hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-400"
                >
                  {label}
                </button>
              </li>
            ))}
          </ul>
        </nav>

        <div className="rounded-2xl border border-white/10 bg-white/[0.04] p-5">
          <span className="inline-flex size-9 items-center justify-center rounded-lg bg-blue-500/10 text-blue-300">
            <Icon name="shield" size={19} />
          </span>
          <p className="mt-4 text-sm leading-6 text-slate-400">
            {isEnglish
              ? "BungeLens provides civic information and does not replace professional legal advice."
              : "BungeLens hutoa elimu ya uraia na haichukui nafasi ya ushauri wa kitaalamu wa kisheria."}
          </p>
        </div>
      </div>

      <div className="border-t border-white/10">
        <div className="mx-auto flex max-w-7xl flex-col gap-2 px-4 py-5 text-xs text-slate-500 sm:flex-row sm:items-center sm:justify-between sm:px-6 lg:px-8">
          <span>© {new Date().getFullYear()} BungeLens</span>
          <span>
            {isEnglish
              ? "Built for informed citizens of Kenya"
              : "Imejengwa kwa ajili ya raia wenye ufahamu nchini Kenya"}
          </span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;