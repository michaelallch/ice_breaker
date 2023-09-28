from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profiles
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

from third_parties.twitter import scrape_user_tweets
from agents.linkedin_lookup_agent import lookup as twitter_lookup_agent


name = "emmanuel macron"
if __name__ == "__main__":
    print("Hello LangChain")

    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = linkedin_profile_url
    # linkedin_data = scrape_linkedin_profiles(linkedin_profile_url=linkedin_profile_url)

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=5)

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two intersting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=tweets))
    print(tweets)
