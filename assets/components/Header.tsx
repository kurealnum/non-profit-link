import React from "react";

interface Props {
  children: string;
}

const Header = ({ children }: Props) => {
  return <h1>{children}</h1>;
};

export default Header;
