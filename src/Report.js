import { useEffect, useState } from "react";
import axios from 'axios';
import {Val} from './Home'

const Report = (links) => {
  const [data, setData] = useState('Loading....');
  const json = JSON.stringify(links);
  console.log(json);

  useEffect(() => {
    axios.post('http://127.0.0.1:5000/AI/answer',json, {
      params: {
        num: Val
      }
    })
  .then(response => {
    setData(response.data);
    console.log(response);
    return;
  })
  .catch(error => {
    console.error(error);
  });
  
  }, [links]);

  // Function to convert new lines to HTML line breaks
  const formatDataWithNewlines = (text) => {
    return { __html: text.replace(/\n/g, '<br>') };
  };

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
          {/* <img src={imageUrl} alt="Amazon product" /> */}
        </div>
        
      ) : (
        // Use dangerouslySetInnerHTML to render the data with new lines
        <p dangerouslySetInnerHTML={formatDataWithNewlines(data)}></p>
      )}
    </div>
  );  
  }
   
  export default Report;