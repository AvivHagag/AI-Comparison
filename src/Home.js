import { useState, useEffect } from "react";
import Report from './Report';


const Home = () => {
  const [count,setCount] =useState(0);
  const [text,setText] = useState('Enter links here:');
  const [url, setUrl] = useState('');
  const [links, setLinks] = useState([]);
  const [showReport,setShowReport]= useState(false);
  const validURL=(str)=> {
      // Regular expression pattern for URL validation
      let urlPattern = /^(https?:\/\/)?[\w.-]+\.[a-zA-Z]{2,}(\/\S*)?$/;
      // Test if the input matches the URL pattern
      return urlPattern.test(url);
    }
    
  const checkEvent=()=> {
    if(validURL(url)){
      console.log(url);
      setLinks([...links, url]); // Update the state with the new URL
      setCount(count+1);
      setText('You entered ' + (count+1) +' links, enter at least 1 more link here:');
      setUrl(''); // Reset the url state to clear the input
    }
    else {
      setText("Invalid link ! please enter a new one");
      setUrl(''); // Reset the url state to clear the input
    }
  }

  const inputUrl=(e) => {
    setUrl(e.target.value)
  }

  const checkSumbit=()=> {
    if (links.length >= 2) {
      setShowReport(true); // Set the state to show the Report component
    } else {
      setText('Insert at least 2 links.');
    }
  }

  return (
    <>
    {!showReport &&
    <div className="home">
      <h2>Please insert at least 2 links to run the AI</h2>
      <label>{text}</label>
      <br />
      <input
        type="text"
        required
        value={url}
        onChange={(e) => inputUrl(e)}
      />
      <button className="SearchBtn" onClick={checkEvent}>add</button>
      <br />
      {count >= 2 && (
        <button className="Sumbit" onClick={checkSumbit}>
          Submit
        </button>
      )}
      </div>
    }
      {showReport? <Report links={links} />:null}
    </>
  );
};


export default Home;

