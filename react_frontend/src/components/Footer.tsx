export interface imgsInfo {
  img: string;
  alt: string;
  link: string;
}

interface Props {
  items: imgsInfo[];
}

const Footer = ({ items }: Props) => {
  return (
    <>
      {items.map((ial, index) => (
        <a key={index} href={ial.link}>
          <img src={ial.img} alt={ial.alt} />
        </a>
      ))}
    </>
  );
};

export default Footer;
