import { useState } from "react";

export default function ChatPanel() {

    const [model, setModel] = useState("gemini");

    return (

        <section className="chat-panel">

            <div className="panel-header">

                <div className="model-toggle">

                    <button
                        className={
                            model === "gemini"
                                ? "model-btn active"
                                : "model-btn"
                        }
                        onClick={() => setModel("gemini")}
                    >
                        Gemini Model
                    </button>

                    <button
                        className={
                            model === "openai"
                                ? "model-btn active"
                                : "model-btn"
                        }
                        onClick={() => setModel("openai")}
                    >
                        OpenAI Model
                    </button>

                </div>

            </div>

            <div className="panel-body">

                <h3>Đây là khung chat</h3>

                <p>

                    Model hiện tại:

                    <br /><br />

                    <strong>

                        {model === "gemini"
                            ? "Gemini Model"
                            : "OpenAI Model"}

                    </strong>

                </p>

            </div>

        </section>

    );

}