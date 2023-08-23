interface Props {
  children: string;
}

const Title = ({ children }: Props) => {
  return <h1>{children}</h1>;
};

export default Title;
