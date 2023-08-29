import React from "react";
import ReactDOM from "react-dom/client";

import Vite from "imgs/vite.svg";

import HomepageHero from "./HomepageHero.tsx";
import Button from "./components/Button.tsx";
import HomepageParagrahs, { paragraphInfo } from "./HomepageParagrahs.tsx";
import Footer, { imgsInfo } from "../components/Footer.tsx";

ReactDOM.createRoot(document.getElementById("react-homepage-hero")!).render(
  <React.StrictMode>
    <HomepageHero />
  </React.StrictMode>
);

const buttons = document.getElementsByClassName("react-button");
const buttons_titles = ["Search non-profits", "Search items"];

for (let i = 0; i < buttons.length; i++) {
  ReactDOM.createRoot(buttons[i]!).render(
    <React.StrictMode>
      <Button>{buttons_titles[i]}</Button>
    </React.StrictMode>
  );
}

const paragraphs: paragraphInfo[] = [
  { header: "My First Header", paragraph: "My First Paragraph" },
  { header: "My Second Header", paragraph: "My Second Paragraph" },
];

ReactDOM.createRoot(document.getElementById("react-paragraphs")!).render(
  <React.StrictMode>
    <HomepageParagrahs paragraphs={paragraphs}></HomepageParagrahs>
  </React.StrictMode>
);

//just demos for now, remember that the img url needs to be the location of the img in the dist folder
const imgs_info_input: imgsInfo[] = [
  {
    img: Vite,
    alt: "A react image",
    link: "https://google.com",
  },
];

ReactDOM.createRoot(document.getElementsByTagName("footer")[0]).render(
  <React.StrictMode>
    <Footer items={imgs_info_input}></Footer>
  </React.StrictMode>
);
