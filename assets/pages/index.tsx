// package imports
import React from "react";
import ReactDOM from "react-dom/client";

// img imports
import SearchButton from "../imgs/search_button_icon.svg";
import TitleBlobSVG from "../imgs/title_blob.svg";
import FirstParagraphBlob from "../imgs/first_paragraph_blob.svg";
import SecondParagraphBlob from "../imgs/second_paragraph_blob.svg";
import EmailIcon from "../imgs/email_icon.svg";
import BrowserIcon from "../imgs/browser_window.svg";
import GithubIcon from "../imgs/github_icon.svg";
import QuestionIcon from "../imgs/question_mark_icon.svg";

// component imports
import { imgsInfo } from "../interfaces/imgsInfo.ts";
import MainTitle from "../components/MainTitle.tsx";
import Button from "../components/Button.tsx";
import Paragraphs, { paragraphInfo } from "../components/Paragraphs.tsx";
import Footer from "../components/Footer.tsx";

//hero info
const hero_imgs_info: imgsInfo = {
  img: TitleBlobSVG,
  alt: "Title blob SVG",
};

// render for the hero
ReactDOM.createRoot(document.getElementById("react-homepage-hero")!).render(
  <React.StrictMode>
    <MainTitle imgsInfo={hero_imgs_info} />
  </React.StrictMode>
);

//render for homepage-search
const buttons = document.getElementsByClassName("homepage-search");
const buttons_info = ["Search non-profits", "Search items"];

// dynamically generate buttons
for (let i = 0; i < buttons.length; i++) {
  ReactDOM.createRoot(buttons[i]!).render(
    <React.StrictMode>
      <Button imgsInfo={{ img: SearchButton, alt: "search" }}>
        {buttons_info[i]}
      </Button>
    </React.StrictMode>
  );
}

//render for paragraphs
const paragraphs: paragraphInfo[] = [
  {
    header: "My First Header",
    paragraph:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    imgsInfo: {
      img: FirstParagraphBlob,
      alt: "Decorative blue blob on paragraph",
    },
  },
  {
    header: "My Second Header",
    paragraph:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    imgsInfo: {
      img: SecondParagraphBlob,
      alt: "Decorative blue blob on paragraph",
    },
  },
];

ReactDOM.createRoot(document.getElementById("react-paragraphs")!).render(
  <React.StrictMode>
    <Paragraphs paragraphs={paragraphs}></Paragraphs>
  </React.StrictMode>
);

//render for footer
const imgs_info_input: imgsInfo[] = [
  {
    img: EmailIcon,
    alt: "An email icon",
    link: "oscar.gaske.cs@gmail.com",
  },
  {
    img: BrowserIcon,
    alt: "A browser icon",
    link: "IFORGETWHERETHISGOES",
  },
  {
    img: GithubIcon,
    alt: "A github icon",
    link: "https://github.com/kurealnum/non-profit-link",
  },
  {
    img: QuestionIcon,
    alt: "A question mark icon",
    link: "IFORGETWHERETHISGOES",
  },
];

ReactDOM.createRoot(document.getElementsByTagName("footer")[0]).render(
  <React.StrictMode>
    <Footer items={imgs_info_input}></Footer>
  </React.StrictMode>
);
