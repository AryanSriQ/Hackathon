# from dotenv import dotenv_values
# from hugchat import hugchat
# from hugchat.login import Login
#
#
#
# secrets = dotenv_values('hf.env')
# hf_email = secrets['EMAIL']
# hf_pass =  secrets['PASS']
#
# # Function for generating LLM response
# def generate_response(prompt_input, email, passwd):
#     # Hugging Face Login
#     sign = Login(email, passwd)
#     cookies = sign.login()
#     # Create ChatBot
#     chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
#     return chatbot.chat(prompt_input)
#
#
# print("Enter the Prompt: ")
# prompt = input()
# response = generate_response(prompt,hf_email,hf_pass)
#
# print("Output: ")
# print(response)

st = "Indian Generate in 100 words"
if "Generate in 100 words"  in st:
    print("Yes")
else:
    print("no")