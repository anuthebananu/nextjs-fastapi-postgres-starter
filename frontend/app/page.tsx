'use client'

import { useState } from "react";
const apiUrl = process.env.NEXT_PUBLIC_API_URL;



export default function Page() {
  // const message = await fetch(`${apiUrl}/messages?conversation_id=1`).then((res) => res.json())
  const [inputMessage, setInputMessage] = useState('')
  const handleSendMessage = () => {
    console.log("Sending message", inputMessage)
  }

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        <p>Messages go here</p>
      </div>
      <div className="bg-white p-4 flex items-center">
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          className="flex-1 border rounded-l-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Type a message..."
          />
        <button
          onClick={handleSendMessage}
          className="bg-blue-500 text-white px-4 py-2 rounded-r-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Send
        </button>
      </div>
      </div>
  )
}
