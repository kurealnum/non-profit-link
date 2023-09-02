import React from "react";

import { imgsInfo } from "../interfaces/imgsInfo";

import Header from "./Header";

export interface paragraphInfo {
  paragraph: string;
  header: string;
  imgsInfo?: imgsInfo;
}

interface Props {
  paragraphs: paragraphInfo[];
}

const Paragraphs = ({ paragraphs }: Props) => {
  // dynamic amount of paragraphs
  return paragraphs.map((paragraph, index) => (
    // every paragraph has their own little section
    <div className="paragraph" key={index}>
      <Header key={paragraph.header}>{paragraph.header}</Header>
      <p key={index}>{paragraph.paragraph}</p>
      {/* if imgs info does exist, create an image */}
      {paragraph.imgsInfo && (
        <img src={paragraph.imgsInfo.img} alt={paragraph.imgsInfo.alt}></img>
      )}
    </div>
  ));
};

export default Paragraphs;
