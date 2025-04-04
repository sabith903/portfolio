from django.shortcuts import render, get_object_or_404
from .models import Skill, Project, About, Contact,Image

def home(request):
    """
    Home page view to display skills, projects, and about information
    """
    skills = Skill.objects.all()
    projects = Project.objects.all()
    about = About.objects.first()
    specific_image = Image.objects.filter(name="Hero Image").first()
    print(specific_image)  # Check if this prints the image object
    print(specific_image.image)  # Check if image field is populated
    print(specific_image.image.url) 
    images = Image.objects.all()

    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        # Create a new Contact object
        contact = Contact.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message
        )
        # Optionally, add a success message or redirect

    return render(request, 'main/home.html', {
        'skills': skills,
        'projects': projects,
        'about': about,
        'images': images,
        'specific_image': specific_image
    })


def skill_projects(request, skill_id):
    """
    View to show projects under a specific skill
    """
    # Get the skill or return 404 if not found
    skill = get_object_or_404(Skill, id=skill_id)
    
    # Get projects associated with this skill
    projects = Project.objects.filter(skills=skill)
    
    return render(request, 'main/skill_projects.html', {
        'skill': skill,
        'projects': projects
    })

def about(request):
    """
    About page view to display personal information
    """
    about_info = About.objects.first()  # Assuming only one About entry
    return render(request, 'main/about.html', {'about': about_info})

def contact(request):
    """
    Contact page view to handle contact form submissions
    """
    if request.method == 'POST':
        # Process form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Create a new Contact instance
        Contact.objects.create(
            name=name,
            email=email,
            phone_number=phone,
            message=message
        )
        
        # You might want to add a success message or redirect
        return render(request, 'main/contact_success.html')
    
    return render(request, 'main/contact.html')