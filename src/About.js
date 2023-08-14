import './card.css'
const About = () => {

    return (
        <div className="card">
          <div className="img-avatar">
            <div className="avatar"></div>
          </div>
          <div className="card-text">
            <div className="portada">
            </div>
            <div className="title-total">
              <div className="title">Site creator</div>
              <h2>Aviv Hagag</h2>

              <div className="desc">This project is a part of my homework for a hiring opportunity. in this project, you can take 5 files and use chatGPT to compare the reviews between different products and identify differences or similarities in how the model responds to the reviews.</div>
              <div className="icons-container">
                <a href="https://www.linkedin.com/in/avivhagag/"><img src="linkedin.png" alt="Icon 1" class="icon"/></a>
                <a href="https://github.com/AvivHagag"><img src="github.png" alt="Icon 2" class="icon"/></a>
                <a href='mailto:Aviv1049@gmail.com'><img src="mail.png" alt="Icon 3" class="icon"/></a>
              </div>
            </div>
          </div>

        </div>
    );
  }
   
  export default About;
  