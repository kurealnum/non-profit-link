//this file will be used "in line" with the homepage app in Django
import React from "react";

import Title from "./Title";

import { imgsInfo } from "../interfaces/imgsInfo";

interface Props {
  imgsInfo?: imgsInfo;
}

function HomepageHero({ imgsInfo }: Props) {
  return (
    <>
      {/* utilizing a pre-existing Title component*/}
      <Title highlight_word="non-profits" id="hero-title" imgsInfo={imgsInfo}>
        Helping non-profits share their resources since 2023
      </Title>
    </>
  );
}

export default HomepageHero;
