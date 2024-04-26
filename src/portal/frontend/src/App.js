import './App.css';
import React, { useState } from 'react';

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
      <button className="btn" onClick={() => {
          console.log('TODO: Go to details of id', id)
        }}>Details</button>
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

function ListOfIncomingProposals(setCurrentReport) {
  return (
    <div>
    <p>Here are incoming proposals!</p>
    <div className="split-view">
    <div className="left-view-inside">
      <DownloadLinkBox id={1} filename="Report1.docx" setCurrentReport={setCurrentReport} />
      <DownloadLinkBox id={2} filename="Report2.docx" setCurrentReport={setCurrentReport}/>
      <DownloadLinkBox id={3} filename="Report3.docx" setCurrentReport={setCurrentReport}/>
    </div>
    </div>
    </div>
  );
}

function ShowIncomingProposal({reportNumber}) {
  // TODO: get data from the reportNumber
  return (
    <div>
      {reportNumber}
      <button className="btn" onClick={() => {
          console.log("TODO: go to business view")
        }}>Go back</button>
      <button className="btn btn-success" onClick={() => {
          console.log("TODO: approve it and go to business view")
        }}>Approve</button>

    </div>
  )
}

function BusinessView() {
  const [currentReport, setCurrentReport] = useState(0);

  return (
    <div className="BusinessView">
      <h2>Business Side</h2>
      // TODO: make routing maybe
      {currentReport == 0 ? <ListOfIncomingProposals /> : <ShowIncomingProposal reportNumber={currentReport}/>}
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
