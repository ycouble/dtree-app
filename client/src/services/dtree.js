export const getNodeById = (dtree, nodeId) => {
  return dtree?.nodes?.find(({ id }) => id === nodeId);
};

export const getRootNode = (dtree) => {
  const rootNodeId = dtree.root_node_id;
  return getNodeById(dtree, rootNodeId);
};

export const getFormattedNode = (dtree, nodeId) => {
  const { children_id, attachements_id, ...node } = getNodeById(dtree, nodeId);

  if (node.type === "STEP" && node.description === undefined) {
    const { title, type, children } = getFormattedNode(dtree, children_id[0]);
    return { id: node.id, title: node.title, question: title, children, type };
  }

  const children = children_id.map((id) => {
    return getNodeById(dtree, id);
  });
  const attachements = attachements_id?.map((id) => {
    return getNodeById(dtree, id);
  });
  return { ...node, children, attachements };
};
