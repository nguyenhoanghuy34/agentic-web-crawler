export default function GoogleButton() {
  const handleGoogleLogin = () => {
    console.log("Google login clicked");
  };

  return (
    <button className="google-btn" onClick={handleGoogleLogin}>
      Continue with Google
    </button>
  );
}