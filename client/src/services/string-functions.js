export const capitalize = (str) => {
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
};

export const reformatStyle = (str) => {
  const idx = str.indexOf("-");
  if (idx === -1) return str;
  return (
    str.slice(0, idx) +
    str.charAt(idx + 1).toUpperCase() +
    str.slice(idx + 2)
  ).replace("fo:", "");
};

export const getFirstWords = (str) => {
  const words = str.split(" ");
  if (words.length < 2) return str;
  if (words[0].length + words[1].length < 7) return words.slice(0, 3).join(" ");
  else return words.slice(0, 2).join(" ");
};
