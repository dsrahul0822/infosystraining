from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatOpenAI(model="gpt-5.1")

def run_chat():
    chat_history=[]
    while True:
        user = input("You: ")
        if user.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        else:
            chat_history.append(f"User: {user}")
            full_prompt = "\n".join(chat_history)
            result = chatmodel.invoke(full_prompt)  
            bot_reply = result.content   
            print(f"Bot:", result.content)
            chat_history.append(f"AI: {bot_reply}")
            #print(chat_history)

if __name__ == "__main__":
    run_chat()