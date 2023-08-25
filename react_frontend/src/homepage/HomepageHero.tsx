//this file will be used "in line" with the homepage app in Django

import Title from "../components/Title";
import Blob from "../frontend_dist/assets/title_blob.svg";

function HomepageHero() {
  return (
    <>
      <Title
        highlight_word="non-profits"
        background_img={[Blob, "Blob image as background for the title"]}
      >
        Helping non-profits share their resources since 2023
      </Title>
    </>
  );
}

export default HomepageHero;
