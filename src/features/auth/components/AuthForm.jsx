import { useState } from "react";
import GoogleButton from "./GoogleButton";

export default function AuthForm() {
  const [mode, setMode] = useState("login"); // login | register
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (mode === "login") {
      console.log("LOGIN:", { email, password });
    } else {
      console.log("REGISTER:", { email, password });
    }
  };

  return (
    <div>
      <GoogleButton />

      <div className="divider">OR</div>

      <form onSubmit={handleSubmit} className="form">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit">
          {mode === "login" ? "Login" : "Create account"}
        </button>
      </form>

      <p className="switch">
        {mode === "login" ? "No account?" : "Already have account?"}{" "}
        <span onClick={() => setMode(mode === "login" ? "register" : "login")}>
          Click here
        </span>
      </p>
    </div>
  );
}