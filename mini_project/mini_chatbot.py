from ollama import chat

System_msg = "You are a friendly tutor.Answer in warm tones.Answer in one sentence."
history = [{"role":"system","content":System_msg}]
question_counter = 0

print("WELCOME")
while True:
    question = input("You:")
    if question =="":

        print("priya : please type something.")
        continue

    if question.lower().strip()=="/help":
        print("-----Available commands -------")
        print("/history - displays converssation history")
        print("/clear - clears chat history")
        print("/help - displays the list")
        print("exit - quits the chatbot")
        print("-----------------------------------")
        print()
        continue

    if question.lower().strip() == "/history":
        print("--------Your Conversation so far------")
        if len(history) < 2:
            print("Nothing here so far!")
        for msg in history[1:]:
            if msg.role == "Priya":
                speaker = "You"
            else:
                speaker = "Priya❤️"
            print(f"{speaker}: {msg.content}")
        print("-----------------------------------")
        print()
        continue
        
    if question.lower().strip() == "/clear":
        history = [{"role":"System","content":System_msg}]
        print("Your history is cleared.Start a fresh conversation.")
        continue

    if question.lower().strip() == "bye":
        print("Priya🤗:Goodbye Priya. please come back soon!😢😢")
        print(f"you asked {question_counter} questions today.Good job!")
        break
    history.append({"role":"user","content":question})
    question_counter+= 1
    try:
        response = chat(
                model= "llama3.2",
                messages= history
            )
        reply = response.message.content
        history.append({"role":"Priya","content":reply})
        print(f"Priya ❤️:{reply}")
        print()
        print("----------")
    except Exception as e:
        print("Unknown issue.Is Ollama running?")
/personality
you type the personality
reset the system msg, print confirmation
and continue the loop
