import React from "react";

import { imgsInfo } from "../interfaces/imgsInfo";

interface Props {
  children: string;
  highlight_word: string;
  id?: string;
  //img src from frontend_dist, and alt
  imgsInfo?: imgsInfo;
}

const Title = ({ children, highlight_word, id, imgsInfo }: Props) => {
  const split_children = children.split(highlight_word);
  return (
    <>
      <h1 id={id}>
        {split_children[0]}
        <span className="highlight-word">{highlight_word}</span>
        {split_children[1]}
      </h1>
      {imgsInfo && (
        <img src={imgsInfo.img} alt={imgsInfo.alt} id="title-background" />
      )}
    </>
  );
};

export default Title;
