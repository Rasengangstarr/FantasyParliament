import { ReactComponent as OrcFace} from "../resources/orc-head.svg"
import { ReactComponent as ElfFace} from "../resources/woman-elf-face.svg"
import { ReactComponent as HumanFace} from "../resources/pig-face.svg"
import { ReactComponent as DwarfFace} from "../resources/dwarf-helmet.svg" 

import { ReactComponent as Warrior} from "../resources/sword-wound.svg"
import { ReactComponent as Mage} from "../resources/wizard-staff.svg"
import { ReactComponent as Craftsman} from "../resources/gear-hammer.svg"
import { ReactComponent as Ranger} from "../resources/oak-leaf.svg" 

import React, { useState, useEffect } from "react";

function PartyMemberCard(props) {
    const [StancePercentages, storeStancePercentages] = useState({war:{},
         industry:{},
         magic:{},
         nature:{}
        });

    useEffect(() => {
        let totalStances = props.member.stances.magic+props.member.stances.industry+props.member.stances.war+props.member.stances.nature;
        let stancesP = {};
        stancesP.war = {left: 0, width: (props.member.stances.war/totalStances)*100};
        stancesP.magic = {left: stancesP.war.width, width: (props.member.stances.magic/totalStances)*100};
        stancesP.nature = {left: stancesP.magic.left + stancesP.magic.width, width: (props.member.stances.nature/totalStances)*100};
        stancesP.industry = {left: stancesP.nature.left + stancesP.nature.width, width: (props.member.stances.industry/totalStances)*100};
        storeStancePercentages(stancesP);
    }, [props.member, props.member.stances]);
    return(
        <div className="m-1 w-42 border-nord-dark-1 border-solid border-2">
            {props.member.race === 1 && <ElfFace className="fill-nord-light-3 inline mx-1" />}
            {props.member.race === 2 && <OrcFace className="fill-nord-light-3 inline mx-1" />}
            {props.member.race === 3 && <DwarfFace className="fill-nord-light-3 inline mx-1" />}
            {props.member.race === 4 && <HumanFace className="fill-nord-light-3 inline mx-1" />}
            
            {props.member.background === 1 && <Warrior className="fill-nord-light-3 inline mx-1" />}
            {props.member.background === 2 && <Mage className="fill-nord-light-3 inline mx-1" />}
            {props.member.background === 3 && <Craftsman className="fill-nord-light-3 inline mx-1" />}
            {props.member.background === 4 && <Ranger className="fill-nord-light-3 inline mx-1" />}
            <div className="inline pl-1">
                {props.member.name}
            </div>
            <div className="m-1">
                <div className="rounded-full h-2.5 relative">
                    <div className="bg-nord-red h-2.5 absolute" style={{left:StancePercentages.war.left+"%", width: StancePercentages.war.width+"%"}}/>
                    <div className="bg-nord-frost-3 h-2.5 absolute" style={{left:StancePercentages.magic.left+"%", width: StancePercentages.magic.width+"%"}}/>
                    <div className="bg-nord-green h-2.5 absolute" style={{left:StancePercentages.nature.left+"%", width: StancePercentages.nature.width+"%"}}/>
                    <div className="bg-nord-yellow h-2.5 absolute" style={{left:StancePercentages.industry.left+"%", width: StancePercentages.industry.width+"%"}}/>
                </div>
            </div>
        </div>
    );
}
export default PartyMemberCard;

