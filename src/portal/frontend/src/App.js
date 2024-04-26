import './App.css';

function FileUploadBox({ id }) {
  return (
    <div className="queue-box">
      <label htmlFor={`file-upload-${id}`}>File {id}</label>
      <input id={`file-upload-${id}`} type="file" />
    </div>
  );
}

function DownloadLinkBox({ id, filename }) {
  return (
    <div className="queue-box">
      <span>File {id}: {filename}</span>
      <a href="#" download>Download</a>
      <button className="btn" onClick={() => console.log('Modify clicked', id)}>Check</button>
      <button className="btn" onClick={() => console.log('Accept clicked', id)}>Accept</button>
    </div>
  );
}

function AcceptedProposalBox({ id }) {
  return (
    <div className="queue-box">
      <label htmlFor={`file-upload-${id}`}>Approved Proposal: {id}</label>
      <input id={`file-upload-${id}`} type="file" />
    </div>
  );
}

function CustomerView() {
  return (
    <div className="CustomerView">
      <h2>Customer Side</h2>
      <p>Interested in a machine learning solution for your business? Send a proposal and we'll respond back in a jiffy!</p>
      <div className="split-view">
          <div className="left-view-inside">
            <FileUploadBox id={1}/>
          </div>
          <div className="right-view-inside">
            <AcceptedProposalBox id={1} />
          </div>
      </div>
    </div>
  );
}

function BusinessView() {
  return (
    <div className="BusinessView">
      <h2>Business Side</h2>
      <p>Here are incoming proposals!</p>
      <div className="split-view">
          <div className="left-view-inside">
            <DownloadLinkBox id={1} filename="Report1.docx" />
            <DownloadLinkBox id={2} filename="Report2.docx" />
            <DownloadLinkBox id={3} filename="Report3.docx" />
          </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className="split-view">
          <div className="left-view-outside">
            <CustomerView />
          </div>
          <div className="right-view-outside">
            <BusinessView />
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
