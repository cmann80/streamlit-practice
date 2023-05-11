from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=0)

print(chat([HumanMessage(content="この文章を英訳してください。私はプログラミングが大好きです")]))

