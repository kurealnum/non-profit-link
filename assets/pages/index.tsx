import React from "react";
import ReactDOM from "react-dom/client";

import Vite from "../imgs/vite.svg";

import HomepageHero from "../components/MainTitle.tsx";
import Button from "../components/Button.tsx";
import Paragraphs, { paragraphInfo } from "../components/Paragraphs.tsx";
import Footer, { imgsInfo } from "../components/Footer.tsx";

ReactDOM.createRoot(document.getElementById("react-homepage-hero")!).render(
  <React.StrictMode>
    <HomepageHero />
  </React.StrictMode>
);

//render for homepage-search
const buttons = document.getElementsByClassName("homepage-search");
const buttons_titles = ["Search non-profits", "Search items"];

const paragraphs: paragraphInfo[] = [
  { header: "My First Header", paragraph: "My First Paragraph" },
  { header: "My Second Header", paragraph: "My Second Paragraph" },
];

for (let i = 0; i < buttons.length; i++) {
  ReactDOM.createRoot(buttons[i]!).render(
    <React.StrictMode>
      <Button>{buttons_titles[i]}</Button>
    </React.StrictMode>
  );
}

//render for paragraphs
ReactDOM.createRoot(document.getElementById("react-paragraphs")!).render(
  <React.StrictMode>
    <Paragraphs paragraphs={paragraphs}></Paragraphs>
  </React.StrictMode>
);

//render for footer
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
