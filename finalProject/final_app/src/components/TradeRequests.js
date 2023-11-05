import React from 'react';

function TradeRequests() {
  // Simulated trade requests data
  const tradeRequests = [
    { pilot: 'John Doe', flightNumber: 'AA123' },
    // Add more trade requests
  ];

  return (
    <div className="container mt-3">
      <h1>Trade Requests</h1>
      <table className="table">
        <thead>
          <tr>
            <th>Pilot</th>
            <th>Flight Number</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {tradeRequests.map((request, index) => (
            <tr key={index}>
              <td>{request.pilot}</td>
              <td>{request.flightNumber}</td>
              <td>
                <button className="btn btn-success">Accept</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TradeRequests;
