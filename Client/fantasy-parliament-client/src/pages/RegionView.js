import React, { useState, useEffect } from "react";

function RegionView() {
  const [Regions, fetchRegions] = useState([]);
  const [HoveredRegion, hoverOverRegion] = useState({racePops: {}});
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
    <div className="absolute ml-16 left-20 ">
    <div className="fixed bg-nord-dark-4 text-nord-light-1 left-40 ml-96 mt-20">
      <div className="text-3xl font-bold">
      {HoveredRegion.name}
      </div>
      <div className="text-l font-bold">{HoveredRegion.type == 0 && "Wasteland" || HoveredRegion.type == 1 && "Plains" || HoveredRegion.type == 2 && "Forest" || HoveredRegion.type == 3 && "Mountains"}</div>
      <div className="text-l">Population: {HoveredRegion.population} </div>
      <div className="text-l">Orcs: {Math.round(HoveredRegion.racePops.orcPop*100)}% </div>
      <div className="text-l">Humans: {Math.round(HoveredRegion.racePops.humanPop*100)}% </div>
      <div className="text-l">Dwarves: {Math.round(HoveredRegion.racePops.dwarfPop*100)}% </div>
      <div className="text-l">Elves: {Math.round(HoveredRegion.racePops.elfPop*100)}% </div>
    </div>
    
    <div className="text-xl font-bold">Region Mode</div> 
    <div className="text-l">
       <span className="text-nord-yellow font-bold">Desert &nbsp;</span>
       <span className="text-nord-green font-bold">Plains &nbsp;</span>
       <span className="text-nord-frost-1 font-bold">Forest &nbsp;</span>
       <span className="text-nord-purple font-bold">Mountains &nbsp;</span>
    </div>
    
    <div className="pt-2 main w-96">
      <div className="container">
        {Regions.map((r,i) => (
          r.type === 0 && <div onMouseOver={() => hoverOverRegion(r)} className="bg-nord-yellow hover:bg-nord-light-3 pt-3 pl-2" key={i}>  </div> || 
          r.type === 1 && <div onMouseOver={() => hoverOverRegion(r)} className="bg-nord-green pt-3 pl-2 hover:bg-nord-light-3" key={i}>  </div> || 
          r.type === 2 && <div onMouseOver={() => hoverOverRegion(r)} className="bg-nord-frost-1 pt-3 pl-2 hover:bg-nord-light-3" key={i}>  </div> || 
          r.type === 3 && <div onMouseOver={() => hoverOverRegion(r)} className="bg-nord-purple pt-3 pl-2 hover:bg-nord-light-3" key={i}>  </div>
        ))}
      </div>
    </div>


    </div>
  );
}

export default RegionView;
