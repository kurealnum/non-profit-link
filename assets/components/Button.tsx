import React from "react";

import { imgsInfo } from "../interfaces/imgsInfo";

interface Props {
  children: string;
  imgsInfo?: imgsInfo;
}

const Button = ({ children, imgsInfo }: Props) => {
  return (
    <>
      <button>{children}</button>
      {imgsInfo && <img src={imgsInfo.img} alt={imgsInfo.alt}></img>}
    </>
  );
};

export default Button;
