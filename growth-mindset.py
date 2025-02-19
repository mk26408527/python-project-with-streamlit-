import streamlit as st


def main():
    st.title("Growth Mindset Explorer")

    # Sidebar for navigation
    page = st.sidebar.selectbox(
        "Choose a page", ["Home", "Mindset Quiz", "Growth Tips", "Set Goals"])

    if page == "Home":
        home_page()
    elif page == "Mindset Quiz":
        quiz_page()
    elif page == "Growth Tips":
        tips_page()
    elif page == "Set Goals":
        goals_page()


def home_page():
    st.header("Welcome to the Growth Mindset Explorer")
    st.write("""
    A growth mindset is the belief that your abilities and intelligence can be developed through effort, learning, and persistence.
    
    Use this app to learn more about the growth mindset and how to develop it!
    """)
    st.image("assets/Growth.png", caption="Growth Mindset Illustration")


def quiz_page():
    st.header("Mindset Quiz")
    st.write("Answer these questions to reflect on your current mindset:")

    q1 = st.radio("1. When faced with a challenge, I usually:",
                  ["Give up easily", "Try harder but get frustrated", "See it as an opportunity to learn"])
    q2 = st.radio("2. I believe my intelligence is:",
                  ["Fixed and can't change much", "Somewhat flexible", "Highly developable"])

    if st.button("See Results"):
        score = 0
        if q1 == "See it as an opportunity to learn":
            score += 1
        if q2 == "Highly developable":
            score += 1

        st.write(f"Your growth mindset score: {score}/2")
        if score == 2:
            st.success("Great job! You show strong signs of a growth mindset.")
        else:
            st.info(
                "There's room to develop your growth mindset. Check out the Growth Tips page!")


def tips_page():
    st.header("Tips for Developing a Growth Mindset")
    tips = [
        "Embrace challenges as opportunities to learn",
        "View effort as a path to mastery",
        "Learn from criticism and feedback",
        "Find lessons and inspiration in others' success",
        "Use the word 'yet' when facing difficulties"
    ]
    for tip in tips:
        st.write(f"• {tip}")


def goals_page():
    st.header("Set Your Growth Goals")
    goal = st.text_input("Enter a personal growth goal:")
    if st.button("Save Goal"):
        st.success(f"Goal saved: {goal}")
        st.write(
            "Remember, the journey is just as important as the destination. Embrace the process!")


if __name__ == "__main__":
    main()
