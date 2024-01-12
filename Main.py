from elevenlabs import generate, play
import openai
import speech_recognition as sr
# Set up your OpenAI API credentials
openai.api_key = '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'

# Use speech recognition to convert speech to text for feedback
def get_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please provide your feedback:")
        audio = r.listen(source)
    try:
        feedback = r.recognize_google(audio)
        return feedback
    except sr.UnknownValueError:
        print("Sorry, I could not understand your feedback.")
    except sr.RequestError as e:
        print("Sorry, there was an error processing your request. Please try again later.")
    return ''

def left():
    print("You go left.")

def right():
    print("You go right.")
    
def forward():
    print("You go forward.")

# Call the OpenAI API to get a response
# response = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt=prompt,
#     max_tokens=100,
#     n=1,
#     stop=None,
#     temperature=0.7
# )


#if 'left()' in response:
    left()
#if 'right()' in response:
    right()
#if 'forward()' in response:
    forward()
#else:
    print("The feedback does not contain any functions.")
#while True:
    print(get_mic())

tts = "Prompt"

audio = generate(
  text=tts,
  voice="Adam",
  model="eleven_multilingual_v2"
)
play(audio)