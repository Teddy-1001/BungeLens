import { useState } from "react";
import Icon from "../components/Icon";

const suggestions = [
  "What does Article 43 mean?",
  "What rights do I have as a Kenyan citizen?",
  "Explain the Finance Bill in simple English",
];

const Chat = () => {
  const [message, setMessage] = useState("");

  return (
    <main className="mx-auto max-w-4xl px-4 py-12 sm:px-6">
      <div className="rounded-2xl border border-slate-200 bg-white shadow-sm">
        <div className="border-b border-slate-200 p-5">
          <h1 className="text-2xl font-black text-slate-950">Ask BungeLens</h1>
          <p className="mt-1 text-sm text-slate-500">Answers grounded in Kenyan legal sources</p>
        </div>
        <div className="grid gap-3 p-5 sm:grid-cols-3">
          {suggestions.map((suggestion) => (
            <button
              key={suggestion}
              onClick={() => setMessage(suggestion)}
              className="rounded-xl border border-slate-200 p-4 text-left text-sm font-medium text-slate-700 hover:border-blue-200"
            >
              {suggestion}
            </button>
          ))}
        </div>
        <form className="flex gap-2 border-t border-slate-200 p-4" onSubmit={(event) => event.preventDefault()}>
          <input
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            placeholder="Ask a question about Kenyan law..."
            className="min-w-0 flex-1 rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
          />
          <button aria-label="Send" className="grid size-12 place-items-center rounded-xl bg-blue-700 text-white">
            <Icon name="send" size={18} />
          </button>
        </form>
      </div>
    </main>
  );
};

export default Chat;
