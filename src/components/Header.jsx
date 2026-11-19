import { useState } from "react";
import { BookBookmark, Menu, X, ChevronRight } from "lucide-react";
import { useLocation, useNavigate } from "react-router-dom";

const Header = ({ t }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const [open, setOpen] = useState(false);

  const currentPage = location.pathname.split("/")[1] || "home";

  const navItems = [
    { path: "home", label: t.home },
    { path: "workspace", label: t.constitution },
    { path: "tracker", label: t.bills },
    { path: "chat", label: t.ask },
  ];

  const goTo = (path) => {
    navigate(path === "home" ? "/" : `/${path}`);
    setOpen(false);
  };

  return (
    <header className="sticky top-0 z-50 border-b border-slate-200/80 bg-white/90 backdrop-blur-xl">
      <div className="mx-auto flex h-16 max-w-7xl items-center px-4 sm:px-6 lg:px-8">
        <button
          type="button"
          onClick={() => goTo("home")}
          aria-label="BungeLens — home"
          className="group flex shrink-0 items-center gap-2.5"
        >
          <span className="grid size-10 place-items-center rounded-xl bg-blue-700 text-white shadow-sm shadow-blue-700/20 transition duration-200 group-hover:-translate-y-0.5 group-hover:bg-blue-800 group-hover:shadow-md">
            <BookBookmark className="size-5" aria-hidden="true" />
          </span>

          <span className="hidden text-sm font-bold tracking-tight text-slate-900 sm:block">
            Bunge<span className="text-blue-700">Lens</span>
          </span>
        </button>

        <nav
          id="primary-navigation"
          aria-label="Main navigation"
          className={`${
            open ? "block" : "hidden"
          } absolute left-0 right-0 top-16 border-b border-slate-200 bg-white px-4 pb-5 pt-3 shadow-xl shadow-slate-900/5 md:static md:ml-10 md:flex md:flex-1 md:items-center md:border-0 md:bg-transparent md:p-0 md:shadow-none`}
        >
          <div className="flex flex-col gap-1 md:flex-row md:items-center">
            {navItems.map(({ path, label }) => {
              const active = currentPage === path;

              return (
                <button
                  key={path}
                  type="button"
                  onClick={() => goTo(path)}
                  aria-current={active ? "page" : undefined}
                  className={`relative rounded-lg px-3.5 py-2.5 text-left text-sm font-medium transition md:text-center ${
                    active
                      ? "bg-blue-50 text-blue-800"
                      : "text-slate-600 hover:bg-slate-100 hover:text-slate-950"
                  }`}
                >
                  {label}
                  {active && (
                    <span
                      aria-hidden="true"
                      className="absolute bottom-0 left-1/2 hidden h-0.5 w-5 -translate-x-1/2 rounded-full bg-blue-600 md:block"
                    />
                  )}
                </button>
              );
            })}
          </div>

          <button
            type="button"
            onClick={() => goTo("library")}
            className="mt-4 flex w-full items-center justify-center gap-2 rounded-xl bg-blue-700 px-4 py-3 text-sm font-semibold text-white shadow-sm shadow-blue-700/20 transition hover:bg-blue-800 hover:shadow-md active:scale-[0.98] focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-blue-200 md:hidden"
          >
            {t.getStarted}
            <ChevronRight className="size-4" aria-hidden="true" />
          </button>
        </nav>

        <div className="ml-auto hidden md:block">
          <button
            type="button"
            onClick={() => goTo("library")}
            className="flex items-center gap-2 rounded-xl bg-blue-700 px-4 py-2.5 text-sm font-semibold text-white shadow-sm shadow-blue-700/20 transition hover:-translate-y-0.5 hover:bg-blue-800 hover:shadow-md active:translate-y-0 focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-blue-200"
          >
            {t.getStarted}
            <ChevronRight className="size-4" aria-hidden="true" />
          </button>
        </div>

        <button
          type="button"
          onClick={() => setOpen((previous) => !previous)}
          aria-label={open ? "Close navigation" : "Open navigation"}
          aria-expanded={open}
          aria-controls="primary-navigation"
          className="ml-auto grid size-10 place-items-center rounded-xl text-slate-700 transition hover:bg-slate-100 hover:text-slate-950 active:scale-95 focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-blue-200 md:hidden"
        >
          {open ? (
            <X className="size-5" aria-hidden="true" />
          ) : (
            <Menu className="size-5" aria-hidden="true" />
          )}
        </button>
      </div>
    </header>
  );
};

export default Header;