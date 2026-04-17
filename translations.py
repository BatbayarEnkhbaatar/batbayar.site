# Translation dictionaries for the website

TRANSLATIONS = {
    'en': {
        'nav': {
            'home': 'Home',
            'about': 'About',
            'projects': 'Projects',
            'contact': 'Contact',
            'voice_api': 'Voice API',
        },
        'footer': '© 2026 My Portfolio. All rights reserved.',
        'home': {
            'title': 'Home',
            'welcome': 'Welcome to My Portfolio',
            'intro': 'I\'m a Full Stack Developer & Research Engineer',
            'description': 'Explore my work, skills, and experience in software development, robotics, and AI.',
            'cta': 'Learn More About Me',
        },
        'about': {
            'title': 'About Me',
            'about_me': 'About Me',
            'name': 'Hi, I\'m Batbayar Enkhbaatar',
            'bio': 'I\'m a Full Stack developer and research engineer with 10+ years of experience in software development, robotics, AI, and cloud technologies. I specialize in building scalable APIs, integrating complex systems, and leading innovative projects in robotics and data engineering.',
            'journey': 'My journey in tech has taken me from system engineering in Mongolia to advanced research in South Korea and Canada, focusing on cutting-edge technologies like ROS2, SLAM, and cloud architectures.',
            'skills': 'Skills & Expertise',
            'backend': 'Backend',
            'backend_desc': 'GraphQL, RESTful APIs',
            'robotics': 'Robotics & AI',
            'robotics_desc': 'ROS2, Ubuntu, Cartographer, SLAM, Nav2, Python, C++',
            'devops': 'DevOps & Cloud',
            'devops_desc': 'Docker, Kubernetes, AWS CI/CD, GitHub Actions, AWS Certified Solutions Architect Associate, GCP',
            'languages_skills': 'Programming Languages',
            'languages_skills_desc': 'C++, Python',
            'experience': 'Experience',
            'senior_researcher': 'Senior Researcher',
            'scientist_mila': 'Scientist in Resident - Researcher',
            'backend_engineer': 'Back-end Engineer',
            'data_engineer': 'Data Engineer',
            'system_engineer': 'Senior System Engineer / System Engineer',
            'education': 'Education',
            'master': 'Master Degree',
            'bachelor': 'Bachelor Degree',
            'languages': 'Languages',
            'awards': 'Awards & Publications',
            'mongolian': 'Mongolian (Native)',
            'korean': 'Korean (TOPIK Level 4)',
            'english': 'English (Advanced)',
        },
        'projects': {
            'title': 'Projects',
            'heading': 'Featured Projects',
            'no_projects': 'Projects coming soon!',
        },
        'contact': {
            'title': 'Contact Me',
            'heading': 'Get In Touch',
            'email': 'Email',
            'phone': 'Phone',
            'linkedin': 'LinkedIn',
            'github': 'GitHub',
            'message': 'Feel free to reach out for collaborations and inquiries!',
        }
    },
    'ko': {
        'nav': {
            'home': '홈',
            'about': '소개',
            'projects': '프로젝트',
            'contact': '연락',
            'voice_api': '음성 API',
        },
        'footer': '© 2026 나의 포트폴리오. 모든 권리를 보유합니다.',
        'home': {
            'title': '홈',
            'welcome': '포트폴리오에 오신 것을 환영합니다',
            'intro': '나는 풀스택 개발자이자 연구 엔지니어입니다',
            'description': '소프트웨어 개발, 로봇공학, AI 경험을 탐색하세요.',
            'cta': '더 알아보기',
        },
        'about': {
            'title': '소개',
            'about_me': '소개',
            'name': '안녕하세요, 저는 Batbayar Enkhbaatar입니다',
            'bio': '저는 소프트웨어 개발, 로봇공학, AI, 클라우드 기술 분야에서 10년 이상의 경험을 가진 풀스택 개발자이자 연구 엔지니어입니다. 확장 가능한 API 구축, 복잡한 시스템 통합, 로봇공학 및 데이터 엔지니어링 혁신 프로젝트 주도를 전문으로 합니다.',
            'journey': '내 기술 경력은 몽골의 시스템 엔지니어링에서 시작하여 남한과 캐나다의 고급 연구로 이어졌으며 ROS2, SLAM, 클라우드 아키텍처 같은 최첨단 기술에 집중합니다.',
            'skills': '기술 및 전문성',
            'backend': '백엔드',
            'backend_desc': 'GraphQL, RESTful APIs',
            'robotics': '로봇공학 & AI',
            'robotics_desc': 'ROS2, Ubuntu, Cartographer, SLAM, Nav2, Python, C++',
            'devops': 'DevOps & 클라우드',
            'devops_desc': 'Docker, Kubernetes, AWS CI/CD, GitHub Actions, AWS 솔루션스 아키텍트 associate, GCP',
            'languages_skills': '프로그래밍 언어',
            'languages_skills_desc': 'C++, Python',
            'experience': '경험',
            'senior_researcher': '선임 연구원',
            'scientist_mila': '상주 과학자 - 연구원',
            'backend_engineer': '백엔드 엔지니어',
            'data_engineer': '데이터 엔지니어',
            'system_engineer': '선임 시스템 엔지니어 / 시스템 엔지니어',
            'education': '학력',
            'master': '석사 학위',
            'bachelor': '학사 학위',
            'languages': '언어',
            'awards': '상 & 학술지',
            'mongolian': '몽골어 (모국어)',
            'korean': '한국어 (TOPIK 4급)',
            'english': '영어 (고급)',
        },
        'projects': {
            'title': '프로젝트',
            'heading': '주요 프로젝트',
            'no_projects': '곧 프로젝트가 추가될 예정입니다!',
        },
        'contact': {
            'title': '연락처',
            'heading': '연락주세요',
            'email': '이메일',
            'phone': '전화',
            'linkedin': 'LinkedIn',
            'github': 'GitHub',
            'message': '협업 및 문의에 대해 편하게 연락주세요!',
        }
    }
}

def get_text(page, key, language='en'):
    """Get translated text"""
    try:
        if page in TRANSLATIONS.get(language, {}):
            return TRANSLATIONS[language][page].get(key, '')
        return TRANSLATIONS['en'][page].get(key, '')
    except:
        return ''
