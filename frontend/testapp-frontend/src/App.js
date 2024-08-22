import React, {useState, useEffect} from 'react';
import './App.css';

function App() {

    /// CHANGE BASEURL WHEN YOU HAVE A DEPLOYED APP
    const baseURL = "http://localhost/api";

    const [data, setData] = useState("Loading...");


    useEffect(() => {
	getCount();
    }, []);


    const getCount = async () => {
	try {
	    const response = await fetch(baseURL+"/get_count/default");
	    const result = await response.json();
	    setData(JSON.stringify(result));
	} catch (error) {
	    console.error("Error fetching data: ", error);
	}
    }

    const handleIncrement = async () => {
	try {
	    await fetch(baseURL+"/increment_count/default", {
		method: "POST",
	    });
	    console.log("Incremented count ");
	    await getCount();
	} catch (error) {
	    console.log("error incrementing count: ",error);
	}
    }

    const handleReset = async () => {
	try {
	    await fetch(baseURL+"/reset_count/default", {
		method: "POST",
	    });

	    console.log("reset response ");
	    await getCount();
	} catch(error) {
	    console.log("Error resetting count ", error);
	}
    }

    console.log("Data is "+ data);

    return (
	<div className="App">
	    <header className="App-header">
		<p>
		    Counter; {data}
		</p>
		<button onClick={handleIncrement}>Increment counter</button>
		<button onClick={handleReset}>Reset counter</button>
	    </header>

	</div>
    );
}

export default App;
