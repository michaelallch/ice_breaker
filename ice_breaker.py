from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profiles
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

information = """
Elon Musk (prononcé en anglais : /ˈiː.lɒn ˈmʌsk/), né le 28 juin 1971 à Pretoria (Afrique du Sud), est un entrepreneur, chef d'entreprises et milliardaire sud-africain, canadien et américain.

Il est cofondateur et président-directeur général de la société astronautique SpaceX et directeur général de la société automobile Tesla. En janvier 2021, selon Bloomberg, Elon Musk devient, à 49 ans, l'homme le plus riche du monde, avec une fortune estimée à plus de 192,3 milliards de dollars. En octobre 2022, il devient le propriétaire de Twitter, par un achat à 44 milliards de dollars.

Il commence sa carrière dans les affaires, comme cofondateur de la société de logiciels Zip2 avec son frère, Kimbal. La start-up est acquise par Compaq pour 307 millions de dollars en 1999. La même année, Musk cofonde la banque en ligne X.com, qui fusionne avec Confinity en 2000 pour former PayPal. eBay rachète PayPal en 2002 pour 1,5 milliard de dollars.

En 2002, Musk fonde SpaceX, un fabricant aérospatial et une société de services de transport spatial, et en est le PDG. En 2004, il investit 6,5 milliards de dollars dans le constructeur de véhicules électriques Tesla, en devient le premier actionnaire et intègre son conseil d'administration, avant de prendre le poste de PDG en 2008. En 2006, il participe à la création de SolarCity, une société d'énergie solaire qui est ensuite acquise par Tesla et devient Tesla Energy. En 2015, il cofonde et copréside OpenAI, une association de recherche promouvant l'intelligence artificielle amicale, qu'il quitte en 2018. En 2016, il fonde The Boring Company, société de construction de tunnels, et Neuralink, société de neurotechnologie.

À partir de 2018, Elon Musk a régulièrement des déboires avec la Securities and Exchange Commission (SEC), et est notamment accusé de manipuler la bourse, en usant de son influence, notamment sur les médias sociaux, dont Twitter. Ses actions et déclarations sont très médiatisées.
"""

if __name__ == "__main__":
    print("Hello LangChain")

    linkedin_profile_url = linkedin_lookup_agent(name="Thomas benard")

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

    linkedin_data = linkedin_profile_url
    # linkedin_data = scrape_linkedin_profiles(linkedin_profile_url=linkedin_profile_url)
    print(chain.run(information=linkedin_data))
