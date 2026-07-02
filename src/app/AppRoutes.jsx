import { Routes, Route, Navigate } from "react-router-dom";

import LoginPage from "../features/auth/pages/LoginPage";
import { CrawlerPage } from "../features/crawler";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />

      <Route path="/app" element={<CrawlerPage />} />

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}