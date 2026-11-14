import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import InvoiceList from "./pages/InvoiceList";
import RemittanceDetail from "./pages/RemittanceDetail";
import { AuthProvider } from "./context/AuthContext";

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter basename="/supplier">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/invoices" element={<InvoiceList />} />
          <Route path="/remittances/:id" element={<RemittanceDetail />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}
