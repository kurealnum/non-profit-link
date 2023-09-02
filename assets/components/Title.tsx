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
        {/* this is how we highlight a certain word */}
        {split_children[0]}
        <span className="highlight-word">{highlight_word}</span>
        {split_children[1]}
      </h1>
      {/* only add an image if imgsInfo exists */}
      {imgsInfo && (
        <img src={imgsInfo.img} alt={imgsInfo.alt} id="title-background" />
      )}
    </>
  );
};

export default Title;
