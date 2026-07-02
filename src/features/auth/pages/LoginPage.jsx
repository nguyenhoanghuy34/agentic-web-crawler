import AuthForm from "../components/AuthForm";

export default function LoginPage() {
  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2 className="title">Welcome back</h2>
        <p className="subtitle">Login to continue</p>

        <AuthForm />
      </div>
    </div>
  );
}