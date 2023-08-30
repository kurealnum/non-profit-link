import React from "react";

import Header from "./Header";

export interface paragraphInfo {
  paragraph: string;
  header: string;
}

interface Props {
  //[0] is the paragraph, [1] is the header
  paragraphs: paragraphInfo[];
}

const HomepageParagrahs = ({ paragraphs }: Props) => {
  return (
    <div className="paragraphs">
      {paragraphs.map((paragraph, index) => (
        <>
          <Header key={index}>{paragraph.header}</Header>
          <p key={index}>{paragraph.paragraph}</p>
        </>
      ))}
    </div>
  );
};

export default HomepageParagrahs;
