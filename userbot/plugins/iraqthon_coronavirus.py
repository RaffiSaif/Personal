#Hello. These files are all private to Source Iraq Thun. 
#In short, there are files registered for Source, another group. 
#You do not need to write a file from the beginning for the sake of rights, 
#and there are complete files. Thank you for installing Iraq Thun. 
#Our channel is here: https://t.me/Bomber
"""CoronaVirus LookUp
Syntax: .corona <country>"""
from .. import CMD_HELP
from covid import Covid
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

@borg.on(admin_cmd(pattern="corona(?: |$)(.*)"))
@borg.on(sudo_cmd(pattern="corona(?: |$)(.*)",allow_sudo = True))
async def corona(event):
    if event.pattern_match.group(1):
        country = event.pattern_match.group(1)
    else:
        country = "World"
    covid = Covid(source="worldometers")
    data = ""
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data['confirmed']+country_data['new_cases']
        hmm2 = country_data['deaths']+country_data['new_deaths']
        data +=  f"\n⚠️Confirmed   : `{hmm1}`"
        data +=  f"\n😔Active           : `{country_data['active']}`"
        data +=  f"\n⚰️Deaths         : `{hmm2}`"
        data +=  f"\n🤕Critical          : `{country_data['critical']}`"
        data +=  f"\n😊Recovered   : `{country_data['recovered']}`"
        data +=  f"\n💉Total tests    : `{country_data['total_tests']}`"
        data +=  f"\n🥺New Cases   : `{country_data['new_cases']}`"
        data +=  f"\n😟New Deaths : `{country_data['new_deaths']}`"
    else:
        data += "\nNo information yet about this country!"
    await edit_or_reply(event ,"**Corona Virus Info in {}:**\n{}".format(country.capitalize(), data))

CMD_HELP.update({"coronavirus":
   "`.covid ` <country name>\
   \n**USAGE :** Get an information about covid-19 data in the given country."
})
