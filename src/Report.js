import { useEffect, useState } from "react";
import axios from 'axios';


const Report = (links) => {
  const [data, setData] = useState('Loading....');
  const json = JSON.stringify(links);
  console.log(json);

  useEffect(() => {
    axios.post('http://127.0.0.1:5000/AI/answer', json)
  .then(response => {
    // Handle the response from the server
    setData(response.data);
    console.log(response);
    return;
  })
  .catch(error => {
    // Handle any errors that occurred during the request
    console.error(error);
  });
  }, [links]);


    return (
      <div className="Report">
        <h2>Report</h2>
        <br />
        {data === 'Loading....' ? (
        <p>{data}
        <div className="loading-spinner">
          <div className="spinner">
          </div>
        </div>
        </p>
      ) : (
        <p>{data}</p>
      )}
      </div>
    );
  }
   
  export default Report;