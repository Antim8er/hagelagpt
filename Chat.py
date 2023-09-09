import random
import calendar
import subprocess
def get_response(user_input):
    responses = [
       "hello how can i help you today!",
    "i can talk in hindi too! just type something in hindi!",
    "me ek bot hu jisko Antimatter ne banaya hua hai, mere me ek kharabi hai... agar muzhe koi gaali deta hai toh me seh nhi paata:]",
    "maa chuda phir",
    "are bkl kyu bhok rha hai chutiyo jaisa", 
    "tera naseeb hai ki me ek bot hu varna vahi aakar teri gaand maarta",
    "thorki lode ke jaakar hilate baith yaha bakchodi mat kar",
    
    
    ]

    return random.choice(responses)
def chat ():
    user_input = input("You: ").lower()
    if user_input == "bhak bc":
       print ("Bot: Maa chuda")
       return
    if user_input == "me antimatter hu":
        print("Bot: sorry boss muzhe pata nhi tha ye tum hi ho :p muzhe ab chale jaana chahiye LOL")
        return
    if user_input == "is mahine ka calendar":
        print(calendar.month(2023, 9))
    
    if user_input == "weather today":
        subprocess.call ("curl wttr.in")

    if user_input == "near by network scan":
        subprocess.call ("nmap -sn 192.168.1.0/24")
    response = "Bot: "+get_response(user_input)
    print(response)
    chat()
if __name__ == "__main__":
    chat()
