from flask import Flask, render_template_string, send_file
import os
from datetime import datetime

app = Flask(__name__)

# Check if resume and profile photo exist
resume_path = 'resume.pdf'
profile_path = 'profile.jpg'
has_resume = os.path.exists(resume_path)
has_profile = os.path.exists(profile_path)

# Portfolio Data
PORTFOLIO_DATA = {
    "name": "REVATHI SURESH KHANAPUR",
    "title": "Software Engineer | AI & Full Stack Developer",
    "location": "Karnataka, India",
    "location_map": "https://www.google.com/maps/search/?api=1&query=Karnataka+India",
    "email": "your.email@gmail.com",  # CHANGE THIS
    "phone": "+91-1234567890",  # CHANGE THIS
    "linkedin": "https://www.linkedin.com/in/your-profile",  # CHANGE THIS
    "summary": "A highly motivated and results-driven individual with a passion for innovation, problem-solving, and Artificial Intelligence.",
    "education": [
        {"degree": "Bachelor of Engineering (BE) - Computer Science and Engineering", "institution": "SJC Institute of Technology, Chickaballapur", "year": "2021-2025", "score": "CGPA: 8.92"}
    ],
    "technical_skills": ["Python", "Java", "JavaScript", "React.js", "SQL", "MySQL", "MongoDB", "HTML5", "CSS3", "DBMS", "Data Structures & Algorithms", "Git", "REST API", "Spring Boot", "Microservices", "Flask"],
    "soft_skills": ["Problem-Solving", "Communication", "Collaboration", "Innovation", "Adaptability", "Continuous Learning"],
    "languages": ["English", "Kannada", "Hindi"],
    "projects": [
        {"name": "AI-Driven Web-Based Secure File Transfer System", "tech": "Python, Flask, AES/RSA Encryption, OpenAI API", "description": "Developed backend using Python/Flask for secure file processing with AES & RSA encryption."},
        {"name": "Online Book Store System", "tech": "HTML, CSS, Java, MySQL, Spring Boot", "description": "Full-stack e-commerce application with user registration, login, book browsing, and order placement."},
        {"name": "Fresh Mart - E-Commerce Grocery Application", "tech": "HTML, CSS, JavaScript, Netlify/Vercel", "description": "Web-based platform with real-time progress tracking, secure authentication."}
    ],
    "experience": [
        {"role": "Full Stack Development Intern", "company": "Inflow Technologies", "location": "", "duration": "", "description": "Gained hands-on experience in Java programming through real-world projects."}
    ],
    "achievements": [
        "🏆 Java Certification - Infosys Springboard",
        "📜 Deep Dive into Python Libraries - INDOSKILL for INDIA",
        "🔧 Internship Certificate - Inflow Technologies",
        "☁️ AWS Trained - Vinsys IT Services",
        "🎓 IBM Certification - Full Stack Development"
    ],
    "activities": [
        "💡 Passionate about AI-driven systems and human-centered solutions",
        "🚀 Committed to bridging technology with real-world impact",
        "📚 Continuous learner focused on next-generation technologies"
    ]
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Revathi Khanapur | Portfolio</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Poppins', sans-serif;
            background: #f5f5f5;
        }
        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            background: white;
            box-shadow: 0 2px 20px rgba(0,0,0,0.1);
            z-index: 1000;
            padding: 15px 0;
        }
        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }
        .logo {
            font-size: 24px;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .nav-links {
            display: flex;
            gap: 25px;
            list-style: none;
            flex-wrap: wrap;
        }
        .nav-links a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: #667eea;
        }
        .resume-btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white !important;
            padding: 8px 20px;
            border-radius: 25px;
        }
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            background: linear-gradient(135deg, #667eea10 0%, #764ba210 100%);
            padding-top: 80px;
        }
        .hero-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }
        .hero-content h1 {
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .gradient-text {
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-title {
            font-size: 24px;
            color: #666;
            margin-bottom: 20px;
        }
        .hero-description {
            color: #666;
            margin-bottom: 30px;
            line-height: 1.6;
        }
        .btn-group {
            display: flex;
            gap: 15px;
        }
        .btn-primary {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 500;
            transition: transform 0.3s;
        }
        .btn-primary:hover {
            transform: translateY(-2px);
        }
        .btn-outline {
            background: transparent;
            border: 2px solid #667eea;
            color: #667eea;
            padding: 12px 30px;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s;
        }
        .btn-outline:hover {
            background: #667eea;
            color: white;
        }
        .hero-image {
            text-align: center;
        }
        .avatar-large {
            width: 250px;
            height: 250px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 50%;
            animation: float 3s ease-in-out infinite;
            overflow: hidden;
        }
        .avatar-large img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
            transition: transform 0.3s;
        }
        .avatar-large img:hover {
            transform: scale(1.05);
        }
        .avatar-large .emoji-avatar {
            font-size: 120px;
            text-align: center;
            line-height: 250px;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        .section {
            padding: 80px 0;
        }
        .section-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        .section-title {
            font-size: 36px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 50px;
        }
        .section-title span {
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        .skill-category {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }
        .skill-category h3 {
            margin-bottom: 20px;
            color: #667eea;
        }
        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 10px;
        }
        .skill-tag {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 10px 24px;
            border-radius: 30px;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s;
            cursor: default;
        }
        .skill-tag:hover {
            transform: translateY(-2px) scale(1.05);
            box-shadow: 0 5px 15px rgba(102,126,234,0.4);
        }
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
        }
        .project-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            transition: transform 0.3s;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .project-header {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
        }
        .project-header h3 {
            margin-top: 10px;
            font-size: 18px;
        }
        .project-body {
            padding: 20px;
        }
        .project-tech {
            color: #667eea;
            font-weight: 500;
            margin-bottom: 10px;
        }
        .project-description {
            color: #666;
            line-height: 1.6;
        }
        .timeline-item {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }
        .timeline-title {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 5px;
            color: #667eea;
        }
        .timeline-subtitle {
            color: #666;
            margin-bottom: 5px;
        }
        .timeline-date {
            color: #999;
            font-size: 14px;
            margin-bottom: 10px;
        }
        .achievements-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .achievement-card {
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            transition: transform 0.3s;
        }
        .achievement-card:hover {
            transform: translateY(-5px);
        }
        .achievement-icon {
            font-size: 40px;
            margin-bottom: 10px;
        }
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            text-align: center;
        }
        .contact-card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            transition: transform 0.3s;
            cursor: pointer;
        }
        .contact-card:hover {
            transform: translateY(-5px);
        }
        .contact-icon {
            font-size: 48px;
            color: #667eea;
            margin-bottom: 15px;
        }
        .contact-card a {
            color: #667eea;
            text-decoration: none;
        }
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 2000;
            justify-content: center;
            align-items: center;
        }
        .modal.active {
            display: flex;
        }
        .modal-content {
            background: white;
            border-radius: 15px;
            width: 90%;
            max-width: 800px;
            max-height: 90vh;
            overflow: hidden;
        }
        .modal-header {
            padding: 20px;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .modal-body {
            padding: 20px;
            overflow-y: auto;
            max-height: calc(90vh - 80px);
        }
        .close-modal {
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
        }
        .footer {
            background: #1a1a2e;
            color: white;
            padding: 30px 0;
            text-align: center;
        }
        body.dark-mode {
            background: #1a1a2e;
        }
        body.dark-mode .navbar,
        body.dark-mode .skill-category,
        body.dark-mode .project-card,
        body.dark-mode .timeline-item,
        body.dark-mode .achievement-card,
        body.dark-mode .contact-card {
            background: #2a2a3e;
            color: #eee;
        }
        body.dark-mode .nav-links a {
            color: #eee;
        }
        body.dark-mode .hero-description,
        body.dark-mode .project-description,
        body.dark-mode .timeline-subtitle {
            color: #ccc;
        }
        .dark-toggle {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 999;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .toast {
            position: fixed;
            bottom: 100px;
            right: 30px;
            background: #4caf50;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            display: none;
            z-index: 1000;
        }
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }
            .hero-container {
                grid-template-columns: 1fr;
                text-align: center;
            }
            .btn-group {
                justify-content: center;
            }
        }
        iframe {
            width: 100%;
            height: 500px;
            border: none;
        }
        .small-hint {
            font-size: 12px;
            color: #667eea;
            margin-top: 8px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">Revathi Khanapur</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#education">Education</a></li>
                <li><a href="#experience">Experience</a></li>
                <li><a href="#achievements">Certifications</a></li>
                <li><a href="#contact">Contact</a></li>
                <li><a href="#" class="resume-btn" onclick="openResumeModal()">📄 Resume</a></li>
            </ul>
        </div>
    </nav>
    
    <section id="home" class="hero">
        <div class="hero-container">
            <div class="hero-content">
                <h1>Hi, I'm <span class="gradient-text">{{ data.name }}</span></h1>
                <div class="hero-title">{{ data.title }}</div>
                <p class="hero-description">{{ data.summary }}</p>
                <div class="btn-group">
                    <button class="btn-primary" onclick="openResumeModal()">View Resume</button>
                    <button class="btn-outline" onclick="downloadResume()">Download CV</button>
                </div>
            </div>
            <div class="hero-image">
                <div class="avatar-large">
                    {% if has_profile %}
                    <img src="/profile-photo" alt="Profile Photo">
                    {% else %}
                    <div class="emoji-avatar">👩‍💻</div>
                    {% endif %}
                </div>
            </div>
        </div>
    </section>
    
    <section id="skills" class="section">
        <div class="section-container">
            <h2 class="section-title">Technical <span>Skills</span></h2>
            <div class="skills-grid">
                <div class="skill-category">
                    <h3>💻 Languages & Frameworks</h3>
                    <div class="skill-tags">
                        <span class="skill-tag">Python</span>
                        <span class="skill-tag">Java</span>
                        <span class="skill-tag">JavaScript</span>
                        <span class="skill-tag">React.js</span>
                        <span class="skill-tag">Spring Boot</span>
                        <span class="skill-tag">Flask</span>
                    </div>
                </div>
                <div class="skill-category">
                    <h3>🗄️ Databases & Tools</h3>
                    <div class="skill-tags">
                        <span class="skill-tag">SQL</span>
                        <span class="skill-tag">MySQL</span>
                        <span class="skill-tag">MongoDB</span>
                        <span class="skill-tag">HTML5/CSS3</span>
                        <span class="skill-tag">Git</span>
                        <span class="skill-tag">REST API</span>
                    </div>
                </div>
                <div class="skill-category">
                    <h3>🤝 Soft Skills</h3>
                    <div class="skill-tags">
                        {% for skill in data.soft_skills %}
                        <span class="skill-tag">{{ skill }}</span>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <section id="projects" class="section" style="background: #f8f9fa;">
        <div class="section-container">
            <h2 class="section-title">Featured <span>Projects</span></h2>
            <div class="projects-grid">
                {% for project in data.projects %}
                <div class="project-card">
                    <div class="project-header">
                        <h3>{{ project.name }}</h3>
                    </div>
                    <div class="project-body">
                        <div class="project-tech">🛠️ {{ project.tech }}</div>
                        <p class="project-description">{{ project.description }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>
    
    <section id="education" class="section">
        <div class="section-container">
            <h2 class="section-title">My <span>Education</span></h2>
            {% for edu in data.education %}
            <div class="timeline-item">
                <h3 class="timeline-title">{{ edu.degree }}</h3>
                <div class="timeline-subtitle">{{ edu.institution }}</div>
                <div class="timeline-date">{{ edu.year }} | {{ edu.score }}</div>
            </div>
            {% endfor %}
        </div>
    </section>
    
    <section id="experience" class="section" style="background: #f8f9fa;">
        <div class="section-container">
            <h2 class="section-title">Work <span>Experience</span></h2>
            {% for exp in data.experience %}
            <div class="timeline-item">
                <h3 class="timeline-title">{{ exp.role }}</h3>
                <div class="timeline-subtitle">{{ exp.company }}</div>
                <p>{{ exp.description }}</p>
            </div>
            {% endfor %}
        </div>
    </section>
    
    <section id="achievements" class="section">
        <div class="section-container">
            <h2 class="section-title">Certifications & <span>Achievements</span></h2>
            <div class="achievements-grid">
                {% for achievement in data.achievements %}
                <div class="achievement-card">
                    <div class="achievement-icon">{{ achievement[:2] }}</div>
                    <p>{{ achievement }}</p>
                </div>
                {% endfor %}
            </div>
            <h2 class="section-title" style="margin-top: 50px;">Activities & <span>Interests</span></h2>
            {% for activity in data.activities %}
            <div class="timeline-item">
                <p>{{ activity }}</p>
            </div>
            {% endfor %}
        </div>
    </section>
    
    <section id="contact" class="section">
        <div class="section-container">
            <h2 class="section-title">Get In <span>Touch</span></h2>
            <div class="contact-grid">
                <div class="contact-card" onclick="copyEmail()">
                    <div class="contact-icon"><i class="fas fa-envelope"></i></div>
                    <h4>Email</h4>
                    <p>{{ data.email }}</p>
                    <span class="small-hint">📋 Click to copy</span>
                </div>
                <div class="contact-card" onclick="makePhoneCall()">
                    <div class="contact-icon"><i class="fas fa-phone"></i></div>
                    <h4>Phone</h4>
                    <p>{{ data.phone }}</p>
                    <span class="small-hint">📞 Click to call</span>
                </div>
                <div class="contact-card" onclick="openLocation()">
                    <div class="contact-icon"><i class="fas fa-map-marker-alt"></i></div>
                    <h4>Location</h4>
                    <p>{{ data.location }}</p>
                    <span class="small-hint">🗺️ View map</span>
                </div>
                <div class="contact-card" onclick="openLinkedIn()">
                    <div class="contact-icon"><i class="fab fa-linkedin"></i></div>
                    <h4>LinkedIn</h4>
                    <p>Connect with me</p>
                    <span class="small-hint">🔗 Open profile</span>
                </div>
            </div>
        </div>
    </section>
    
    <footer class="footer">
        <div class="section-container">
            <p>&copy; 2026 Revathi Suresh Khanapur. All rights reserved.</p>
        </div>
    </footer>
    
    <div id="resumeModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>My Resume</h3>
                <button class="close-modal" onclick="closeResumeModal()">×</button>
            </div>
            <div class="modal-body">
                {% if has_resume %}
                <iframe src="/view-resume"></iframe>
                {% else %}
                <div style="text-align: center; padding: 50px;">
                    <i class="fas fa-file-pdf" style="font-size: 64px; color: #667eea;"></i>
                    <p style="margin-top: 20px;">Resume PDF not found.</p>
                </div>
                {% endif %}
            </div>
        </div>
    </div>
    
    <div class="dark-toggle" onclick="toggleDarkMode()">
        <i class="fas fa-moon"></i>
    </div>
    
    <div id="toast" class="toast">
        <i class="fas fa-check-circle"></i> <span id="toastMessage"></span>
    </div>
    
    <script>
        function openResumeModal() { 
            document.getElementById('resumeModal').classList.add('active'); 
        }
        function closeResumeModal() { 
            document.getElementById('resumeModal').classList.remove('active'); 
        }
        function downloadResume() { 
            window.location.href = '/download-resume'; 
        }
        function copyEmail() {
            const email = "{{ data.email }}";
            navigator.clipboard.writeText(email);
            showToast("✅ Email copied: " + email);
        }
        function makePhoneCall() {
            const phone = "{{ data.phone }}";
            window.location.href = "tel:" + phone;
        }
        function openLocation() {
            window.open("{{ data.location_map }}", '_blank');
        }
        function openLinkedIn() {
            window.open("{{ data.linkedin }}", '_blank');
        }
        function showToast(message) {
            const toast = document.getElementById('toast');
            document.getElementById('toastMessage').innerText = message;
            toast.style.display = 'block';
            setTimeout(() => { toast.style.display = 'none'; }, 3000);
        }
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
            const icon = document.querySelector('.dark-toggle i');
            if(document.body.classList.contains('dark-mode')) {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
        }
        document.addEventListener('keydown', function(e) { 
            if(e.key === 'Escape') closeResumeModal(); 
        });
        window.onclick = function(event) { 
            if(event.target === document.getElementById('resumeModal')) closeResumeModal(); 
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, data=PORTFOLIO_DATA, has_resume=has_resume, has_profile=has_profile)

@app.route('/profile-photo')
def profile_photo():
    if has_profile:
        return send_file(profile_path, mimetype='image/jpeg')
    return "Photo not found", 404

@app.route('/view-resume')
def view_resume():
    if has_resume:
        return send_file(resume_path, mimetype='application/pdf')
    return "Resume not found", 404

@app.route('/download-resume')
def download_resume():
    if has_resume:
        return send_file(resume_path, as_attachment=True, download_name='Revathi_Khanapur_Resume.pdf')
    return "Resume not found", 404