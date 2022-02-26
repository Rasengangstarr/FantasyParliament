import PartyView from './pages/PartyView'
import RegionView from './pages/RegionView';

import NavIcon from './components/NavIcon';

import { ReactComponent as MapIcon} from "./resources/honeycomb.svg"
import { ReactComponent as PartiesIcon} from "./resources/public-speaker.svg"

import React, { useState } from "react";

function App() {
  const [View, setView] = useState(0);

  return (
  <div>
    <div className="fixed bg-nord-dark-1 w-20 h-screen border-r-2 border-nord-dark-2 top-0 left-0">
    </div>
  <div className="top-0 left-20 ">
    {(View == 0 && <PartyView className="on-" />) || (View == 1 && <RegionView />) }
  </div>
      <div className="w-20 bg-nord-dark-1 p-1 h-screen top-0 fixed">
        <nav>
          <NavIcon onIconClicked={() => setView(0)} name="Party Viewer" icon={<PartiesIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
          <NavIcon onIconClicked={() => setView(1)} name="Map Viewer" icon={<MapIcon className="block m-auto fill-nord-frost-2 group-hover:transition-all group-hover:fill-nord-red" /> }/> 
        </nav>
      </div>
  </div>
  );
}

export default App;
