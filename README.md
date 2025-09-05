🍲 FoodOne – Food Sharing & Saving Platform

FoodOne is a web application developed by me with the goal of reducing food wastage and making surplus food accessible to people who need it. The platform connects food donors with seekers, encouraging a sustainable community where food is shared instead of wasted.

🚀 Features

User Authentication – Secure login and signup system for donors and seekers

Food Posting – Donors can post food details (type, description, quantity, location, pickup time)

Listings Page – Seekers can browse available food items in real time

Filtering & Search – Search food by category, dietary preference, and distance

Map Integration – View food pickup points on an interactive map

Dashboard – Users can manage (view, edit, delete) their own food posts

Admin Panel – Manage users, monitor food posts, and ensure platform safety

🛠️ Tech Stack

Backend: Django + PostgreSQL

Frontend: HTML, CSS, JavaScript (custom UI preserved)

Authentication: Django Auth System

Maps & Location: Geolocation API + Map Integration

Deployment: (Heroku / Render / DigitalOcean – update based on what you used)

📸 Screenshots

(Add screenshots of your homepage, food listings, post form, and map here)

⚙️ Installation

Clone the repository

git clone https://github.com/your-username/foodone.git
cd foodone


Create a virtual environment

python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows


Install dependencies

pip install -r requirements.txt


Set up database & run migrations

python manage.py makemigrations
python manage.py migrate


Run the server

python manage.py runserver


Open in browser: http://localhost:8000
Deployed:https://bholey.onrender.com/

📌 Roadmap

 Add real-time chat between donors & seekers

 Implement push notifications for new food nearby

 Mobile app version (React Native / Flutter)

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

📄 License

This project is licensed under the MIT License – free to use and modify.

👨‍💻 Developed By

Roshan Neupane
Passionate about building impactful web apps that solve real-world problems 🌍
