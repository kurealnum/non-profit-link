// package imports
import React from "react";
import ReactDOM from "react-dom/client";

// component imports
import Button from "../components/Button.tsx";

// img imports
import EditIcon from "../imgs/edit_icon.svg";

const buttons = document.getElementsByClassName("react-button");
const buttons_text = ["Edit your needs", "Edit your surplus"];

for (let i = 0; i < buttons.length; i++) {
  ReactDOM.createRoot(buttons[i]).render(
    <React.StrictMode>
      <Button imgsInfo={{ img: EditIcon, alt: "Edit button" }}>
        {buttons_text[i]}
      </Button>
    </React.StrictMode>
  );
}
