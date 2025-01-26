'''Chatbot for FAQs
Create a chatbot that can answer frequently asked
questions (FAQs) about a particular topic or product.
Use natural language processing (NLP) techniques and
pre-built libraries like NLTK or SpaCy to understand and
generate responses.'''


faqs = {
    "exam schedule": "The exam schedule is usually announced two weeks before exams. Please check the notice board or the university website.",
    "admission process": "The admission process involves filling out the online form, uploading required documents, and attending an interview if applicable.",
    "library hours": "The library is open from 8 AM to 8 PM on weekdays and 10 AM to 4 PM on weekends.",
    "hostel facilities": "The hostels provide single and shared rooms, Wi-Fi, and meals. Please contact the hostel office for more details.",
    "scholarships": "Scholarships are available for merit-based and need-based students. Visit the scholarship section on the university website for eligibility criteria.",
    "course materials": "Course materials can be downloaded from the university portal or collected from your respective departments.",
    "internship opportunities": "Internship opportunities are shared via the placement cell. Check your university email for updates.",
    "grading system": "The grading system follows a 10-point scale with letter grades from A+ to F.",
    "attendance policy": "A minimum of 75% attendance is required to be eligible for exams.",
    "student ID card": "To apply for a student ID card, visit the administration office with a passport-sized photo and a copy of your admission letter."
}

def get_response(user_query):
    # Check if any keyword in the user query matches the FAQ keys
    for key, answer in faqs.items():
        if key in user_query.lower():
            return answer
    return "Sorry, I couldn't find an answer to that. Please try asking differently."

# Chatbot interface
print("Student FAQ Chatbot (Type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Best of luck with your studies!")
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}")
