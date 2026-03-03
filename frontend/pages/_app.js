import "../styles/globals.css";

export default function App({ Component, pageProps }) {
  return (
    <>
      <div className="glow-strip" />
      <Component {...pageProps} />
    </>
  );
}


