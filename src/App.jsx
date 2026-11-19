import { useEffect } from "react";
import { Navigate, Route, Routes, useLocation, useNavigate } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import Library from "./pages/Library";
import Workspace from "./pages/Workspace";
import Chat from "./pages/Chat";
import Tracker from "./pages/Tracker";
import Impact from "./pages/Impact";

const navCopy = {
  en: {
    home: "Home",
    constitution: "Constitution",
    bills: "Bills",
    ask: "Ask",
    getStarted: "Get Started",
  },
};

const App = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const lang = "en";

  useEffect(() => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, [location.pathname]);

  return (
    <div className="min-h-screen bg-slate-50">
      <Header t={navCopy[lang]} />
      <Routes location={location}>
        <Route path="/" element={<Home navigate={(path) => navigate(`/${path}`)} lang={lang} />} />
        <Route path="/home" element={<Navigate replace to="/" />} />
        <Route path="/library" element={<Library lang={lang} />} />
        <Route path="/workspace" element={<Workspace lang={lang} />} />
        <Route path="/chat" element={<Chat lang={lang} />} />
        <Route path="/tracker" element={<Tracker lang={lang} />} />
        <Route path="/impact" element={<Impact lang={lang} />} />
        <Route path="*" element={<Navigate replace to="/" />} />
      </Routes>
      <Footer lang={lang} />
    </div>
  );
};

export default App;
