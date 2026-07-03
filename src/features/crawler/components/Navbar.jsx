export default function Navbar({
    collapsed,
    setCollapsed
}) {

    const navItems = [
        "Dashboard",
        "Crawler",
        "History",
        "Settings"
    ];

    return (

        <header
            className={
                collapsed
                    ? "crawler-navbar collapsed"
                    : "crawler-navbar"
            }
        >

            <div className="crawler-navbar-content">

                <div className="crawler-logo">

                    CrawlAI

                </div>

                <nav className="crawler-nav">

                    {navItems.map(item => (

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

            </div>

            <div
                className="navbar-toggle"
                onClick={() => setCollapsed(!collapsed)}
            >

                {collapsed ? "▼" : "▲"}

            </div>

        </header>

    );

}