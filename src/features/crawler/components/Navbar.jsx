export default function Navbar() {
    const navItems = [
        "Dashboard",
        "Crawler",
        "History",
        "Settings"
    ];

    return (
        <header className="crawler-navbar">

            <div className="crawler-logo">
                CrawlAI
            </div>

            <nav className="crawler-nav">
                {navItems.map((item) => (
                    <button
                        key={item}
                        className="crawler-nav-item"
                    >
                        {item}
                    </button>
                ))}
            </nav>

            <div className="crawler-user">

                <div className="crawler-avatar">
                    HH
                </div>

            </div>

        </header>
    );
}