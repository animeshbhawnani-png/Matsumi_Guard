import { useEffect, useState } from "react";

const SUPPORTED_WALLETS = [
  { key: "nami", label: "Nami" },
  { key: "eternl", label: "Eternl" }
];

export function WalletConnector({ onConnected }) {
  const [availableWallets, setAvailableWallets] = useState([]);
  const [connecting, setConnecting] = useState(false);
  const [connectedWallet, setConnectedWallet] = useState(null);
  const [connectionError, setConnectionError] = useState(null);

  useEffect(() => {
    if (typeof window === "undefined" || !window.cardano) return;
    const found = SUPPORTED_WALLETS.filter(w => window.cardano[w.key]);
    setAvailableWallets(found);
  }, []);

  const connect = async walletKey => {
    if (typeof window === "undefined" || !window.cardano?.[walletKey]) return;
    setConnecting(true);
    setConnectionError(null);
    try {
      const api = await window.cardano[walletKey].enable();
      setConnectedWallet(walletKey);
      if (onConnected) {
        onConnected({ walletKey, api });
      }
    } catch (e) {
      console.error("Wallet connect error", e);
      const errorText = String(e?.info || e?.message || e || "").toLowerCase();
      if (walletKey === "eternl" && errorText.includes("dapp account")) {
        setConnectionError("Eternl needs a dApp account selected first. Open Eternl, switch to full app, then create/select a dApp account and retry.");
      } else {
        setConnectionError("Failed to connect wallet. Check extension permissions and wallet state (unlocked/account selected).");
      }
    } finally {
      setConnecting(false);
    }
  };

  if (connectedWallet) {
    return (
      <span style={{
        fontSize: "0.75rem",
        padding: "4px 10px",
        borderRadius: "999px",
        background: "rgba(34,197,94,0.16)",
        color: "#4ade80",
        border: "1px solid rgba(34,197,94,0.45)",
        display: "inline-flex",
        alignItems: "center",
        gap: "6px"
      }}>
        <span style={{
          width: "6px",
          height: "6px",
          borderRadius: "50%",
          background: "#4ade80",
          display: "inline-block"
        }}></span>
        {SUPPORTED_WALLETS.find(w => w.key === connectedWallet)?.label || connectedWallet}
      </span>
    );
  }

  return (
    <div style={{ display: "flex", flexWrap: "wrap", alignItems: "center", gap: "8px" }}>
      {availableWallets.length === 0 && (
        <div style={{ 
          fontSize: "0.7rem", 
          color: "var(--text-muted)",
          display: "flex",
          flexDirection: "column",
          gap: "4px"
        }}>
          <span>No wallets detected</span>
          <div style={{ 
            marginTop: "4px",
            padding: "6px 10px",
            background: "rgba(15,23,42,0.9)",
            borderRadius: "8px",
            border: "1px solid rgba(148,163,184,0.2)"
          }}>
            <span style={{ fontSize: "0.65rem", display: "block", marginBottom: "4px" }}>
              Install a Cardano wallet:
            </span>
            <div style={{ display: "flex", gap: "6px", flexWrap: "wrap" }}>
              <a 
                href="https://chrome.google.com/webstore/detail/nami/lpfcbjknijpeeillifnkikgncikgfhdo" 
                target="_blank" 
                rel="noopener noreferrer"
                style={{
                  fontSize: "0.65rem",
                  color: "var(--accent)",
                  textDecoration: "none"
                }}
              >
                Nami Wallet →
              </a>
              <span style={{ color: "rgba(148,163,184,0.5)" }}>|</span>
              <a 
                href="https://chrome.google.com/webstore/detail/eternl/kmhcihpebfmpgmihbkipmjlmmioameka" 
                target="_blank" 
                rel="noopener noreferrer"
                style={{
                  fontSize: "0.65rem",
                  color: "var(--accent)",
                  textDecoration: "none"
                }}
              >
                Eternl →
              </a>
            </div>
          </div>
        </div>
      )}
      {availableWallets.map(w => (
        <button
          key={w.key}
          className="btn-primary"
          style={{ fontSize: "0.75rem", padding: "6px 12px" }}
          disabled={connecting}
          onClick={() => connect(w.key)}
        >
          {connecting ? "Connecting..." : `Connect ${w.label}`}
        </button>
      ))}
      {connectionError && (
        <div
          style={{
            width: "100%",
            marginTop: "4px",
            padding: "8px 10px",
            borderRadius: "8px",
            fontSize: "0.72rem",
            background: "rgba(127, 29, 29, 0.25)",
            border: "1px solid rgba(248, 113, 113, 0.45)",
            color: "#fecaca"
          }}
        >
          {connectionError}
        </div>
      )}
    </div>
  );
}


