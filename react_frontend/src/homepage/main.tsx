import React from "react";
import ReactDOM from "react-dom/client";

import HomepageHero from "./HomepageHero.tsx";
import Button from "../components/Button.tsx";
import HomepageParagrahs from "./HomepageParagrahs.tsx";

ReactDOM.createRoot(document.getElementById("react-homepage-hero")!).render(
  <React.StrictMode>
    <HomepageHero />
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

var paragraphs = [
  ["My paragraph", "My header"],
  ["My paragraph2", "My header2"],
];

ReactDOM.createRoot(document.getElementById("react-paragraphs")!).render(
  <React.StrictMode>
    <HomepageParagrahs paragraphs={paragraphs}></HomepageParagrahs>
  </React.StrictMode>
);
