import React, { useState, useEffect } from "react";
function RegionView() {
  const [Regions, fetchRegions] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5000/realms")
      .then(res => res.json())
      .then(
        (result) => {
          fetchRegions(result.sort((a,b) => a.id - b.id));
        },
        (error) => {
          console.log("Error: " + error);
        }
      )
  }, []);
  
  return (
    <div className="main ml-12 mt-12 w-96">
      <div className="container">
        {Regions.map((r,i) => (
          r.type === 0 && <div className="bg-nord-green pt-3 pl-2" key={i}> D </div> || 
          r.type === 1 && <div className="bg-nord-red pt-3 pl-2" key={i}> P </div> || 
          r.type === 2 && <div className="bg-nord-yellow pt-3 pl-2" key={i}> F </div> || 
          r.type === 3 && <div className="bg-nord-purple pt-3 pl-2" key={i}> M </div>
        ))}
      </div>
    </div>
  );
}

export default RegionView;
