import "../crawler.css";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import DataPanel from "../components/DataPanel";
import ChatPanel from "../components/ChatPanel";

export default function CrawlerLayout() {
    return (
        <div className="crawler-page">

            <Navbar />

            <div className="crawler-layout">

                <main className="crawler-main">

                    <DataPanel />

                    <ChatPanel />

                </main>

                <Footer />

            </div>

        </div>
    );
}