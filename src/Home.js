import { useState, useEffect } from "react";
import Report from './Report';
export let Val = '0'; // Set a default value

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
  const [deepComparison, setDeepComparison] = useState(false);
  const [hovered, setHovered] = useState(false);
  const text2=useState ('Deep comparison (up to 3 minutes): Analyzes the product in depth to get a quality comparison')
  const text3=useState ('Shallow comparison (up to 1.5 minutes): Shallowly evaluates the product to get a quick comparison')
    const handleMouseEnter = () => {
      setHovered(true);
    };
  
    const handleMouseLeave = () => {
      setHovered(false);
    };
    
    
  const checkEvent=()=> {
    if(validURL(url)){
      console.log(url);
      setLinks([...links, url]); // Update the state with the new URL
      setCount(count+1);
      if(links.length == 0) {
        setText('You entered ' + (count+1) +' links, enter at least 1 more link here:');
      }
      else {
        setText('You entered ' +(count+1));
      }
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
  
  const toggleComparison = () => {
    setDeepComparison(prevMode => !prevMode)
    if (deepComparison) {
      Val='0';
    } else {
      Val='1';
    }
  };

  return (
    <>
    {!showReport &&
    <div className="home">
      <div>
        <label> Comparison Mode: {deepComparison ? 'Deep' : 'Shallow'} </label>
          <label className="switch"> 
              <input
                  type="checkbox"
                  checked={deepComparison}
                  onChange={toggleComparison}
                />
              <span className="slider round"></span>
           </label>
           <div className="info-icon" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
              <span>&#9432;</span>
              {hovered && <div className="info-text">{text2}<br />{text3}</div>}
            </div>
      </div>
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
      {showReport? <Report links={links}/>:null}
    </>
  );
};

export default Home;

