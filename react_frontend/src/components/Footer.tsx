export interface imgs_info {
  img: string;
  alt: string;
  link: string;
}

interface Props {
  items: imgs_info[];
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
