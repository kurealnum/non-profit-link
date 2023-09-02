import React from "react";

interface Props {
  children: string;
  highlight_word: string;
  id?: string;
  //img src from frontend_dist, and alt
  background_img: string[];
}

const Title = ({ children, highlight_word, id, background_img }: Props) => {
  const split_children = children.split(highlight_word);
  return (
    <>
      <h1 id={id}>
        {split_children[0]}
        <span className="highlight-word">{highlight_word}</span>
        {split_children[1]}
      </h1>
      <img
        src={background_img[0]}
        alt={background_img[1]}
        id="title-background"
      />
    </>
  );
};

export default Title;
