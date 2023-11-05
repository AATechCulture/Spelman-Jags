import React from 'react';

function Schedule() {
  // Simulated schedule data
  const schedule = [
    { flightNumber: 'AA123', date: '2023-12-15', destination: 'New York' },
    // Add more schedule entries
  ];

  return (
    <div className="container mt-3">
      <h1>My Schedule</h1>
      <table className="table">
        <thead>
          <tr>
            <th>Flight Number</th>
            <th>Date</th>
            <th>Destination</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {schedule.map((flight, index) => (
            <tr key={index}>
              <td>{flight.flightNumber}</td>
              <td>{flight.date}</td>
              <td>{flight.destination}</td>
              <td>
                <button className="btn btn-primary">Trade</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Schedule;
