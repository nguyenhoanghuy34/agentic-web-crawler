import { Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "../features/auth/pages/LoginPage";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />

      {/* future crawler area */}
      <Route path="/app" element={<div>App Shell (crawler later)</div>} />

      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
}