import { Link, useHistory } from 'react-router-dom';

const Navbar = () => {
    const history = useHistory();
  
    const refreshPage = () => {
      history.push('/');
      window.location.reload();
    };

  return (
    <nav className="navbar">
      <h1 className="clickable" onClick={refreshPage}>AI Report</h1>
      <div className="links">
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
      </div>
    </nav>
  );
}
 
export default Navbar;