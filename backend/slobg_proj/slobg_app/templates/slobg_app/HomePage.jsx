class HomePage extends React.Component {
 
    // How do we change the page depending on the level of access
    // Volunteer vs. SLOBG Worker
    constructor(props) {
        super(props);
        this.state = {

        };
    }

    render() {
        return (
            <div>
                <h1>SLO Botanical Gardens Homepage</h1>
                {/*Add onClick functionality once rerouting is set up */}
                <button className="btn btn-primary btn-lg">Record My Hours</button>         
                <button className="btn btn-primary btn-lg">Manage Volunteer Hours</button>
            </div>
        );
    }

}