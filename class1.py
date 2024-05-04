from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain



if __name__ == '__main__':
    print ("Hello Worlds")
    information = """John Zachary DeLorean (/dəlɔriən/ də-LOR-ee-ən; January 6, 1925[1]  March 19, 2005) was an American engineer, inventor, and executive in the U.S. automobile industry. He is widely known as founder of the DeLorean Motor Company, as well as for his work at General Motors.[2]

DeLorean managed the development of several vehicles throughout his career, including the Pontiac GTO, Pontiac Firebird, Pontiac Grand Prix, Chevrolet Cosworth Vega, and DMC DeLorean, which was featured in the 1985 film Back to the Future. He was the youngest division chief in General Motors history, then left to start the DeLorean Motor Company (DMC) in 1973. Production delays meant that DMC's first car did not reach the consumer market until 1981, when a depressed buying market was compounded by lukewarm reviews from critics and the public. After a year, the DeLorean had failed to recover its $175 million investment costs, unsold cars accumulated, and the company was in financial trouble.[3]

In October 1982, DeLorean was charged with cocaine trafficking after FBI informant James Hoffman solicited him as financier in a scheme to sell 220 lb (100 kg) of cocaine worth approximately $24 million. DMC was insolvent at the time and $17 million in debt. Hoffman had approached DeLorean, a man whom he barely knew with no prior criminal record, and DeLorean was able to successfully defend himself at trial under the procedural defense of police entrapment. The trial ended in a not guilty verdict in August 1984, by which time DMC had filed for bankruptcy and ceased operations.
    """

    sumary_templeta= """
    Given the information {information} about a person i want you to create:
    1. a 15 word setence about the person or the object
    2. a good quality of the person of the object
    """

    sumary_promopt_templetae = PromptTemplate(input_variables=["information"],template=sumary_templeta)

    llm = ChatOpenAI(base_url = 'http://localhost:11434/v1',api_key='ollama',model='llama3')

    chain = LLMChain(llm=llm, prompt=sumary_promopt_templetae)
    res = chain.invoke(input={"information":information})
    
    print (res)

