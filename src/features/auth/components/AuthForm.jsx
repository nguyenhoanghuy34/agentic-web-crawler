import { useState } from "react";
import { useNavigate } from "react-router-dom";
import GoogleButton from "./GoogleButton";

export default function AuthForm() {
  const navigate = useNavigate();

  const [mode, setMode] = useState("login"); // login | register
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (mode === "login") {
      // Giả lập đăng nhập thành công
      console.log("LOGIN:", { email, password });

      // Chuyển sang trang chính
      navigate("/app");
    } else {
      // Giả lập đăng ký thành công
      console.log("REGISTER:", { email, password });

      // Sau này có thể chuyển về login hoặc tự động đăng nhập
      alert("Đăng ký thành công (giả lập)");
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
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">
          {mode === "login" ? "Login" : "Create account"}
        </button>
      </form>

      <p className="switch">
        {mode === "login"
          ? "No account?"
          : "Already have an account?"}{" "}
        <span
          onClick={() =>
            setMode(mode === "login" ? "register" : "login")
          }
        >
          {mode === "login" ? "Create one" : "Login"}
        </span>
      </p>
    </div>
  );
}