import React, {useState, useEffect} from 'react';
import './App.css';

function App() {
    const [data, setData] = useState("Loading...");

    useEffect(() => {
	fetch("https://nbtestaks.uk/api/somedata/")
	    .then(response => response.json())
	    .then(data => setData(JSON.stringify(data)))
	    .catch(error => console.error("Error fetching data: ", error));
    }, []);
    console.log("Data is "+data);
    return (
	<div className="App">
	    <header className="App-header">
		<p>
		    API response; {data}
		</p>
	    </header>
	</div>
    );
}

export default App;
