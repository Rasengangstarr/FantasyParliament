import PartyView from './pages/PartyView'
import RegionView from './pages/RegionView';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import NavIcon from './components/NavIcon';

import { ReactComponent as MapIcon} from "./resources/honeycomb.svg"
import { ReactComponent as PartiesIcon} from "./resources/public-speaker.svg"

import React, { useState, useEffect } from "react";

function App() {
  const [View, setView] = useState(0);

  let latestEventId = -1;

  function getEvents()
  {
    let eventId = 0
    console.log("IM TRYING!" + latestEventId);
    if (latestEventId >= 0)
    {
      eventId = latestEventId;
      fetch("http://127.0.0.1:5000/events?from="+eventId)
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result);
          if (result.length > 0)
          {
            console.log(result.slice(-1)[0].id);
            latestEventId = result.slice(-1)[0].id;
            result.forEach(e => {toast(e.name)});
          }
        },
        (error) => {
          console.log("Error: " + error);
        }
      );
    }
  }
useEffect(() => {
  fetch("http://127.0.0.1:5000/events/max") 
  .then(res => res.json())
    .then(
      (result) => {
        console.log("redoing");
        latestEventId = result;
      },
      (error) => {
        console.log("Error: " + error);
      });
      const interval = setInterval(() => {getEvents();}, 1000);
      //return () => clearInterval(interval);
    }, []);
    

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
      <ToastContainer position="bottom-center" newestOnTop="true" /> 
    </div>
  );
}

export default App;
