import AuthForm from "../components/AuthForm";
import "../auth.css";

import loginBackground from "../../../assets/login_background.jpg";

export default function LoginPage() {
    return (
        <div
            className="login-page"
            style={{
                backgroundImage: `url(${loginBackground})`,
            }}
        >
            <div className="login-overlay">

                <div className="glass-card">

                    <h1 className="title">
                        Welcome Back
                    </h1>

                    <p className="subtitle">
                        Sign in to continue
                    </p>

                    <AuthForm />

                </div>

            </div>
        </div>
    );
}