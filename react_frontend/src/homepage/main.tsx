import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import Button from "../components/Button.tsx";

ReactDOM.createRoot(document.getElementById("react-homepage-hero")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

var buttons = document.getElementsByClassName("react-button");
var buttons_titles = ["Search non-profits", "Search items"];

for (let i = 0; i < buttons.length; i++) {
  ReactDOM.createRoot(buttons[i]!).render(
    <React.StrictMode>
      <Button>{buttons_titles[i]}</Button>
    </React.StrictMode>
  );
}
