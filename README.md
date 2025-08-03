# 🌄 Sudurpaschim Social Life Website

This project is a dynamic, multi-page website representing the culture, religion, social structure, and feedback system of **Sudurpaschim Province**. Built with **Flask**, **SQLite**, **Bootstrap 5**, and custom CSS, it highlights key aspects of the province and provides interactive features for users.

---

## 🌐 Main Features

### 🧭 Navigation Bar
- Sticky top navbar with logo and responsive design
- Links to Home, About, Feedback, Culture (dropdown: Youth, Community, Festivals, Social Issues), Religion

### 📖 About Page
- Alternating layout with text and images about Sudurpaschim Province
- Bootstrap grid for responsive design

### 🎭 Culture Section
- Subpages for:
  - Youth (lifestyle, technology, education)
  - Community (village life, joint family, ethnic harmony)
  - Festivals (Dashain, Holi, Maghi, Deuda, Gaura)
  - Social Issues (gender, youth empowerment, social awareness)

### 🛐 Religion Page
- Details on religious harmony and practices in the province

### 📝 Feedback System
- Styled feedback form (Full Name, Email, Contact, Message)
- Data stored in SQLite database via Flask backend
- PHP/MySQL integration option for feedback (datacon.php)

### 🖼️ Static Resources
- All images and CSS loaded from `/static/` directory
- Organized folders for images (community, cultural, festivals, youth, etc.)

### 🧩 Template Structure
- Jinja2 includes for header and footer for consistent layout
- Common header/footer used across all pages
- Centralized common-header.html and common-cultural-header.html for reusable navigation

### 🔗 Direct Page Access
- Flask routes for all major pages and subpages
- Anchor navigation (e.g., `/index#about`)

---

## 🗂️ Project Structure

```
project/
├── app.py                # Main Flask app and routes
├── static/
│   ├── style.css         # Custom CSS
│   └── images/           # All images (organized by topic)
├── templates/
│   ├── index.html        # Home page
│   ├── feedback.html     # Feedback form
│   ├── header.html       # Navbar/header include
│   ├── footer.html       # Footer include
│   ├── Community/        # Community subpages
│   ├── Cultural/         # Cultural subpages
│   ├── Youth/            # Youth subpages
│   ├── Festivals/        # Festival subpages
│   ├── Socialissues/     # Social issues subpages
│   └── Religion/         # Religion page
├── instance/
│   └── site.db           # SQLite database
└── README.md
```

---

## 🧰 Tools & Technologies

- ⚙️ **Flask** (Python web framework)
- 🗃️ **SQLite** (Feedback database)
- 🎨 **Bootstrap 5** (CSS framework)
- 💅 **CSS3** (Custom styles)
- 🌐 **HTML5**
- 🐘 **PHP/MySQL** (optional feedback backend)

---

## 🏁 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Bibekadhikari77/sudurpaschim-social-life-website.git
   cd sudurpaschim-social-life-website
   ```
2. Install Python dependencies:
   ```bash
   pip install flask flask_sqlalchemy
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/`

---

## 📂 Key Pages & Routes

- `/` or `/index.html` — Home page
- `/index#about` — About section anchor
- `/feedback` — Feedback form (Flask backend)
- `/feedback.html` — Direct feedback form access
- `/Community/village-life.html`, `/Community/joint-family.html`, `/Community/ethnic-harmony.html` — Community subpages
- `/Cultural/gaura.html`, `/Cultural/festivals-identity.html`, `/Cultural/folk-culture.html` — Cultural subpages
- `/Festivals/dashain.html`, `/Festivals/holi.html`, `/Festivals/maghi.html` — Festival subpages
- `/Youth/lifestyle.html`, `/Youth/technology.html`, `/Youth/education.html` — Youth subpages
- `/Socialissues/gender.html`, `/Socialissues/youthempower.html`, `/Socialissues/socialawarness.html` — Social issues subpages
- `/Religion/religion.html` — Religion page

---

## 📝 Feedback Integration

- Feedback form posts to Flask backend and stores data in SQLite
- Optionally, feedback can be sent to PHP backend (`datacon.php`) for MySQL storage
- Feedback table includes auto timestamp

---

## 💡 Customization & Extensibility

- Easily add new pages by creating templates and adding routes in `app.py`
- Centralized header/footer for consistent layout
- Static resources for images and CSS

---

## 📄 License

This project is open source and available under the MIT License.
