import { Invoice, Remittance, StatementLine } from "../types";

const BASE = process.env.REACT_APP_API_BASE ?? "/api/supplier";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${BASE}${path}`, {
    credentials: "include",
    headers: { "Content-Type": "application/json" },
    ...init,
  });
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return (await response.json()) as T;
}

export const api = {
  invoices: () => request<Invoice[]>("/invoices"),
  remittances: () => request<Remittance[]>("/remittances"),
  statement: (from: string, to: string) =>
    request<StatementLine[]>(`/statement?from=${from}&to=${to}`),
  uploadInvoice: (body: FormData) =>
    request<{ id: string }>("/invoices", { method: "POST", body }),
};
