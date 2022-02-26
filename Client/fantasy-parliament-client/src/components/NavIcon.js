function NavIcon(props) {
    const sendInfoBack = () => {
        props.onIconClicked(props.iconId);
    }
    return(
        <button val={props.iconId} onClick={sendInfoBack} className="flex z-20 justify-center content-center group flex-col h-16 w-16 bg-nord-dark-3 m-1 p-1 rounded-lg hover:rounded-2xl hover:transition-all">
            {props.icon} 
            <div className="absolute w-auto min-w-max pb-1 font-bold left-20 px-5 rounded-md scale-0 origin-left group-hover:transition-all group-hover:scale-100 text-nord-light-1 bg-nord-dark-4">
                {props.name} 
            </div> 
        </button>
    );
}
export default NavIcon;
