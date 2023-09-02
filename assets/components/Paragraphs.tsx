import React from "react";

import Header from "./Header";

export interface paragraphInfo {
  paragraph: string;
  header: string;
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
    </div>
  ));
};

export default Paragraphs;
