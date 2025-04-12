import speech_recognition as sr
import pyttsx3

tasks = []


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"🗣 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def add_task(task):
    tasks.append(task)
    speak(f"Task added: {task}")

def view_tasks():
    if not tasks:
        speak("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            speak(f"Task {i}: {task}")

def remove_task(index):
    try:
        removed = tasks.pop(index - 1)
        speak(f"Removed task: {removed}")
    except IndexError:
        speak("Invalid task number.")

def run_task_manager():
    speak("Welcome to your voice task manager. Say a command.")

    while True:
        command = recognize_speech()

        if not command:
            continue

        if command.startswith("add "):
            task = command[4:]
            add_task(task)

        elif command.startswith("remove task"):
            parts = command.split()
            if len(parts) >= 3 and parts[2].isdigit():
                remove_task(int(parts[2]))
            else:
                speak("Please say the task number to remove.")

        elif "view tasks" in command:
            view_tasks()

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        else:
            speak("Unknown command. Please say add, view, remove or exit.")

if __name__ == "__main__":
    run_task_manager()
