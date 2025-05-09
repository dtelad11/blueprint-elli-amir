import './index.css';
import { useEffect, useState } from "react";

function App() {
	const [screener, setScreener] = useState(null);
	const [loading, setLoading] = useState(true);
	const [currentIndex, setCurrentIndex] = useState(0);
	const [answers, setAnswers] = useState([]);
	const [isDone, setIsDone] = useState(false);

	useEffect(() => {
		/* Get the screener data from the backend. */
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

	function submitAnswers(finalAnswers) {
		/**
		 * Submits the user's screener answers to the backend for
		 * scoring (... or storage, delivery to therapist, et cetera).
		 */
		const baseUrl = import.meta.env.VITE_API_BASE_URL;

		fetch(`${baseUrl}/score`, {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ answers: finalAnswers }),
		})
			.then((res) => res.json())
			.then((data) => {
				console.log("Backend response:", data);
			})
			.catch((err) => {
				console.error("Error submitting answers:", err);
			});
	}

	function handleAnswer(value) {
		/**
		 * Add the user's latest response to the answers array, and
		 * submit to the API if done.
		 */
		const question_id = currentQuestion.question_id;
		const newAnswers = [...answers, { question_id, value }];
		setAnswers(newAnswers);
		
		if (currentIndex + 1 < totalQuestions) {
			setCurrentIndex(currentIndex + 1);
		} else {
			console.log("Final answers:", newAnswers);
			submitAnswers(newAnswers);
			setIsDone(true);
		}
	}

	if (loading) return <div>Loading screener...</div>;
	if (!screener) return <div>Failed to load screener.</div>;

	if (isDone) {
		/* Let the user know that we're done. */
		return (
			<div style={{ textAlign: "center", padding: "2rem" }}>
			<h1>Thank you!</h1>
			<p>Your answers have been submitted.</p>
			</div>
		);
	}

	/* Parse the screener contents and show the current question. */
	/* Elli: In a real app, we would define the structure of the screener
	 * using a `screener.ts` type file and update the `useState` call above
	 * accordingly. This would ensure type safety and better integration
	 * with the rest of the app. */
	const section = screener.content.sections[0];
	const questions = section.questions;
	const answerOptions = section.answers;
	const totalQuestions = questions.length;
	const currentQuestion = questions[currentIndex];
	
	return (
		<div style={{ maxWidth: "600px", margin: "0 auto", padding: "2rem" }}>
		<h1>{screener.content.display_name}</h1>
		<p>{section.title}</p>
		<h2 style={{ minHeight: "3.5em", display: "flex", alignItems: "top" }}>{currentQuestion.title}</h2>
		<p>
		Question {currentIndex + 1} of {totalQuestions}
		</p>
		<progress value={currentIndex} max={totalQuestions} style={{ width: "100%", height: "1rem", margin: "1rem 0" }}/>
		
		{answerOptions.map((option) => (
			<button
			key={option.value}
			onClick={() => handleAnswer(option.value)}
			style={{
				display: "block",
				margin: "0.5rem 0",
				padding: "0.75rem 1rem",
				width: "100%",
				backgroundColor: "#2C5EFF",
				color: "white",
				border: "none",
				borderRadius: "6px",
				fontSize: "1rem",
				fontWeight: "bold",
			}}
			>
			{option.title}
			</button>
		))}
		</div>
	);
}

export default App;
	
