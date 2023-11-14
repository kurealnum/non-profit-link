// package imports
import React from "react";
import ReactDOM from "react-dom/client";

// component imports
import Button from "../components/Button.tsx";
import Header from "../components/Header.tsx";

const left_of_dashboard_info = JSON.parse(
  document.getElementById("org")!.textContent!
);

ReactDOM.createRoot(document.getElementById("react-dashboard")!).render(
  <React.StrictMode>
    <section id="left-of-dashboard">
      <Header>{left_of_dashboard_info["org-name"] + "'s dashboard"}</Header>
      <p>{left_of_dashboard_info["org-desc"]}</p>
      <Button>Temporary</Button>
    </section>
    <section id="mid-of-dashboard"></section>
    <section id="right-of-dashboard"></section>
  </React.StrictMode>
);
