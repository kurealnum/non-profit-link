interface Props {
  children: string;
  highlight_word: string;
}

const Title = ({ children, highlight_word }: Props) => {
  const split_children = children.split(highlight_word);
  return (
    <h1>
      {split_children[0]}
      <span className="highlight-word">{highlight_word}</span>
      {split_children[1]}
    </h1>
  );
};

export default Title;
