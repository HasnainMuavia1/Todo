# Modern ToDo Application with Django

A sleek, modern Todo application built with Django, featuring user authentication and real-time task management. This application provides a beautiful user interface with smooth animations and a responsive design.

## 🌟 Features

### Authentication
- User registration with email verification
- Secure login system
- Password reset functionality
- Remember me option
- Social authentication ready

### Task Management
- Create, Read, Update, and Delete (CRUD) tasks
- Mark tasks as complete/incomplete
- Task filtering (All, Active, Completed)
- Task description support
- Real-time task counter
- Responsive design for all devices

### UI/UX
- Modern and clean interface
- Smooth animations and transitions
- Intuitive task management
- Interactive notifications
- Mobile-first design
- Beautiful gradients and shadows

## 🚀 Technology Stack

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, JavaScript
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome 6
- **Database**: SQLite (default) / PostgreSQL (production)
- **Authentication**: Django built-in authentication

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create .env file
```bash
cp .env.example .env
# Update .env with your configuration
```

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Run development server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
todo_project/
│
├── todo/                    # Main application directory
│   ├── migrations/         # Database migrations
│   ├── static/            # Static files (CSS, JS, Images)
│   ├── templates/         # HTML templates
│   ├── forms.py          # Form definitions
│   ├── models.py         # Database models
│   ├── urls.py           # URL configurations
│   ├── views.py          # View logic
│   └── apps.py           # App configuration
│
├── static/                # Project-wide static files
├── templates/            # Project-wide templates
├── manage.py             # Django management script
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root and add the following:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

### Database Configuration

The project uses SQLite by default. To use PostgreSQL, update your database configuration in settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📱 Usage

1. Register a new account through the signup page
2. Login with your credentials
3. Start adding tasks through the main interface
4. Mark tasks as complete by clicking the checkbox
5. Edit tasks by clicking the edit icon
6. Delete tasks by clicking the delete icon
7. Filter tasks using the filter dropdown
8. Logout using the button in the top right corner

## 🔒 Security Features

- CSRF protection
- Password hashing
- Form validation
- Secure session handling
- Protected views with login required
- SQL injection prevention
- XSS protection

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Hasnain Muavia
- GitHub: [@yourgithubusername](https://github.com/yourgithubusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Font Awesome for the icons
- Bootstrap team for the amazing framework
- Django team for the excellent documentation
- All contributors who help to improve this project

## 📸 Screenshots

[Add your application screenshots here]

## 🐛 Bug Reports

If you discover any bugs, feel free to create an issue on the GitHub repository. Please include:
- Your operating system name and version
- Any details about your local setup that might be helpful in troubleshooting
- Detailed steps to reproduce the bug

## 🎯 Future Improvements

- [ ] Add task categories
- [ ] Implement task priorities
- [ ] Add due dates for tasks
- [ ] Create task sharing functionality
- [ ] Add dark mode support
- [ ] Implement task export feature
- [ ] Add task statistics and analytics
- [ ] Create mobile app version

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!
