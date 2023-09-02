import React from "react";

import { imgsInfo } from "../interfaces/imgsInfo";

interface Props {
  children: string;
  imgsInfo?: imgsInfo;
}

const Button = ({ children, imgsInfo }: Props) => {
  return (
    <div className="search-button">
      <button>{children}</button>
      {imgsInfo && <img src={imgsInfo.img} alt={imgsInfo.alt}></img>}
    </div>
  );
};

export default Button;
