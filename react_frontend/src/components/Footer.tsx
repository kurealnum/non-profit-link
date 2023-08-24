interface Props {
  //imgs are [0], alts are [1], and links are [2]
  imgs_alts_links: string[][];
}

const Footer = ({ imgs_alts_links }: Props) => {
  return (
    <>
      {imgs_alts_links.map((ial, index) => (
        <a key={index} href={ial[2]}>
          <img src={ial[0]} alt={ial[1]} />
        </a>
      ))}
    </>
  );
};

export default Footer;
