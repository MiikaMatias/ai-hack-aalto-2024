function AcceptedProposalBox({ id }) {
    return (
      <div className="queue-box">
        <label htmlFor={`file-upload-${id}`}>Approved Proposal: {id}</label>
        <button className="btn" onClick={() => {
            console.log('TODO: Download the the sent file')
          }}>Download sent file</button>
        <button className="btn" onClick={() => {
            console.log('TODO: Download the accepted proposal')
          }}>Download accepted proposal</button>
      </div>
    );
  }

export default AcceptedProposalBox;