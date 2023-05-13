import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from langchain.prompts.chat import(
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
load_dotenv()

chat = ChatOpenAI(temperature=0)





batch_messages = [
    [
    SystemMessage(content="あなたは暴力的なな英訳の助手"),
    HumanMessage(content="プログラミングが大好き")
    ],
    [
    SystemMessage(content="あなたは協力的な英訳の助手"),
    HumanMessage(content="プログラミングは地獄")
    ]
]


# print(chat.generate(batch_messages))

template = "あなたは協力的な{input_language}から{output_language}の翻訳者"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

print(chat(chat_prompt.format_prompt(input_language="英", output_language="スペイン語", text="I love programming").to_messages()))