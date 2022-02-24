import PartyNavIcon from "../components/PartyNavIcon";
import { ReactComponent as HyenaIcon } from "../resources/hyena-head.svg"
import { ReactComponent as CloakedFigureIcon } from "../resources/cloaked-figure-on-horseback.svg"
import { ReactComponent as ElysiumShadeIcon } from "../resources/elysium-shade.svg"
import { ReactComponent as NectarIcon } from "../resources/nectar.svg"
import { ReactComponent as PhilosopherBustIcon } from "../resources/philosopher-bust.svg"
import React, { useState, useEffect } from "react";

function PartyView() {
  const [Parties, fetchParties] = useState([{},{},{},{},{}]);
  const [SelectedParty, setSelectedParty] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:5000/parties")
      .then(res => res.json())
      .then(
        (result) => {
          fetchParties(result);
        },
        (error) => {
          console.log("Error: " + error);
        }
      )
  }, []);

  const selectParty = (data) => 
  {
    console.log("in");
    console.log(data);
    setSelectedParty(Parties.filter(e => e.id == data)[0]);
    console.log(SelectedParty);
  };


 
  return (
    <div>
    <div className="w-20 h-screen bg-nord-dark-1 p-1 top-0 left-0 fixed">
      <nav>
      <PartyNavIcon iconId={0} onIconClicked={selectParty} partyName={Parties[0].name} icon={<HyenaIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
      <PartyNavIcon iconId={1} onIconClicked={selectParty} partyName={Parties[1].name} icon={<CloakedFigureIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
      <PartyNavIcon iconId={2} onIconClicked={selectParty} partyName={Parties[2].name} icon={<ElysiumShadeIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
      <PartyNavIcon iconId={3} onIconClicked={selectParty} partyName={Parties[3].name} icon={<NectarIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
      <PartyNavIcon iconId={4} onIconClicked={selectParty} partyName={Parties[4].name} icon={<PhilosopherBustIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
      </nav>
    </div>
    <div className="px-24 py-4 text-3xl font-bold">
      {SelectedParty.name} 
    </div>
    </div>
  );
}

export default PartyView;
