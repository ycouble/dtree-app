export const getNodeById = (dtree, nodeId) => {
  return dtree.nodes.find(({ id }) => id === nodeId);
};

export const getRootNode = (dtree) => {
  const rootNodeId = dtree.root_node_id;
  return getNodeById(dtree, rootNodeId);
};

export const getFormattedNode = (dtree, nodeId) => {
  const { children_id, attachements_id, ...node } = getNodeById(dtree, nodeId);

  if (node.type === "STEP" && node.description === undefined) {
    const step_title = node.title;
    const { title, ...next_node } = getFormattedNode(dtree, children_id[0]);
    return { title: step_title, question: title, ...next_node };
  }

  const children = children_id.map((id) => {
    return getNodeById(dtree, id);
  });
  const attachements = attachements_id?.map((id) => {
    return getNodeById(dtree, id);
  });
  return { ...node, children, attachements };
};

export const getChildrenID = (dtree, nodeId = dtree.root_node_id) => {
  const node = getNodeById(dtree, nodeId);
  if (node.children_id.length == 1) return node.children_id[0];
  // TODO: else error
};
