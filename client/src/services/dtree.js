export const getNodeById = (dtree, nodeId) => {
  return dtree.nodes.find(({ id }) => id === nodeId);
};

export const getRootNode = (dtree) => {
  const rootNodeId = dtree.root_node_id;
  return getNodeById(dtree, rootNodeId);
};

export const getFormattedNode = (dtree, nodeId) => {
  const node = getNodeById(dtree, nodeId);
  if (node.type === "STEP" && node.description === undefined) {
    const step_title = node.title;
    return { ...getFormattedNode(dtree, node.children_id[0]), step_title };
  }
  const children = node.children_id.map((id) => {
    return getNodeById(dtree, id);
  });
  const attachements = node.attachements_id?.map((id) => {
    return getNodeById(dtree, id);
  });
  return { ...node, children, attachements };
};

export const getChildrenID = (dtree, nodeId = dtree.root_node_id) => {
  const node = getNodeById(dtree, nodeId);
  if (node.children_id.length == 1) return node.children_id[0];
  // TODO: else error
};
