function FileUploadBox({ id }) {
    const [file, setFile] = useState(null);

    const onFileChange = event => {
      setFile(event.target.files[0]);
    };
  
    const onFileUpload = () => {
      const formData = new FormData();
      
      if (file) {
        formData.append("file", file);
      }
  
      console.log(file);
  
      fetch('http://localhost:5000/upload_proposal', {
        method: 'POST',
        body: formData,
      })
      .then(response => response.json())
      .then(data => {
        console.log("Success:", data);
      })
      .catch(error => {
        console.error("Error:", error);
      });
    };
  
    return (
      <div>
        <h1>Upload a Proposal</h1>
        <input type="file" onChange={onFileChange} />
        <button onClick={onFileUpload}>
          Upload!
        </button>
      </div>
    );
  }
  

export default FileUploadBox;