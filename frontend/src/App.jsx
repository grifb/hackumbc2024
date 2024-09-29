import { useState } from 'react'
import './App.css'

function App() {
    const [url, setUrl] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [failed, setFailed] = useState(false);

    function submitUrl() {
        if (url != '') {
            fetch(`http://raspberrypi.local:3000/download-video`, {
                method: `POST`,
                body: JSON.stringify({
                    url
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(res => {
                    setFailed(false);
                    setUrl('');
                    setSubmitted(true);

                    setTimeout(() => {
                        setSubmitted(false);
                    }, 3000);
                })
                .catch(e => {
                    if (e instanceof TypeError) {
                        setFailed(true);
                         console.error(e);
                    }
                });
        }
    }

    return (
        <div className="grid min-h-screen place-items-center">
        <div className="flex flex-col gap-8 min-w-[50%]">
        <h1 className="font-sans-serif font-bold text-6xl">JamBase</h1>
        <input 
        onChange={(e) => setUrl(e.currentTarget.value)} 
        value={url} 
        className="border-2 border-black p-4 rounded-sm text-center" placeholder="https://youtube.com" 
        />
        <button onClick={submitUrl} className="bg-black text-white p-4 rounded-lg">Pump Up The Jam</button>
        {failed && <p className="text-red-500">Failed to connect to the API. Is the API running?</p>}
        {submitted && <p className="text-green-500">Your song has been queued up!</p>}
        </div>
        </div>
    )
}

export default App
