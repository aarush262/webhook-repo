# 🚀 GitHub Webhook Listener using Flask + MongoDB

This project is a *GitHub Webhook Listener* built with *Flask, **MongoDB, and **Ngrok*. It receives push and pull request events from any GitHub repo and stores them in MongoDB. The UI displays real-time activity using HTML, CSS, and JavaScript.

---

## 📦 Features

- 📬 Receives GitHub webhook events (push, pull_request)
- 📊 Stores event data in MongoDB
- 🌐 Live-updating front-end using AJAX
- 🧾 Displays author, action type, branches, and timestamps
- 🌈 Clean UI styled with basic CSS

---

## 🔧 How to Run

1. *Clone the Repository*

```bash
git clone https://github.com/aarush262/webhook-repo.git
cd webhook-repo

	2.	Install Dependencies

pip install -r requirements.txt

	3.	Start Flask Server

python app.py

	4.	Start Ngrok (in a new terminal)

ngrok http 5000

Copy the HTTPS URL from Ngrok — this will be used for the GitHub webhook.

⸻

🔗 Set up GitHub Webhook
	1.	Go to your GitHub repository
	2.	Navigate to Settings > Webhooks
	3.	Click “Add Webhook”
	4.	Set the Payload URL to your Ngrok URL + /webhook (e.g. https://xxxx.ngrok-free.app/webhook)
	5.	Set Content type to application/json
	6.	Choose individual events or keep default (push, pull_request)
	7.	Save the webhook

⸻

🔄 Test with curl (optional)

curl -X POST https://<your-ngrok-url>/webhook \
-H "Content-Type: application/json" \
-d '{"author":"Test User", "action_type":"push"}'


⸻

🛠 Project Structure

webhook-repo/
│
├── app.py                # Flask backend
├── requirements.txt      # Dependencies
├── README.md             # You’re reading it 🙂
│
├── static/
│   └── styles.css        # CSS styling
│
├── templates/
│   └── index.html        # HTML UI (with JS to fetch events)


⸻

💾 MongoDB Schema Example

{
  "author": "aarush262",
  "action_type": "push",
  "from_branch": null,
  "to_branch": "main",
  "timestamp": "2025-07-03T12:15:59Z"
}


⸻

📸 Screenshot


⸻

💻 Tech Stack
	•	Backend: Python + Flask
	•	Database: MongoDB (local)
	•	Frontend: HTML, CSS, JavaScript
	•	Tunnel: Ngrok
	•	Version Control: Git + GitHub

⸻

👨‍💻 Author

Aarush Yadav
GitHub: @aarush262

⸻

⭐ Support

If this helped you or impressed you, drop a ⭐ on the repo 🙂
