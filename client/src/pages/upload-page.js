import React, { useState } from "react";

import { Button, RedirectButton } from "../components";
import css from "./css/no-match-page.module.css";

import { upload } from "../services/api";

const UploadPage = () => {
  const [selectedFile, setSelectedFile] = useState();

  const changeHandler = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmission = () => {
    const sendFile = async () => {
      const body = new FormData();
      body.append("file", selectedFile);

      const results = await upload(body);

      console.log(results);
    };

    sendFile();
  };

  return (
    <div className={css.page}>
      <input type="file" name="file" onChange={changeHandler} />
      {selectedFile ? (
        <div>
          <p>Filename: {selectedFile.name}</p>
          <p>Filetype: {selectedFile.type}</p>
          <p>Size in bytes: {selectedFile.size}</p>
          <p>
            lastModifiedDate:{" "}
            {selectedFile.lastModifiedDate.toLocaleDateString()}
          </p>
        </div>
      ) : (
        <p>Select a file to show details</p>
      )}
      <Button text={"Submit"} onClick={handleSubmission} />
      <RedirectButton text={"Logout"} type={"logout"} />
    </div>
  );
};

export default UploadPage;
