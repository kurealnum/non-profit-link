interface Props {
  children: string;
}

const Button = ({ children }: Props) => {
  return <button>{children}</button>;
};

export default Button;
