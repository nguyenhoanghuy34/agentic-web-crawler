import { useState } from "react";

import "../crawler.css";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import DataPanel from "../components/DataPanel";
import ChatPanel from "../components/ChatPanel";

export default function CrawlerLayout() {

    const [collapsed, setCollapsed] = useState(false);

    return (

        <div className="crawler-page">

            <Navbar
                collapsed={collapsed}
                setCollapsed={setCollapsed}
            />

            <main
                className={
                    collapsed
                        ? "crawler-main expanded"
                        : "crawler-main"
                }
            >

                <DataPanel />

                <ChatPanel />

            </main>

            <Footer />

        </div>

    );

}