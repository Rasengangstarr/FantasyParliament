import React, { useState } from "react";

function PartyView(props) {
  return (
    <div>
      <h1 className="text-3xl font-bold my-2 mx-2">Party View</h1>
      <nav>
          <div>
            <button className="bg-slate-300 text-1xl text-black px-1 m-2 w-56">
              Brown Cobra Association
            </button>
          </div>
          <div>
            <button className='bg-slate-300 text-1xl text-black px-1 mx-2 w-56'>
              Another Party 
            </button>
          </div>
      </nav>
    </div>
  );
}

export default PartyView;
