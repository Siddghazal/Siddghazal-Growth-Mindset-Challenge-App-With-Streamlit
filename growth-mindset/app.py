import streamlit as st
import random

# Page Title
st.title("🌿 Gratitude & Growth Challenge")

# Welcome Message
st.header("😊 Welcome to Your Gratitude & Growth Journey!")
st.write("A strong mindset starts with gratitude! Reflect on your daily experiences, appreciate the little things, and embrace personal growth.")

# Growth Mindset & Gratitude Quote
quotes = [
    "Every day may not be good, but there is something good in every day.",
    "Gratitude turns what we have into enough.",
    "The more grateful I am, the more beauty I see in life.",
    "Gratitude and growth go hand in hand—embrace both!"
]
st.header("💡 Growth & Gratitude Quote of the Day")
st.write(f"> *{random.choice(quotes)}*")

# Daily Gratitude Affirmation
affirmations = [
    "Gratitude opens the door to abundance.",
    "Each day is a new opportunity to be grateful.",
    "I am thankful for the challenges that help me grow."
]
st.header("🙏 Daily Gratitude Affirmation")
st.write(f"**{random.choice(affirmations)}**")

# Gratitude Section
st.header("💖 What Are You Grateful For Today?")
st.write("Gratitude helps you shift your focus to the positive things in life. Write down at least three things you are grateful for today!")
gratitude = st.text_area("Express your gratitude:")

if gratitude:
    st.success("🌟 Beautiful! Practicing gratitude brings happiness and positivity into your life.")
else:
    st.info("Take a moment to appreciate the little things—what made you feel grateful today?")

# Mood Tracker
st.header("😊 How Are You Feeling Today?")
mood = st.radio("Select your current mood:", ["Grateful 🙏", "Happy 😊", "Motivated 🚀", "Calm 🌿", "Tired 😴", "Stressed 😟"])

if mood:
    st.write(f"💙 You are feeling: {mood}. Recognizing your emotions helps you grow!")

# Challenge Section
st.header("💪 Challenge Yourself with Gratitude!")
st.write("Personal growth starts with stepping out of your comfort zone. What challenge will you take on today?")

random_challenges = [
    "Write down 5 things you are grateful for and why.",
    "Express gratitude to someone who has helped you.",
    "Take 10 minutes to appreciate nature around you.",
    "Reflect on a past challenge and find something to be grateful for in it.",
    "Start a gratitude journal and write in it daily."
]

suggested_challenge = random.choice(random_challenges)

challenge = st.text_input("Set your challenge for today:", placeholder=suggested_challenge)

if challenge:
    st.success(f"🔥 Awesome! Challenge accepted: **{challenge}**. Embrace it with gratitude!")
else:
    st.warning("Choose a challenge that helps you grow and practice gratitude!")

# Learning & Gratitude Reflection
st.header("📝 Reflect on Your Learning & Gratitude")
st.write("Gratitude and growth go hand in hand. Reflect on what you learned today and how gratitude played a role in it.")
reflection = st.text_area("Write about your experience:")

if reflection:
    st.success(f"📖 Insightful! Your reflection: **{reflection}**. Keep growing with gratitude!")
else:
    st.info("Every experience teaches us something. What did you learn today?")

# Kindness & Gratitude Section
st.header("💞 Spread Kindness with Gratitude")
st.write("Kindness and gratitude make the world a better place. How will you spread kindness today?")
kindness = st.text_area("Write one kind act you will do today:")

if kindness:
    st.success("🌟 Amazing! Kindness, like gratitude, creates positive ripples in the world.")
else:
    st.info("A small act of kindness can make a big difference. Plan one today!")


# Footer
st.write("---")
st.write("🌸 Keep practicing gratitude and challenging yourself. Growth is a journey, and gratitude makes it beautiful! 💕")
st.write("**✍️ Made with ❤️ by Ghazala Siddiqui**")
