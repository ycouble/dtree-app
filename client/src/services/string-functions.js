export const capitalize = (str) => {
  return str.charAt(0).toUpperCase() + str.slice(1);
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
