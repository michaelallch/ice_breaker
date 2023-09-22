import os
import requests


def scrape_linkedin_profiles(linkedin_profile_url: str):
    """scrape information from linkedin profiles,
    Manually scrape the information from the linkedinf profile"""
    # api_endpoint = "https://nubela.co/proxyurl/api/v2/linkedin"
    # header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    # response = requests.get(
    #    api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    # )
    response = requests.get(
        "https://gist.githubusercontent.com/michaelallch/25a115836c5e0475d09e925783fea910/raw/3574a3f0316795d2d034c0040f537e8777ae4425/eden-marco.json"
    )
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
