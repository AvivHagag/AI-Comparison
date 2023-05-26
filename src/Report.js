import { useEffect, useState } from "react";
import axios from 'axios';


const Report = (links) => {
  const [data, setData] = useState('Loading....');
  const json = JSON.stringify(links);
  console.log(json);

  useEffect(() => {
    axios.post('http://127.0.0.1:5000/AI/answer', json)
  .then(response => {
    setData(response.data);
    console.log(response);
    return;
  })
  .catch(error => {
    console.error(error);
  });
  }, [links]);


  return (
    <div className="Report">
      <h2>Report</h2>
      <br />
      {data === 'Loading....' ? (
        <div>
          <p>{data}</p>
          <div className="loading-spinner">
            <div className="spinner"></div>
          </div>
        </div>
      ) : (
        <p>{data}</p>
      )}
    </div>
  );  
  }
   
  export default Report;