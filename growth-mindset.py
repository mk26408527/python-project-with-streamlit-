import streamlit as st  # Import the Streamlit library


def main():
    st.title("Growth Mindset Explorer")  # Set the title of the app

    # Sidebar for navigation
    page = st.sidebar.selectbox(
        "Choose a page", ["Home", "Mindset Quiz", "Growth Tips", "Set Goals"])  # Create a selectbox for page navigation

    # Display the selected page
    if page == "Home":
        home_page()
    elif page == "Mindset Quiz":
        quiz_page()
    elif page == "Growth Tips":
        tips_page()
    elif page == "Set Goals":
        goals_page()


def home_page():
    st.header("Welcome to the Growth Mindset Explorer")  # Set the header for the home page
    st.write("""
    A growth mindset is the belief that your abilities and intelligence can be developed through effort, learning, and persistence.
    
    Use this app to learn more about the growth mindset and how to develop it!
    """)  # Display information about the growth mindset
    st.image("assets/Growth.png", caption="Growth Mindset Illustration")  # Display an image with a caption


def quiz_page():
    st.header("Mindset Quiz")  # Set the header for the quiz page
    st.write("Answer these questions to reflect on your current mindset:")  # Display instructions for the quiz

    # Create radio buttons for quiz questions
    q1 = st.radio("1. When faced with a challenge, I usually:",
                  ["Give up easily", "Try harder but get frustrated", "See it as an opportunity to learn"])
    q2 = st.radio("2. I believe my intelligence is:",
                  ["Fixed and can't change much", "Somewhat flexible", "Highly developable"])

    if st.button("See Results"):  # Button to see quiz results
        score = 0
        if q1 == "See it as an opportunity to learn":
            score += 1
        if q2 == "Highly developable":
            score += 1

        st.write(f"Your growth mindset score: {score}/2")  # Display the quiz score
        if score == 2:
            st.success("Great job! You show strong signs of a growth mindset.")  # Display success message
        else:
            st.info(
                "There's room to develop your growth mindset. Check out the Growth Tips page!")  # Display info message


def tips_page():
    st.header("Tips for Developing a Growth Mindset")  # Set the header for the tips page
    tips = [
        "Embrace challenges as opportunities to learn",
        "View effort as a path to mastery",
        "Learn from criticism and feedback",
        "Find lessons and inspiration in others' success",
        "Use the word 'yet' when facing difficulties"
    ]
    for tip in tips:
        st.write(f"• {tip}")  # Display each tip


def goals_page():
    st.header("Set Your Growth Goals")  # Set the header for the goals page
    goal = st.text_input("Enter a personal growth goal:")  # Text input for entering a goal
    if st.button("Save Goal"):  # Button to save the goal
        st.success(f"Goal saved: {goal}")  # Display success message
        st.write(
            "Remember, the journey is just as important as the destination. Embrace the process!")  # Display additional message


if __name__ == "__main__":
    main()  # Run the main function
