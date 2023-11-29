import React from "react";

import { imgsInfo } from "../interfaces/imgsInfo";

interface Props {
  children: string;
  imgsInfo?: imgsInfo;
}

const Button = ({ children, imgsInfo }: Props) => {
  return (
    <div className="button">
      <button>{children}</button>
      {/* only add an image if imgsInfo exists */}
      {imgsInfo && <img src={imgsInfo.img} alt={imgsInfo.alt}></img>}
    </div>
  );
};

export default Button;
