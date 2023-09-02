import React from "react";
import { imgsInfo } from "../interfaces/imgsInfo";

interface Props {
  items: imgsInfo[];
}

const Footer = ({ items }: Props) => {
  return (
    <>
      {/* map our imgs out for our footer */}
      {items.map((ial, index) => (
        <a key={index} href={ial.link}>
          <img src={ial.img} alt={ial.alt} />
        </a>
      ))}
    </>
  );
};

export default Footer;
