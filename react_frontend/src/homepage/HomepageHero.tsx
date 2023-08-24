//this file will be used "in line" with the homepage app in Django

import Title from "../components/Title";

function HomepageHero() {
  return (
    <>
      <Title
        highlight_word="non-profits"
        background_img={[
          "/frontend_dist/assets/title_blob.svg",
          "Blob image as background for the title",
        ]}
      >
        Helping non-profits share their resources since 2023
      </Title>
    </>
  );
}

export default HomepageHero;
