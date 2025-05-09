import { useEffect, useState } from "react";

function App() {
	const [screener, setScreener] = useState(null);
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		const baseUrl = import.meta.env.VITE_API_BASE_URL;

    		fetch(`${baseUrl}/screener`)
			.then((res) => res.json())
			.then((data) => {
				setScreener(data);
				setLoading(false);
			})
			.catch((err) => {
				console.error("Error loading screener:", err);
				setLoading(false);
			});
	}, []);

	if (loading) return <div>Loading screener...</div>;
	if (!screener) return <div>Failed to load screener.</div>;
	
	return (
		<div>
		<h1>{screener.full_name}</h1>
		<pre>{JSON.stringify(screener, null, 2)}</pre>
		</div>
	);
}

export default App;
	
