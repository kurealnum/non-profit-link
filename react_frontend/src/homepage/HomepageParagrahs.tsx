import Header from "../components/Header";

interface Props {
  //[0] is the paragraph, [1] is the header
  paragraphs: string[][];
}

const HomepageParagrahs = ({ paragraphs }: Props) => {
  return (
    <div className="paragraphs">
      {paragraphs.map((paragraph, index) => (
        <>
          <Header key={index}>{paragraph[1]}</Header>
          <p key={index}>{paragraph[0]}</p>
        </>
      ))}
    </div>
  );
};

export default HomepageParagrahs;
