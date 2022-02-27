import NavIcon from "../components/NavIcon";
import PartyMemberCard from "../components/PartyMemberCard";

import { ReactComponent as HyenaIcon } from "../resources/hyena-head.svg"
import { ReactComponent as CloakedFigureIcon } from "../resources/cloaked-figure-on-horseback.svg"
import { ReactComponent as ElysiumShadeIcon } from "../resources/elysium-shade.svg"
import { ReactComponent as NectarIcon } from "../resources/nectar.svg"
import { ReactComponent as PhilosopherBustIcon } from "../resources/philosopher-bust.svg"
import React, { useState, useEffect } from "react";

function PartyView() {
  const [Parties, fetchParties] = useState([{},{},{},{},{}]);
  const [SelectedParty, setSelectedParty] = useState({members:[]});

  useEffect(() => {
    fetch("http://127.0.0.1:5000/parties/detailed")
      .then(res => res.json())
      .then(
        (result) => {
          result.map(p => {
            let stanceTotal = p.stances.war+p.stances.nature+p.stances.industry+p.stances.magic 
            p.warLeft = 0
            p.warWidth = (p.stances.war / stanceTotal) * 100;
            p.magicLeft = p.warWidth;
            p.magicWidth = (p.stances.magic / stanceTotal) * 100;
            p.natureLeft = p.magicLeft + p.magicWidth;
            p.natureWidth = (p.stances.nature / stanceTotal) * 100;
            p.industryLeft = p.natureLeft + p.natureWidth;
            p.industryWidth = (p.stances.industry / stanceTotal) * 100;
            return p;
          });
          result = result.sort((a,b) => a.id - b.id);
          fetchParties(result);
          setSelectedParty(result[0]);

        },
        (error) => {
          console.log("Error: " + error);
        }
      )
  }, []);

  const selectParty = (data) => 
  {
    setSelectedParty(Parties.filter(e => e.id === data)[0]);
  };


 
  return (
    <div>
      <div className="w-96 left-40 h-fit px-4 py-4 absolute">
        <div className="text-2xl font-bold">
          {SelectedParty.name} 
        </div>
         <div className="m-1 py-5">
                <div className="rounded-full h-5 relative">
                    <div className="bg-nord-red h-5 absolute" style={{left: SelectedParty.warLeft+"%", width: SelectedParty.warWidth+"%"}}/>
                    <div className="bg-nord-frost-3 h-5 absolute" style={{left: SelectedParty.magicLeft+"%", width: SelectedParty.magicWidth+"%"}}/>
                    <div className="bg-nord-green h-5 absolute" style={{left: SelectedParty.natureLeft+"%", width: SelectedParty.natureWidth+"%"}}/>
                    <div className="bg-nord-yellow h-5 absolute" style={{left: SelectedParty.industryLeft+"%", width: SelectedParty.industryWidth+"%"}}/>
                </div>
          </div>
          <div >
          {SelectedParty.members.sort((a,b) => b.job - a.job).map((m,i) => (
            <PartyMemberCard key={i} member={m} />
          ))}
          </div>
      </div>
      <div className="w-20 left-20 bg-nord-dark-1 p-1 h-screen top-0 fixed ">
        <nav>
        <NavIcon iconId={0} onIconClicked={selectParty} name={Parties[0].name} icon={<HyenaIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
        <NavIcon iconId={1} onIconClicked={selectParty} name={Parties[1].name} icon={<CloakedFigureIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
        <NavIcon iconId={2} onIconClicked={selectParty} name={Parties[2].name} icon={<ElysiumShadeIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
        <NavIcon iconId={3} onIconClicked={selectParty} name={Parties[3].name} icon={<NectarIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
        <NavIcon iconId={4} onIconClicked={selectParty} name={Parties[4].name} icon={<PhilosopherBustIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
        </nav>
      </div>

    </div>
  );
}

export default PartyView;
