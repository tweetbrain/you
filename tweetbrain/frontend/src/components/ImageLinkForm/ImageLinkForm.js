import React from 'react';
import './ImageLinkForm.css';


const ImageLinkForm = ({value, handleSubmit, handleChange}) => {
    return(
        <div>
            <p className="f2">
                {'Insert your Twitter handle for me to predict your theme song!'}
            </p>
            <form onSubmit={handleSubmit}>
              <div className="center">
                  <div className="text_submit center pa3 br2 shadow-5">
                      <input className="f4 pa2 w-70 center" type="text" value={value} onChange={handleChange}  />
                      <button className="w-30 grow f4 link ph3 pv2 dib white" style={{background:'red'}}>Submit</button>
                  </div>
              </div>
            </form>
        </div>
    ) 
}
export default ImageLinkForm;